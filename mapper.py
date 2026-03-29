def map_device(dev):
    if dev["type"] == "mos":
        if "pmos" in dev.get("model", "").lower():
            return ("analogLib", "pmos")
        return ("analogLib", "nmos")

    if dev["type"] == "resistor":
        return ("analogLib", "res")

    if dev["type"] == "capacitor":
        return ("analogLib", "cap")

    return ("analogLib", "res")