'use client';

import { useState } from 'react';
import { supabase } from '@/lib/supabaseClient';

export interface QuestionData {
  title: string;
  description: string;
  tags: string[];
  price: number;
  mediaFile?: File;
  mediaType?: 'audio' | 'video' | 'none';
}

export default function CreateQuestionForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [tags, setTags] = useState('');
  const [price, setPrice] = useState(10);
  const [mediaFile, setMediaFile] = useState<File | null>(null);
  const [mediaType, setMediaType] = useState<'audio' | 'video' | 'none'>('none');
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [mediaDuration, setMediaDuration] = useState<number | null>(null);

  const MAX_DURATION = 180; // 3 minutos em segundos
  const MAX_SIZE = 50 * 1024 * 1024; // 50 MB

  const validateForm = (): boolean => {
    const newErrors: Record<string, string> = {};

    if (!title.trim()) newErrors.title = 'Título é obrigatório';
    if (title.length > 200) newErrors.title = 'Título muito longo (máx 200 caracteres)';

    if (!description.trim()) newErrors.description = 'Descrição é obrigatória';
    if (description.length < 10) newErrors.description = 'Descrição deve ter pelo menos 10 caracteres';

    if (price < 5 || price > 500) newErrors.price = 'Preço deve estar entre R$5 e R$500';

    if (mediaFile) {
      if (mediaFile.size > MAX_SIZE) {
        newErrors.media = `Arquivo muito grande (máx 50MB). Tamanho: ${(mediaFile.size / 1024 / 1024).toFixed(2)}MB`;
      }

      const validTypes = mediaType === 'audio' 
        ? ['audio/mpeg', 'audio/m4a', 'audio/mp4']
        : ['video/mp4', 'video/quicktime'];

      if (!validTypes.includes(mediaFile.type)) {
        newErrors.media = `Tipo de arquivo inválido. Use: ${mediaType === 'audio' ? 'mp3, m4a' : 'mp4, mov'}`;
      }

      if (mediaDuration !== null && mediaDuration > MAX_DURATION) {
        newErrors.media = `Duração excede o máximo de 3 minutos (atual: ${Math.floor(mediaDuration)}s)`;
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleMediaChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) {
      setMediaFile(null);
      setMediaDuration(null);
      return;
    }

    setErrors((prev) => ({ ...prev, media: '' }));
    setMediaFile(file);
    setMediaDuration(null);

    try {
      const objectUrl = URL.createObjectURL(file);
      const isAudio = file.type.startsWith('audio');
      const mediaEl = document.createElement(isAudio ? 'audio' : 'video');
      mediaEl.preload = 'metadata';
      mediaEl.src = objectUrl;
      mediaEl.onloadedmetadata = () => {
        URL.revokeObjectURL(objectUrl);
        const duration = Number(mediaEl.duration || 0);
        setMediaDuration(Number.isFinite(duration) ? duration : null);
        if (duration && duration > MAX_DURATION) {
          setErrors((prev) => ({ ...prev, media: 'Duração máxima de 3 minutos excedida.' }));
          setMediaFile(null);
          setMediaDuration(null);
          // limpar input
          e.target.value = '';
        }
      };
      mediaEl.onerror = () => {
        URL.revokeObjectURL(objectUrl);
        setErrors((prev) => ({ ...prev, media: 'Não foi possível ler a duração da mídia.' }));
      };
    } catch (_) {
      setErrors((prev) => ({ ...prev, media: 'Falha ao processar a mídia selecionada.' }));
    }
  };

  const formatDuration = (totalSeconds: number) => {
    const m = Math.floor(totalSeconds / 60);
    const s = Math.floor(totalSeconds % 60);
    return `${m}:${s.toString().padStart(2, '0')}`;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) return;

    setLoading(true);

    try {
      const questionData: QuestionData = {
        title,
        description,
        tags: tags.split(',').map(t => t.trim()).filter(t => t),
        price,
        mediaFile: mediaFile || undefined,
        mediaType: mediaFile ? mediaType : 'none',
      };

      // Upload opcional da mídia; DB será criado via webhook após pagamento
      let media_url: string | null = null;

        const { data: userData } = await supabase.auth.getUser();
        const userId = userData.user?.id;
        if (!userId) {
          setErrors({ submit: 'Você precisa estar logado para enviar uma pergunta.' });
          setLoading(false);
          return;
        }

        if (mediaFile) {
          // Upload direto no Storage usando sessão do usuário (requer policies no Supabase)
          const ext = mediaFile.name.split('.').pop();
          const key = `questions/${userId}/${Date.now()}.${ext}`;

          const { data: uploadData, error: uploadError } = await supabase.storage
            .from('question-media')
            .upload(key, mediaFile as File, {
              cacheControl: '3600',
              upsert: false,
              contentType: mediaFile.type,
            });

          if (uploadError) {
            console.error('Upload error', uploadError);
            const maybeStatus = (uploadError as any)?.statusCode || (uploadError as any)?.status || '';
            const raw = JSON.stringify(uploadError);
            const rlsHint = String(uploadError.message || '')
              .toLowerCase()
              .includes('row level security') || String(raw).toLowerCase().includes('row-level security');
            const hint = rlsHint || maybeStatus === 403
              ? ' Verifique as policies do bucket question-media para permitir INSERT por authenticated.'
              : '';
            setErrors({ submit: `Erro ao enviar arquivo de mídia: ${uploadError.message || 'falha desconhecida.'}${hint}` });
            setLoading(false);
            return;
          }

          const { data: publicUrlData } = supabase.storage
            .from('question-media')
            .getPublicUrl(uploadData.path);
          media_url = publicUrlData.publicUrl;
        }
        // Criar sessão de Checkout na API e redirecionar
        const resp = await fetch('/api/checkout', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            user_id: userId,
            title: questionData.title,
            description: questionData.description,
            tags: questionData.tags,
            price: questionData.price,
            media_url,
            media_type: questionData.mediaType === 'none' ? null : questionData.mediaType,
            media_duration_seconds: mediaDuration ? Math.floor(mediaDuration) : null,
          }),
        });

        const data = await resp.json();
        if (!resp.ok || !data?.url) {
          setErrors({ submit: data?.error || 'Falha ao criar sessão de pagamento.' });
          setLoading(false);
          return;
        }

        // Redireciona para o Stripe Checkout
        window.location.href = data.url as string;

      setTitle('');
      setDescription('');
      setTags('');
      setPrice(10);
      setMediaFile(null);
      setMediaType('none');
      setMediaDuration(null);
    } catch (error) {
      setErrors({ submit: 'Erro ao enviar pergunta. Tente novamente.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {success && (
        <div className="p-4 bg-green-100 border border-green-400 text-green-700 rounded">
          ✓ Pergunta enviada com sucesso!
        </div>
      )}

      {errors.submit && (
        <div className="p-4 bg-red-100 border border-red-400 text-red-700 rounded">
          {errors.submit}
        </div>
      )}

      {/* Título */}
      <div>
        <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-2">
          Título da pergunta *
        </label>
        <input
          id="title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Ex: Como conseguir meus primeiros 100 usuários?"
          className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
            errors.title ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {errors.title && <p className="text-red-500 text-sm mt-1">{errors.title}</p>}
      </div>

      {/* Descrição */}
      <div>
        <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-2">
          Descrição detalhada *
        </label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Detalhe sua dúvida, contexto, e o que você já tentou..."
          rows={5}
          className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
            errors.description ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {errors.description && <p className="text-red-500 text-sm mt-1">{errors.description}</p>}
      </div>

      {/* Tags */}
      <div>
        <label htmlFor="tags" className="block text-sm font-medium text-gray-700 mb-2">
          Tags (separadas por vírgula)
        </label>
        <input
          id="tags"
          type="text"
          value={tags}
          onChange={(e) => setTags(e.target.value)}
          placeholder="Ex: startup, marketing, growth"
          className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      {/* Preço */}
      <div>
        <label htmlFor="price" className="block text-sm font-medium text-gray-700 mb-2">
          Preço (R$) *
        </label>
        <input
          id="price"
          type="number"
          value={price}
          onChange={(e) => setPrice(Number(e.target.value))}
          min="5"
          max="500"
          className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
            errors.price ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        <p className="text-xs text-gray-500 mt-1">Você receberá 80% (R${(price * 0.8).toFixed(2)})</p>
        {errors.price && <p className="text-red-500 text-sm mt-1">{errors.price}</p>}
      </div>

      {/* Upload de mídia */}
      <div className="border-2 border-dashed border-gray-300 rounded-lg p-6">
        <p className="text-sm font-medium text-gray-700 mb-4">Adicionar mídia (opcional)</p>

        <div className="space-y-4">
          <div className="flex gap-4">
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                checked={mediaType === 'audio'}
                onChange={() => setMediaType('audio')}
              />
              <span className="text-sm">🎙️ Áudio (mp3, m4a)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                checked={mediaType === 'video'}
                onChange={() => setMediaType('video')}
              />
              <span className="text-sm">🎥 Vídeo (mp4, mov)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                checked={mediaType === 'none'}
                onChange={() => setMediaType('none')}
              />
              <span className="text-sm">Nenhum</span>
            </label>
          </div>

          {mediaType !== 'none' && (
            <div>
              <input
                type="file"
                accept={mediaType === 'audio' ? 'audio/mpeg,audio/m4a,audio/mp4' : 'video/mp4,video/quicktime'}
                onChange={handleMediaChange}
                className="block w-full text-sm text-gray-500
                  file:mr-4 file:py-2 file:px-4
                  file:rounded-lg file:border-0
                  file:text-sm file:font-semibold
                  file:bg-blue-50 file:text-blue-700
                  hover:file:bg-blue-100"
              />
              {mediaFile && (
                <div className="mt-2 p-3 bg-blue-50 rounded-lg">
                  <p className="text-sm text-gray-700">
                    📎 {mediaFile.name} ({(mediaFile.size / 1024 / 1024).toFixed(2)}MB)
                  </p>
                  {mediaDuration !== null && (
                    <p className="text-xs text-gray-600 mt-1">Duração: {formatDuration(mediaDuration)} {mediaDuration > MAX_DURATION ? '(excede 3min)' : ''}</p>
                  )}
                </div>
              )}
              <p className="text-xs text-gray-500 mt-2">Máximo 3 minutos, 50MB</p>
            </div>
          )}

          {errors.media && <p className="text-red-500 text-sm">{errors.media}</p>}
        </div>
      </div>

      {/* Botão submit */}
      <button
        type="submit"
        disabled={loading}
        className="w-full bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400 transition"
      >
        {loading ? '⏳ Enviando...' : '🚀 Enviar Pergunta'}
      </button>
    </form>
  );
}
