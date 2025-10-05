def verificar_erro(string):
    erros = 0
    for letra in string:
        if letra < 'a' or letra > 'm':
            erros += 1
    if erros == 0:
        return f"printer_success: {erros}/{len(string)}"
    else:
        return f"printer_error: {erros}/{len(string)}"


s1 = "aaabbbbhaijjjm"
s2 = "aaaxbbbbyyhwawiwjjjwwm"

print(verificar_erro(s1))
print(verificar_erro(s2))
