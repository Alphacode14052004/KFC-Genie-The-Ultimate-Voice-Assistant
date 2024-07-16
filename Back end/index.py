import pandas as pd

menu = pd.read_csv('kfc_data.csv')

def handle_order(order_txt):
    items = [deal for deal in menu['deal'] if deal.lower() in order_txt.lower()]

    if not items:
        return "No items found in your order."

    resp = f"You have ordered {', '.join(items)}. "

    total = calc_total(items)
    resp += f"Your total is Rupees. {total}. "

    return resp


def calculate_total(items):
    total = 0
    for deal in items:
        try:
            price = float(menu.loc[menu['deal'] == deal, 'price (in rs.)'].values[0])
            total += price
        except IndexError:
            print(f"Deal '{deal}' not found in the menu.")
        except ValueError:
            print(f"Invalid price value for deal '{deal}'.")
    return total
