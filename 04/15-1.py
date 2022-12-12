name = input("상품명을 입력하세요: ")
price = input("가격을 입력하세요: ")
count = input("갯수를 입력하세요: ")


products = {}
products[name] = (price, count)
print(products)