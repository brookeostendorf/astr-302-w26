#!/usr/bin/env python

#Function that creates a new file and writes strings from an array into said file#

def write_inp_file(contents):
    last_item = contents[-1] 
    file_name_val = last_item.split('=')[-1].strip().replace("'", "").replace('"', "")
    
    with open(f"{file_name_val}.inp", "w", encoding="utf-8") as f:
        f.writelines('\n'.join(contents))
        
    return