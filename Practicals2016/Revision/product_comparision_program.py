def product_input():
    product_quantity = float(input("Please input quantity: "))
    product_price = float(input("Please input price: "))

    return product_quantity, product_price


def calculate_cheaper_product(product_1_quantity, product_1_price, product_2_quantity, product_2_price):
    product_1_unit_price = product_1_quantity / product_1_price
    product_2_unit_price = product_2_quantity / product_2_price

    if product_1_unit_price < product_2_unit_price:
        return "First"
    else:
        return "Second"


def main():
    product_1_quantity, product_1_price = product_input()
    product_2_quantity, product_2_price = product_input()

    print(calculate_cheaper_product(product_1_quantity, product_1_price, product_2_quantity, product_2_price))

main()
