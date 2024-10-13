words={
    'кринж':'что-то странное, стыдное',
    'lol':'очень смешно',
    'rofl':'шутка',
    'shis' : 'одобрение или восторг',
    'kripovij' :'страшный, пугающий',
    'agritsa' : 'злиться'
    'ucik' : 'учитель'

    
}
vopros = input('enter words:').lower
if vopros in words:
    print('перевод:', words[vopros])
else:
    print('error')
