def even_odd_verifier(n: int) -> str:
    if n % 2 == 0:
        return "par"
    else:
        return "impar"

even_odd_verifier(9)