data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('共有', len(data), '筆留言')
x = input('請輸入你想看第幾筆留言:')
x = int(x)
print(data[x])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('資料總長度是',sum_len)
print('平均長度是',sum_len / len(data))
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('資料一共有',len(good),'有good')
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有',len(new),'筆資料小於100字')


