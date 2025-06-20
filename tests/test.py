def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
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

if __name__ == "__main__":
    test_calculate_with_empty_list()
    test_calculate_total_with_multiple_product()
    print("Test passed!")