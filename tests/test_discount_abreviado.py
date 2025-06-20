'''
Esta función se encarga de calcular el total de un producto, teniendo en cuenta si tiene descuento o no. 
'''
def calculate_total(products, with_discount=False):
    return sum((product['price']-(product['price']*product.get('discount',0)) for product in products))
print('Paso lo primero')

def test_calculate_with_empty_list():
    assert calculate_total([],[]) == 0

def test_calculate_total_single_product():
    products = [
        {'name': 'Notebook', 'price': 5}
    ]
    assert calculate_total(products) == 5

def test_calculate_total_single_product_with_discount():
    products = [
        {'name': 'Notebook', 'price': 5, 'discount': 0.1}
    ]
    assert calculate_total(products) == 4.5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Notebook", "price": 5, "discount": 0
        },
        {
            "name": "Laptop", "price": 10, "discount": 0.2
        },
        {
            "name": "Cellphone", "price": 5, "discount": 0.1
        },
        {
        "name": "book", "price": 50
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 67.5

if __name__ == "__main__":
    test_calculate_with_empty_list()
    print("Test passed for empty list!")
    test_calculate_total_single_product()
    print("Test passed for single product!")
    test_calculate_total_single_product_with_discount()
    print("Test passed for single product with discount!")
    test_calculate_total_with_multiple_product()
    print("Test passed for multiple products!") 
