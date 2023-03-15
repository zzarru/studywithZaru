test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheating_lst = [key for key, value in test_status.items() if value == 'cheating']
cheating_lst.sort()
for i in cheating_lst:
	del(test_status[i])

print(cheating_lst)

sleeping_lst = [key for key, value in test_status.items() if value == 'sleeping']
for i in sleeping_lst:
	test_status[i] = 'solving'

print(test_status)