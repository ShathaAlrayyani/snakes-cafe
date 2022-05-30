
welcoming = "** Welcome to the Snakes Cafe! **\n** Please see our menu below. **\n** \n** To quit at any time, type 'quit' **"
menu = "Appetizers \n-------\nWings\nCookies\nSpring Rolls\n \nEntrees\n-------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n \nDesserts\n--------\nIce Cream\nCake\nPie\n \nDrinks\n------\nCoffee\nTea\nUnicorn Tears"


def decor(func, func2):
    def wrap():
        print("**************************************")
        func()
        print("**************************************")
        print(menu)
        print("**************************************")
        print("** What would you like to order? ** ")
        print("**************************************")
        func2()
    return wrap


def print_text():
    print(welcoming)

def orders():
    dana = menu.split("\n")
    count = 0
    order = input(">")
    while order in dana:
        if order =='quit':
            break
        count = count+1
        print(f'** {count} order of {order} have been added to your meal **')
        order = input(">")



decorater = decor(print_text, orders)
decorater()

