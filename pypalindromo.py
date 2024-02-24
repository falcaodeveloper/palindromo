def palindromo(valor):
    contagem = int()
    original = valor
    frase = ''

    valor = valor.casefold()
    valor = valor.replace(' ', '')
    valor = valor.replace('"', '')
    valor = valor.replace('.', '')
    valor = valor.replace(':', '')
    valor = valor.replace('!', '')
    valor = valor.replace('?', '')
    valor = valor.replace(',', '')
    valor = valor.replace(';', '')
    valor = valor.replace('/', '')
    valor = valor.replace('-', '')
    valor = valor.replace('_', '')
    valor = valor.replace('á', 'a')
    valor = valor.replace('à', 'a')
    valor = valor.replace('ã', 'a')
    valor = valor.replace('ê', 'e')
    valor = valor.replace('é', 'e')
    valor = valor.replace('í', 'i')
    valor = valor.replace('ó', 'o')
    valor = valor.replace('õ', 'o')
    valor = valor.replace('ô', 'o')
    valor = valor.replace('ü', 'u')
    
    contagem = len(valor) - 1

    while contagem >= 0:
        frase = frase + valor[contagem]
        contagem -= 1

    return frase.endswith(valor)