# -*- coding: utf-8 -*-
"""
Método de Newton-Raphson para aproximação do valor de pi.

Este programa implementa o método numérico de Newton-Raphson para encontrar
uma aproximação do número pi com precisão de 5 casas decimais.
"""
import math
import sys
import io

def funcao(x):
    """
    Função cuja raiz é π: f(x) = sin(x)
    A raiz de sin(x) no intervalo (0, 4) é π.
    """
    return math.sin(x)

def derivada_funcao(x):
    """
    Derivada da função: f'(x) = cos(x)
    """
    return math.cos(x)

def newton_raphson(x0, precisao=1e-5, max_iteracoes=1000):
    """
    Implementa o método de Newton-Raphson para encontrar a raiz de uma função.
    
    Args:
        x0: Valor inicial da aproximação
        precisao: Precisão desejada para a solução
        max_iteracoes: Número máximo de iterações permitidas
        
    Returns:
        Uma tupla contendo:
        - Aproximação da raiz
        - Número de iterações realizadas
        - Erro final
    """
    x = x0
    iteracao = 0
    erro = float('inf')
    
    while erro > precisao and iteracao < max_iteracoes:
        x_novo = x - funcao(x) / derivada_funcao(x)
        erro = abs(x_novo - x)
        x = x_novo
        iteracao += 1
    
    return x, iteracao, erro

def main():
    # Configura a codificação de saída para UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # Configuração inicial
    x0 = 3.0  # Valor inicial próximo a pi
    precisao = 1e-5
    
    print("Método de Newton-Raphson para aproximação de pi")
    print("-" * 50)
    print(f"Valor inicial (x0): {x0}")
    print(f"Precisão desejada: {precisao}")
    
    # Executa o método de Newton-Raphson
    pi_aproximado, iteracoes, erro_final = newton_raphson(x0, precisao)
    
    # Exibe os resultados
    print("\nResultados:")
    print(f"Valor aproximado de pi: {pi_aproximado:.5f}")
    print(f"Valor real de pi:      {math.pi:.5f}")
    print(f"Número de iterações:  {iteracoes}")
    print(f"Erro final:           {erro_final:.10f}")

if __name__ == "__main__":
    main()
