product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = int(input('請輸入商品價格:'))
	product.append([name, price])
print(product)

with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') 
	for p in product:
		f.write(p[0] +',' + str(p[1]) + '\n')