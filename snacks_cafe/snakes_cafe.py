from restaurant_menu import menu_list


#! Do NOT FORGET TO:
# [1] add the description of the functions
# [2] Write the description about the program in README

print(menu_list)

menu = [
    'Wings',
    'Cookies',
    'Spring Rolls',
    'Salmon',
    'Steak',
    'Meat Tornado',
    'A Literal Garden',
    'Ice Cream',
    'Cake',
    'Pie',
    'Coffee',
    'Tea',
    'Unicorn Tears'
]

orders = {}


def print_order(item_name, item_amount):
    """
        This function prints orders and take too inputs:

        Input:
            item_name: string
            item_amount: int
        Output:
            String contain the two inputs
    """
    add_s = ''
    if item_amount > 1:
        add_s = 's'
    print(
        f'\n** {item_amount} order{add_s} of {item_name.capitalize()} have been added to your meal **\n')


def is_item_exist(item):
    """
        The function check if the item exist or NOT in the orders variable

        Input:
            item: string
        Output:
            return true if the item exist OR None if NOT
    """
    for order in menu:
        if order.lower() == item.lower():
            item.lower()
            try:
                if orders[item]:
                    orders[item] += 1
            except:
                orders[item] = 1
            return True


def print_summary():
    """
        Function print all the orders.

        Inputs: 
            no input
        Output:
            print all orders
    """
    orders_list = list(orders.keys())
    print('----------------- SUMMARY -----------------')
    for order in orders_list:
        print_order(order, orders[order])
    print('-------------------------------------------')


while True:
    get_value = input('> ')
    if get_value.lower() == 'summary':
        print_summary()
        continue

    if get_value.lower() == 'quit':
        break

    if is_item_exist(get_value.lower()):
        item_name = get_value.lower()
        item_amount = orders[item_name]
        print_order(item_name, item_amount)
        continue
    else:
        print('Item does not exist')
        continue
