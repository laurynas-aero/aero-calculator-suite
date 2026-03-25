
CONSTANTS = {
    "si": {
        "gamma": 1.4,
        "R": 287.05,             # J/(kg*K)
        "g": 9.80665,            # m/s^2
        "T0": 288.15,            # K
        "T11": 216.65,           # K
        "T20": 216.65,           # K
        "T32": 228.65,           # K
        "T47": 270.65,           # K
        "T51": 270.65,           # K
        "T71": 214.65,           # K
        "P0": 101325.0,          # Pa
        "h11": 11000,            # m
        "h20": 20000,            # m
        "h32": 32000,            # m
        "h47": 47000,            # m
        "h51": 51000,            # m
        "h71": 71000,            # m
        "h86": 86000,            # m
        "L_tropo": -0.0065,      # K/m
        "L_strato_lower": 0.001, # K/m
        "L_strato_upper": 0.0028,# K/m
        "L_meso_lower": -0.0028, # K/m
        "L_meso_upper": -0.002,  # K/m
        "units": {
            "altitude": "m",
            "temperature": "K",
            "pressure": "Pa",
            "density": "kg/m^3",
            "speed": "m/s"
        }
    },

    "english": {
        "gamma": 1.4,
        "R": 1716.59,             # ft*lbf/(slug*R)
        "g": 32.174,              # ft/s^2
        "T0": 518.67,             # R
        "T11": 398.97,            # R
        "T20": 398.97,            # R
        "T32": 411.57,            # R
        "T47": 487.17,            # R
        "T51": 487.17,            # R
        "T71": 386.37,            # R
        "P0": 2116.22,            # lbf/ft^2
        "h11": 36089,             # ft
        "h20": 65617,             # ft
        "h32": 104987,            # ft
        "h47": 154199,            # ft
        "h51": 167323,            # ft
        "h71": 232940,            # ft
        "h86": 282150,            # ft
        "L_tropo": -0.00356616,   # R/ft
        "L_strato_lower": 0.0003, # R/ft
        "L_strato_upper": 0.00085,# R/ft
        "L_meso_lower": -0.00085, # R/ft
        "L_meso_upper": -0.00061, # R/ft
        "units": {
            "altitude": "ft",
            "temperature": "R",
            "pressure": "lbf/ft^2",
            "density": "slug/ft^3",
            "speed": "ft/s"
        }
    }
}