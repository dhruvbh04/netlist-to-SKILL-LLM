\# Netlist to SKILL Converter (Cadence Virtuoso)



This project converts SPICE netlists into Cadence SKILL scripts to automatically generate schematics.



\## Features

\- Supports MOS, R, C

\- Uses LLM (Gemini) for parsing

\- Generates Cadence-compatible SKILL code



\## Usage



```bash

python main.py input/sample.sp

```





Then in Cadence:



load("output/gen.il")



\## Requirements

\-Python 3.x

\-google-generativeai

\-python-dotenv

