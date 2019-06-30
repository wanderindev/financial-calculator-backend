from math import ceil


def aggregate(_list, periods):
    return [round(sum(_list[:x]), 2) for x in periods]
