shopping_dict = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["bułki", "chleb", "pączek"]
}
print("Lista Zakupów:")
licznik = 0

for shop in shopping_dict.keys():
    products = [product.capitalize() for product in shopping_dict[shop]]
    licznik += len(products)
    print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {products}") 
print(f"W sumie kupuję {licznik} produktów.")