'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabaseClient';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import NotificationsBell from './NotificationsBell';

export default function Header() {
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getUser = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      setUser(user);
      setLoading(false);
    };
    getUser();

    const { data: listener } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null);
    });

    return () => {
      listener?.subscription.unsubscribe();
    };
  }, []);

  const handleLogout = async () => {
    await supabase.auth.signOut();
    setUser(null);
    router.push('/');
  };

  if (loading) return null;

  return (
    <header className="bg-white shadow-sm">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-blue-600">
          🎤 MicroMentor
        </Link>

        <div className="flex gap-4 items-center">
          {user ? (
            <>
              <NotificationsBell />
              <Link
                href="/mentor/profile"
                className="px-4 py-2 text-sm font-semibold text-blue-600 hover:bg-blue-50 rounded-lg transition"
              >
                👤 Perfil
              </Link>
              <span className="text-gray-700 text-sm">
                {user.email}
              </span>
              <button
                onClick={handleLogout}
                className="px-4 py-2 text-sm font-semibold text-red-600 hover:bg-red-50 rounded-lg transition"
              >
                Sair
              </button>
            </>
          ) : (
            <>
              <Link href="/auth/login" className="px-4 py-2 text-sm font-semibold text-blue-600 hover:bg-blue-50 rounded-lg transition">
                Login
              </Link>
              <Link href="/auth/signup" className="px-4 py-2 text-sm font-semibold bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
                Cadastro
              </Link>
            </>
          )}
        </div>
      </nav>
    </header>
  );
}
