import os
import sys
import xml.etree.ElementTree as ET

from herd import Herd


def custom_dict_sort(dictin):
    try:
        return {'name': dictin['name'], 'age': dictin['age']}
    except KeyError:
        return None


def organize_data_yaks(root_xml):
    yaks_list = []
    for child in root_xml:
        if child.tag == 'labyak' and isinstance(child.attrib, dict):
            sorted_yak = custom_dict_sort(child.attrib)
            if sorted_yak:
                yaks_list.append(sorted_yak)

    return yaks_list


def run(days):

    file_input = 'load.xml'
    if os.path.isfile(file_input):
        file_in = file_input #'herd.xml'
    else:
        print('File not found! Try again')
        sys.exit(1)

    root = ET.parse(file_in).getroot()
    yaks_list = organize_data_yaks(root)

    herd = Herd(yaks_list)
    data = herd.get_stock(days)
    return data


def get_stock_info(days):
    data = run(days)
    return {'milk': data['milk'], 'skins': data['skins']}


def get_herd_info(days):
    data = run(days)
    return {'herd': data['herd']}
