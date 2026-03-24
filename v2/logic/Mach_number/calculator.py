from logic.Speed_of_sound.calculator import (
    compute_speed_of_sound_from_temperature, 
    compute_speed_of_sound_from_altitude
    )

def compute_mach_number_from_temperature(temp, speed, units):
    """
    Computes Mach number from temperature and speed.

    Parameters:
        temp (float): Temperature (K or R depending on units)
        speed (float): Speed (m/s or ft/s depending on units)
        units (str): "si" or "english"

    Returns:
        float: Mach number (m/s or ft/s depending on units)
        """
    speed_of_sound = compute_speed_of_sound_from_temperature(temp, units)
    _check_inputs(speed_of_sound, speed)

    mach_number = speed/speed_of_sound

    return mach_number

def compute_mach_number_from_altitude(alt, speed, units):
    """
    Computes Mach number from altitude and speed.

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        speed (float): Speed (m/s or ft/s depending on units)
        units (str): "si" or "english"

    Returns:
        float: Mach number (m/s or ft/s depending on units)
        """
    speed_of_sound = compute_speed_of_sound_from_altitude(alt, units)
    _check_inputs(speed_of_sound, speed)

    mach_number = speed/speed_of_sound

    return mach_number

def compute_mach_number_from_speed_of_sound(speed_of_sound, speed):
    """
    Computes Mach number from the speed of sound and speed.

    Parameters:
        speed_of_sound (float): Speed of sound (m/s or ft/s depending on units)
        speed (float): Speed (m/s or ft/s depending on units)

    Returns:
        float: Mach number (m/s or ft/s depending on units)
        """
    _check_inputs(speed_of_sound, speed)
    
    mach_number = speed/speed_of_sound

    return mach_number

def compute_speed_from_mach_number(mach_number, speed_of_sound):
    """
    Computes speed from the Mach number and speed of sound.

    Parameters:
        mach_number (float): Mach number
        speed_of_sound (float): Speed of sound (m/s or ft/s depending on units)

    Returns:
        float: Speed (m/s or ft/s depending on units)
        """
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_from_temperature(mach_number, temp, units):
    """
    Computes speed from the temperature and temperature.

    Parameters:
        mach_number (float): Mach number
        temp (float): Temperature (K or R depending on units)
        units (str): "si" or "english"

    Returns:
        float: Speed (m/s or ft/s depending on units)
        """
    speed_of_sound = compute_speed_of_sound_from_temperature(temp, units)
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_from_altitude(mach_number, alt, units):
    """
    Computes speed from the Mach number and altitude.

    Parameters:
        mach_number (float): Mach number
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Speed (m/s or ft/s depending on units)
        """
    speed_of_sound = compute_speed_of_sound_from_altitude(alt, units)
    speed = mach_number*speed_of_sound

    return speed

def compute_speed_of_sound_from_mach_number(speed, mach_number):
    """
    Computes speed of sound from the speed and Mach number.

    Parameters:
        speed (float): Speed (m/s or ft/s depending on units)
        mach_number (float): Mach number

    Returns:
        float: Speed of sound (m/s or ft/s depending on units)
        """
    speed_of_sound = speed/mach_number

    return speed_of_sound

def _check_inputs(speed_of_sound, speed):
    if speed_of_sound <= 0:
        raise ValueError("Speed of sound must be positive.")
    if speed < 0:
        raise ValueError("Speed cannot be negative.")
    return