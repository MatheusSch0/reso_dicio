dicio_sino = {
'felicidade': 'alegria',
'trsite': 'deprimido',
'inteligente': 'esperto',
'casa': 'lar',
}

palavra = input ('Digite aqui sua busca?')

if palvra in dicio_sino:
    sinonimo = dicio_sino[palavra]
    print('a palavra escolhida foi {sinonimo},ela tem no dicionario')
else:
    print('a palvra nãotem no dicionario')
