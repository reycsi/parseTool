from parseTool import parse
while 1:
	site = input("Введите адрес сайта: ")
	selector = input("Введите css селектор: ")
	print(parse(site, selector))
