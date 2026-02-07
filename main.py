from parslib import parseText
while 1:
	site = input("Введите адрес сайта: ")
	selector = input("Введите css селектор: ")
	print(parseText(site, selector))