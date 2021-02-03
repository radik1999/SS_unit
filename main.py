import math


def fizz_buzz(number: int) -> str:
    if not number % 15:
        return 'FizzBuzz'
    elif not number % 5:
        return 'Buzz'
    elif not number % 3:
        return 'Fizz'
    else:
        return str(number)


def profit(sale: dict) -> float:
    inv = sale.get('inventory')
    return sale.get('sell_price') * inv - sale.get('cost_price') * inv


def quadratic_solutions(a: int, b: int, c: int) -> int:
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return 0
    elif not d:
        return 1
    else:
        return 2


def square_areas_difference(radius: int) -> int:
    return (radius * 2) ** 2 / 2


def list_of_multiples(number: int, length: int) -> list:
    return [i * number for i in range(1, length + 1)]


def format_date(slash_date: str) -> str:
    date_arr = slash_date.split('/')
    date_arr.reverse()
    return ''.join(date_arr)


def lines_are_parallel(line1_params, line2_params):
    a1_coefficient = line1_params[1]
    a2_coefficient = line2_params[1]
    try:
        a1_coefficient = line1_params[1] / line1_params[0]
        a2_coefficient = line2_params[1] / line2_params[0]
    except:
        pass

    return a1_coefficient == a2_coefficient


def vol_shell(r1, r2):
    def vol(r):
        return (4 / 3) * math.pi * r ** 3

    return round(math.fabs(vol(r1) - vol(r2)), 3)


def greeting(name):
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    if name in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST.get(name)}."
    else:
        return "Hi! I'm a guest."


def stupid_addition(par1, par2):
    if type(par1).__name__ == type(par2).__name__:
        if type(par1).__name__ == 'str':
            return int(par1) + int(par2)
        else:
            return str(par1) + str(par2)
    else:
        return None


def is_repdigit(number):
    return number >= 0


def concat(*lists):
    res = []
    for lst in lists:
        res += lst
    return res


# 12
def emptying_values(lst: list) -> list:
    return [type(element)() for element in lst]


# 13
def sum_fractions(lst: list) -> int:
    return round(sum([sub_lst[0] / sub_lst[1] for sub_lst in lst]))


# 14
def get_indices(lst: list, item) -> list:
    res = []
    for indx, element in enumerate(lst):
        if element == item:
            res.append(indx)
    return res



if __name__ == '__main__':
    print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
    # print(type([313])())
