import sys
from gemini_parser import parse_with_gemini
from validator import validate
from mapper import map_device
from skill_gen import generate

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py input\\file.sp")
        return

    with open(sys.argv[1], "r") as f:
        netlist = f.read()

    print("Parsing with Gemini...")
    data = parse_with_gemini(netlist)

    print("Validating...")
    devices = validate(data)

    print("Generating SKILL...")
    skill = generate(devices, map_device)

    with open("output\\gen.il", "w") as f:
        f.write(skill)

    print("Done → output\\gen.il")

if __name__ == "__main__":
    main()