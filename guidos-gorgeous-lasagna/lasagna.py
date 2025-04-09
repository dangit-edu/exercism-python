EXPECTED_BAKE_TIME = 40 # int - represents the minutes the lasagna should bake in the oven
PREPARATION_TIME = 2 # int - represents the minutes each layer of lasagna takes to prepare, before baking

def bake_time_remaining(elapsed_bake_time):
    """Calculate the lasagna's elapsed baking time.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that returns how many remaining minutes the lasagna needs to bake, based on
    the elapsed minutes the lasagna has already baked in the oven.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the lasagna preparation time.

    :param number_of_layers: int - number of layers that comprise the lasagna.
    :return: int - how many total minutes to prepare the lasagna.

    Function that returns the total minutes needed to prepare the lasagna before
    baking, based on its number of layers.
    """

    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the lasagna's total elapsed cooking time.
    
    :param number_of_layers: int - number of layers that comprise the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.

    Function that returns how many total elapsed minutes the lasagna has been cooked, 
    comprised of the combined preparation and elapsed baking times. 
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time