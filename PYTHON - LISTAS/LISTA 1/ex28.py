count = 0
soma = 0

for i in range(5):
    n = int(input())
    if n >= 0:
        soma += n
        count += 1
if count == 0:
    exit()
else:
    media = soma / count
print(media)