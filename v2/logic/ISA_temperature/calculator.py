from logic.constants import CONSTANTS

def compute_temperature_from_altitude(alt, units):
    """
    Computes ISA temperature in the troposphere and tropopause (0-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Temperature (K or R depending on units)
        """
    
    const = _constants(units)
    h11 = const["h11"]
    h20 = const["h20"]
    h32 = const["h32"]
    h47 = const["h47"]
    h51 = const["h51"]
    h71 = const["h71"]
    h86 = const["h86"]

    if alt < h11:
        T = _compute_temperature_from_altitude_troposphere(alt, const)
    elif h11 <= alt < h20:
        T = _compute_temperature_from_altitude_tropopause(alt, const)
    elif h20 <= alt < h32:
        T = _compute_temperature_from_altitude_stratosphere_lower(alt, const)
    elif h32 <= alt < h47:
        T = _compute_temperature_from_altitude_stratosphere_upper(alt, units)
    elif h47 <= alt < h51:
        T = _compute_temperature_from_altitude_stratopause(alt, units)
    elif h51 <= alt < h71:
        T = _compute_temperature_from_altitude_mesospher_lower(alt, units)
    elif h71 <= alt <= h86:
        T = _compute_temperature_from_altitude_mesosphere_upper(alt, units)

    return T

def _constants(units):
    """
    Finds constants and formats in dictionary.

    Parameters:
        units (str): "si" or "english"

    Returns:
        Dictionary of constants
        """
    return{
        "T0":CONSTANTS[units]["T0"],
        "T11":CONSTANTS[units]["T11"],
        "T20":CONSTANTS[units]["T20"],
        "T32":CONSTANTS[units]["T32"],
        "T47":CONSTANTS[units]["T47"],
        "T51":CONSTANTS[units]["T51"],
        "T71":CONSTANTS[units]["T71"],
        "h11":CONSTANTS[units]["h11"],
        "h20":CONSTANTS[units]["h20"],
        "h32":CONSTANTS[units]["h32"],
        "h47":CONSTANTS[units]["h47"],
        "h51":CONSTANTS[units]["h51"],
        "h71":CONSTANTS[units]["h71"],
        "h86":CONSTANTS[units]["h86"],
        "L_tropo":CONSTANTS[units]["L_tropo"],
        "L_strato_lower":CONSTANTS[units]["L_strato_lower"],
        "L_strato_upper":CONSTANTS[units]["L_strato_upper"],
        "L_meso_lower":CONSTANTS[units]["L_meso_lower"],
        "L_meso_upper":CONSTANTS[units]["L_meso_upper"],
    }

def _compute_temperature_from_altitude_troposphere(alt, const):
    """
    Computes temperature from alititude in the troposphere (0-11 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T0 = const["T0"]
    L= const["L_tropo"]
    T = T0 + L*alt

    return T

def _compute_temperature_from_altitude_tropopause(alt, const):
    """
    Computes temperature from alititude in the tropopause (11-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T11 = const["T11"]
    T = T11

    return T

def _compute_temperature_from_altitude_stratosphere_lower(alt, const):
    """
    Computes temperature from alititude in the stratosphere (20-32 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T20 = const["T20"]
    L = const["L_strato_lower"]
    h20 = const["h20"]
    T = T20 + L*(alt - h20)

    return T

def _compute_temperature_from_altitude_stratosphere_upper(alt, const):
    """
    Computes temperature from alititude in the stratosphere (32-47 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T32 = const["T32"]
    L = const["L_strato_upper"]
    h32 = const["h32"]
    T = T32 + L*(alt - h32)

    return T

def _compute_temperature_from_altitude_stratopause(alt, const):
    """
    Computes temperature from alititude in the stratopause (47-51 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T47 = const["T47"]
    T = T47

    return T

def _compute_temperature_from_altitude_tropopause(alt, const):
    """
    Computes temperature from alititude in the tropopause (11-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T11 = const["T11"]
    T = T11

    return T

def _compute_temperature_from_altitude_mesospher_lower(alt, const):
    """
    Computes temperature from alititude in the mesospher (51-71 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T51 = const["T51"]
    L = const["L_meso_lower"]
    h51 = const["h51"]
    T = T51 + L*(alt - h51)

    return T

def _compute_temperature_from_altitude_mesosphere_upper(alt, const):
    """
    Computes temperature from alititude in the mesosphere (71-86 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Temperature (K or R depending on units)
        """
    T71 = const["T71"]
    L = const["L_meso_upper"]
    h71 = const["h71"]
    T = T71 + L*(alt - h71)

    return T