from logic.ISA_temperature.calculator import compute_temperature_from_altitude
from logic.constants import CONSTANTS

def compute_speed_of_sound_from_temperature(temp, units):
    """
    Computes speed of sound from the temperature.

    Parameters:
        temp (float): Temperature (K or R depending on units)
        units (str): "si" or "english"

    Returns:
        float: Speed of sound (m/s or ft/s depending on units)
        """
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    speed_of_sound = (GAMMA*SPECIFIC_HEAT*temp) ** 0.5

    return speed_of_sound

def compute_speed_of_sound_from_altitude(alt, units):
    """
    Computes speed of sound from the altitude.

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Speed of sound (m/s or ft/s depending on units)
        """
    
    # ADD INPUT CHECKING HERER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    temp = compute_temperature_from_altitude(alt, units)
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    speed_of_sound = ((GAMMA*SPECIFIC_HEAT) * temp) ** 0.5

    return speed_of_sound

def compute_temperature_from_speed_of_sound(speed_of_sound, units):
    """
    Computes temperature from the speed of sound.

    Parameters:
        speed_of_sound (float): Speed of sound (m/s or ft/s depending on units)
        units (str): "si" or "english"

    Returns:
        float: Temperature (K or R depending on units)
        """
    SPECIFIC_HEAT = CONSTANTS[units]["R"]
    GAMMA = CONSTANTS[units]["gamma"]

    temp = (speed_of_sound ** 2) / (GAMMA*SPECIFIC_HEAT)

    return temp