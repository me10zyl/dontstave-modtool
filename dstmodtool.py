import re
import os
dir_path = "e:\\test\\mods\\"

false = 0
true = 1
dirs = os.listdir(dir_path)
mod_infos = []
for dir in dirs:
    dir_abs = os.path.join(dir_path, dir)
    if os.path.isdir(dir_abs):
        mod_info = os.path.join(dir_abs, 'modinfo.lua');
        if os.path.exists(mod_info):
            mod_infos.append(mod_info)
for file_path in mod_infos:
    try:
        f = open(file_path, 'r')
        bracket = 0
        for line in f.readlines():
            trip = line.strip()
            has_bracket = false
            if '{' in trip:
                bracket += 1
                has_bracket = true
            if '}' in trip:
                bracket -= 1
            if bracket > 0:
                trip = trip.replace('=', ':')
            trip = trip.replace('"', '\'').replace('..','\\')
            pattern = re.compile(r'name\s*=\s*\'?(\w|\s)+\'?')
            #if pattern.match(trip) or (has_bracket and bracket == 0):
                #exec trip
            if pattern.match(trip):
                print os.path.dirname(file_path) + trip.split('=')[1].replace('\'','')
    finally:
        if f:
            f.close()