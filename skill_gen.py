from config import LIB_NAME, CELL_NAME, VIEW_NAME

def generate(devices, mapper):
    lines = []

    lines.append(
        f'cv = dbOpenCellViewByType("{LIB_NAME}" "{CELL_NAME}" "{VIEW_NAME}" "" "w")'
    )

    # Instances
    x = 0
    for d in devices:
        lib, cell = mapper(d)

        lines.append(
            f'inst_{d["name"]} = dbCreateInst(cv "{lib}" "{cell}" "symbol" {x}:0 "R0")'
        )

        for k, v in d.get("params", {}).items():
            lines.append(f'inst_{d["name"]}~>{k} = "{v}"')

        x += 10

    # Nets
    nets = set()
    for d in devices:
        nets.update(d["nodes"])

    for n in nets:
        lines.append(f'net_{n} = dbCreateNet(cv "{n}")')

    # Connections
    for d in devices:
        inst = f'inst_{d["name"]}'

        if d["type"] == "mos":
            pins = ["D", "G", "S", "B"]
        else:
            pins = ["PLUS", "MINUS"]

        for pin, net in zip(pins, d["nodes"]):
            lines.append(
                f'dbCreateInstTerm({inst} net_{net} "{pin}")'
            )

    return "\n".join(lines)