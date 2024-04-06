with open ('reviews.txt', 'r') as file: # 開啟某個檔案並讀取內容，使用with open ('file_name.type', 'r') as ___
	data = []
	count = 0
	for line in file: #  for loop填寫至data清單中
		data.append(line) # 透過.append函式將line內容裝進data[]裏頭中，裏頭100W比留言line
		count += 1 #每裝一筆，count數+1
		if count % 100000 == 0: #如果count /100000且餘數=0時，列印出此時data進行的長度。
			print(len(data))
dic = {}
for line in data: # 由上述data[]中，已經存放100W line
	line_words = line.split() #如果以第一筆留言為例，for第一留言時，以split()將第一留言以''不含空格來拆分。 所以會變成一個一個字宣告為cs中
	for single_word in line_words:
		if single_word in dic: #利用這個方式將single_word存進dic{}
			dic[single_word] += 1 #
		else:
			dic[single_word] = 1	
	break # 當作完第一筆時，break跳出for loop環節。
	#print('test') #因為先遇到break，所以此print根本不會列印。
for single_word in line_words:
	w = input('想查詢什麼字: ')
	if w == 'q':
		print('謝謝使用')
		break
	elif w not in dic:
		print('這個字不在字典裏頭喔!')
	else:
		print('這個', w, '字重複了: ', dic[w], '次')



# print(line_words[0]) # 第一則留言中第一個字
# print('--------分隔線--------')
# print(words[0]) # 第一則留言所有的字
# print('--------分隔線--------')
# print(data[0]) # 第一則留言











#sum_len = 0 # 預計從第0則留言開始計算 字數/留言
#for word in data:
#	sum_len += len(word) #sum_len = sum_len + 1
#print(sum_len) # 確認 +=是否有確實執行
#avg = sum_len/ len(data) # 定義avg
#print(avg)
