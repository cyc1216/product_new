#讀取檔案
product = []
with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f :
		if '商品,價格' in line:
			continue
		s = line.strip().split(',')
		product.append(s)
	'''
    上面取出資料並忽略表頭的快寫法
	product = [line.strip().split(',') for line in f if '商品,價格'  not in line ]
	'''
print(product)	

#輸入新的資料
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = int(input('請輸入商品價格:'))
	product.append([name, price])
print(product)

#印出所有商品與價格
for p in product:
	print(p[0], '的價格為', p[1])

#將輸入的資料寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') 
	for p in product:
		f.write(p[0] +',' + str(p[1]) + '\n')