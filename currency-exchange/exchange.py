def exchange_money(budget, exchange_rate):
    """Function returns value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Function returns the amount of budget money that remains after an exchange.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Function returns the total value of bills an exchange booth would provide, excluding fractional amounts.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """Function returns the number of whole currency bills provided by the exchange booth, given the exchanged amount. 
    The booth will only provide whole bills of the given denomination, and keeps fractional amounts of whole bills.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """Function returns the remaining currency value that this exchange booth would keep from the initial amount, 
    given the denomination of whole bills and the booth's policy of keeping fractional amounts.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount - (amount // denomination) * denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Function returns the maximum value of new currency, given the exchange rate plus the vendor's exchange fee, AKA the "spread".
    The denomination of bills is a whole number and cannot be sub-divided, given the vendor's policy of keeping fractional amounts.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    spread_rate = spread / 100
    vendor_exchange_rate = exchange_rate + (exchange_rate * spread_rate)
    vendor_exchange_value = budget / vendor_exchange_rate
    number_of_bills = vendor_exchange_value // denomination
    vendor_exchange_value_per_policy = int(number_of_bills * denomination)

    return vendor_exchange_value_per_policy
