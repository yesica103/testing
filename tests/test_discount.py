def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total
def calculate_total_discount(products):
    total = 0
    for product in products:
        total += product['price']- (product['price'] * product['discount'])  # Assuming a 10% discount
    return total


def test_calculate_with_empty_list():
   
    assert calculate_total([]) == 0

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Notebook", "price": 5
        },
        {
            "name": "Laptop", "price": 10
        },
        {
            "name": "Cellphone", "price": 5
        },
        {
        "name": "book", "price": 50
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 70

def test_calculate_total_discount_with_empty_list():
    assert calculate_total_discount([]) == 0

def test_calculate_discount_with_multiple_product():
    products = [
        {
            "name": "Notebook", "price": 5, "discount": 0.1
        },
        {
            "name": "Laptop", "price": 10, "discount": 0.1
        },
        {
            "name": "Cellphone", "price": 5, "discount": 0.1
        },
        {
            "name": "book", "price": 50, "discount": 0.1
        }
    ]
    print(calculate_total_discount(products))
    assert calculate_total_discount(products) == 63.0

if __name__ == "__main__":
    test_calculate_with_empty_list()
    print("Test passed for empty list!")
    test_calculate_total_with_multiple_product()
    print("Test passed for multiple products!")
    test_calculate_total_discount_with_empty_list()
    print("Test passed for empty discount list!")
    test_calculate_discount_with_multiple_product()
    print("Test passed for multiple products with discount!")
    print("All tests passed!")
