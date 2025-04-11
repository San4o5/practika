def print_product_names(product_names):
    for name in product_names:
        print(name)

def find_product_by_name(products, product_name, index = 0):
    product_keys = list(products.keys())
    
    if index >= len(product_keys):
        print("Товар не знайдено!")
        return
    
    if product_keys[index] == product_name:
        product_info = products[product_name]
        print(f"Товар знайдено: {product_name}, Ціна: {product_info['Ціна']}, Залишок: {product_info['Залишок']}")
        return
    
    find_product_by_name(products, product_name, index + 1)
