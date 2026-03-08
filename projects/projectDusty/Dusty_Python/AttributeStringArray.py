#!/usr/bin/env python

#Function that reads the atrributes of an object, converts the values of defined attributes into properly formatted text strings, and puts the strings in an array#

def inspect_attributes(obj):
    instance_data = vars(obj)
    content = []
    for name, value in instance_data.items():
        if not name.startswith('_') and not name.startswith('gt_') and value is not None and (not isinstance(value, list) or len(value) > 0):
            if name.startswith("file"):
                if isinstance(value, list):
                    for item in value:
                        content.append(f"{item}")
                else: content.append(f"{value}")
                continue
            if isinstance(value, list):
                list_str = ", ".join(str(item) for item in value)
                content.append(f"{name}= {list_str}")

            else: content.append(f"{name}= {value}")
    return content