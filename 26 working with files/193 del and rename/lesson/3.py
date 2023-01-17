#create

with open('files/lorem3.txt', mode='x', encoding='utf-8') as file:
	file.write("this is open(mode='x')")

"""encoding:
cp1254 -> windows un turkce encoding formati
os encodingleri ile open -> encoding = utf-8
"""