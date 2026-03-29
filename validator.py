def validate(data):
    devices = data.get("devices", [])
    valid = []

    for d in devices:
        if "name" not in d or "nodes" not in d:
            continue

        if d["type"] == "mos" and len(d["nodes"]) != 4:
            continue

        if d["type"] in ["resistor", "capacitor"] and len(d["nodes"]) != 2:
            continue

        valid.append(d)

    return valid