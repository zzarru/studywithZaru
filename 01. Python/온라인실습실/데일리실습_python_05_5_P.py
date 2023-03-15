words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words_list = list(map(str, words_dict.keys()))
thesaurus = []
for i in words_list:
    if i[0] == 'l':
        i = 'il' + i
    elif i[0] == 'r':
        i = 'ir' + i
    elif i [0] == 'b' or 'm' or 'p':
        i = 'im' + i

    thesaurus.append(i)

thesaurus.sort()
print(thesaurus)



