import numpy
import csv

def sharpe_ratio(data,rfr):
    hprs = HPRS(data)
    ahpr = AHPR(data)
    print('Sharpe Ratio', (ahpr -rfr) / numpy.std(hprs))

def HPRS(data):
    hprs = []
    price_changes = []
    for x in range(1, len(data)):
        if data[x] != data[x - 1]:
            price_changes.append(data[x])
    for x in range(1, len(price_changes)):
        hprs.append(price_changes[x] / price_changes[x - 1])
    return hprs

def AHPR(data):
    return numpy.mean(HPRS(data))

def CAR(data):
    hprs = HPRS(data)
    car = 1
    for x in hprs:
        car = car * x
    car = car ** (1 / len(hprs))
    return car

# Parse a csv and return
#   OHCL average array
#   Opening prices array
#   High prices array
#   Closing prices array
#   Low prices array
def parse_csv(csv):
    # To add soon
    return None