# Simple export tool

## Tool was used to process bus stops data exported from pdf files

This code for each provided csv file in the *in* folder with bus stops data outputs a new csv file with structured data to the *out* folder.

Format of the output data:

* Line number
* Distance in KM from the first bus stop in line
* Bus stop name
* Time of the first departure in time table

## Setup

1. Install pandas in your virtual enviroment

```bash
pip install pandas
```

2. Put csv files to be processed in the *in* folder

3. Run *get_data_from_bus_lines.py* file and check the *out* folder for processed file
