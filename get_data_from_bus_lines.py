from os import listdir, makedirs, path
import re

import pandas as pd


files = [f for f in listdir('in')]
ABS_OUT = path.abspath('out/')
if not path.exists(ABS_OUT):
    makedirs(ABS_OUT)
errors = []
for file in files:
    try:
        PATH = 'in/' + file
        OUT_PATH = ABS_OUT + '/' +  file
        line_number = re.search('(\d+)',file)
        if line_number:
            line_number = line_number.group(1)
        
        df = pd.read_csv(PATH, sep=';')
        stop = df.iloc[:,0].dropna().drop_duplicates()

        stop_km = []
        stop_names = []
        line_numbers = []

        for line in stop:
                km = re.search('\d+\.\d+',line)
                if km:
                    stop_km.append(km.group(0))
                stop_name = re.search('\d+\.\d+\s*(?:[A-Z]*\s)(.*)',line)
                if stop_name:
                    stop_names.append(stop_name.group(1).strip())
                    line_numbers.append(line_number)
        line_times = df.iloc[0:len(stop_names),3]
        data = {'line_number': line_numbers, 'km': stop_km, 'name': stop_names, 'time': line_times}
        data = pd.DataFrame(data)
        data.to_csv(path_or_buf=OUT_PATH, sep=';', index=False)
    except Exception:
        errors.append(file)

print(f'Files with errors: {errors}')
