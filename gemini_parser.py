import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
You are an expert in Cadence Virtuoso and SPICE. You are an expert in reading and converting netlists into structured data. Convert the following netlist into STRICT JSON format:

{
  "devices": [
    {
      "type": "mos|resistor|capacitor",
      "name": "",
      "nodes": [],
      "model": "",
      "params": {}
    }
  ]
}

Rules:
- MOS → 4 nodes
- Resistor/Capacitor → 2 nodes
- Extract values (W, L, resistance, capacitance)
- NO explanation
- ONLY JSON

Netlist:
"""

def parse_with_gemini(netlist_text):
    response = model.generate_content(PROMPT + netlist_text)

    text = response.text

    # Extract JSON safely
    json_text = re.search(r'\{.*\}', text, re.DOTALL).group()

    return json.loads(json_text)