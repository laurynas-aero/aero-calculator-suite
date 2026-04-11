from logic.constants import CONSTANTS
from logic.ISA_temperature.calculator import compute_temperature_from_altitude
from math import exp

def compute_pressure_from_altitude(alt, units):
    """
    Computes ISA pressure. (0-86 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        units (str): "si" or "english"

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
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
        P = _compute_pressure_from_altitude_troposphere(alt, const, units)
    elif h11 <= alt < h20:
        P = _compute_pressure_from_altitude_tropopause(alt, const, units)
    elif h20 <= alt < h32:
        P = _compute_pressure_from_altitude_stratosphere_lower(alt, const, units)
    elif h32 <= alt < h47:
        P = _compute_pressure_from_altitude_stratosphere_upper(alt, const, units)
    elif h47 <= alt < h51:
        P = _compute_pressure_from_altitude_stratopause(alt, const, units)
    elif h51 <= alt < h71:
        P = _compute_pressure_from_altitude_mesosphere_lower(alt, const, units)
    elif h71 <= alt <= h86:
        P = _compute_pressure_from_altitude_mesosphere_upper(alt, const, units)

    return P

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
        "P0":CONSTANTS[units]["P0"],
        "P11":CONSTANTS[units]["P11"],
        "P20":CONSTANTS[units]["P20"],
        "P32":CONSTANTS[units]["P32"],
        "P47":CONSTANTS[units]["P47"],
        "P51":CONSTANTS[units]["P51"],
        "P71":CONSTANTS[units]["P71"],
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
        "g":CONSTANTS[units]["g"],
        "R":CONSTANTS[units]["R"]
    }

def _compute_pressure_from_altitude_troposphere(alt, const, units):
    """
    Computes pressure from alititude in the troposphere (0-11 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P0 = const["P0"]
    T0 = const["T0"]
    L= const["L_tropo"]
    g = const["g"]
    R = const["R"]

    T = compute_temperature_from_altitude(alt, units)

    P = P0*((T/T0))**(-g/(R*L))

    return P

def _compute_pressure_from_altitude_tropopause(alt, const, units):
    """
    Computes pressure from alititude in the troposphere (11-20 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P11 = const["P11"]
    T11 = const["T11"]
    h11 = const["h11"]
    g = const["g"]
    R = const["R"]

    P = P11*exp(-(g*(alt-h11))/(R*T11))

    return P

def _compute_pressure_from_altitude_stratosphere_lower(alt, const, units):
    """
    Computes pressure from alititude in the lower stratosphere (20-32 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P20 = const["P20"]
    T20 = const["T20"]
    L= const["L_strato_lower"]
    g = const["g"]
    R = const["R"]

    T = compute_temperature_from_altitude(alt, units)

    P = P20*((T/T20))**(-g/(R*L))

    return P

def _compute_pressure_from_altitude_stratosphere_upper(alt, const, units):
    """
    Computes pressure from alititude in the upper stratosphere (32-47 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P32 = const["P32"]
    T32 = const["T32"]
    L= const["L_strato_upper"]
    g = const["g"]
    R = const["R"]

    T = compute_temperature_from_altitude(alt, units)

    P = P32*((T/T32))**(-g/(R*L))

    return P

def _compute_pressure_from_altitude_stratopause(alt, const, units):
    """
    Computes pressure from alititude in the stratopause (47-51 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P47 = const["P47"]
    T47 = const["T47"]
    h47 = const["h47"]
    g = const["g"]
    R = const["R"]

    P = P47*exp(-(g*(alt-h47))/(R*T47))

    return P

def _compute_pressure_from_altitude_mesosphere_lower(alt, const, units):
    """
    Computes pressure from alititude in the lower mesosphere (51-71 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P51 = const["P51"]
    T51 = const["T51"]
    L= const["L_meso_lower"]
    g = const["g"]
    R = const["R"]

    T = compute_temperature_from_altitude(alt, units)

    P = P51*((T/T51))**(-g/(R*L))

    return P

def _compute_pressure_from_altitude_mesosphere_upper(alt, const, units):
    """
    Computes pressure from alititude in the upper stratosphere (71-86 km).

    Parameters:
        alt (float): Altitude (m or ft depending on units)
        const (dic): Dictionary of constants

    Returns:
        float: Pressure (Pa or lbf/ft² depending on units)
        """
    P71 = const["P71"]
    T71 = const["T71"]
    L= const["L_meso_upper"]
    g = const["g"]
    R = const["R"]

    T = compute_temperature_from_altitude(alt, units)

    P = P71*((T/T71))**(-g/(R*L))

    return P