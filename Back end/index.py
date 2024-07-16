import pandas as pd

menu = pd.read_csv('kfc_data.csv')

def handle_order(order_txt):
    itms = []
    for deal in menu['deal']:
        if deal.lower() in order_txt.lower():
            items.append(deal)

    resp = f"You have ordered {', '.join(items)}. "

    total = calc_total(items)
    resp += f"Your total is Rupees. {total}. "

    return items


def calculate_total(itms):
    total = 0
    for deal in itms:
        try:
            price = menu.loc[menu['deal'] == deal, 'price (in rs.)'].values[0]
            total += float(price)
        except IndexError:
            print(f"Deal '{deal}' not found in the menu.")
        except ValueError:
            print(f"Invalid price value for deal '{deal}'.")
    return total
