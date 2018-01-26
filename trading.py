import csv
import math
import matplotlib.pyplot as plt
from signals import *
from indicators import *
from utilities import *

def execute_trades(signals, data, start_balance=100000):
    success = fail = entry_price = holding = 0
    balance = start_balance
    history = []
    total = []
    history.append(balance)
    # Initial values
    if signals[0] == 1:
        holding = int(balance / data[len(data) - len(signals)])
        balance = balance - data[len(data) - len(signals)] * holding
        entry_price = data[len(data) - len(signals)]
        history.append(balance)
    else:
        holding = -(balance / data[len(data) - len(signals)])
        entry_price = data[len(data) - len(signals)]
        history.append(balance)

    # Main trading
    for x in range(len(data) - len(signals) + 1, len(data)):
        volume = (balance / data[x])
        # Buying/Short Exit
        sign = signals[x - (len(data) - len(signals))]
        if sign == 1:
            if holding < 0:
                if entry_price > data[x]:
                    success = success + 1
                elif entry_price < data[x]:
                    fail = fail + 1
                balance = balance - ((entry_price - data[x]) * holding)
                volume = (balance / data[x])
                balance = balance - (data[x] * volume)
                holding = volume
                entry_price = data[x]
                history.append(balance)
            elif holding == 0:
                volume = (balance / data[x])
                balance = balance - (data[x] * volume)
                holding = volume
                entry_price = data[x]
                history.append(balance)
        elif sign == -1:
            if holding > 0:
                if entry_price < data[x]:
                    success = success + 1
                elif entry_price > data[x]:
                    fail = fail + 1
                balance = balance + (data[x]) * holding
                volume = (balance / data[x])
                holding = -volume
                entry_price = data[x]
                history.append(balance)
            elif holding == 0:
                volume = (balance / data[x])
                holding = -volume
                entry_price = data[x]
                history.append(balance)
        else:
            history.append(balance)
        if holding > 0:
            total.append(balance + holding * entry_price)
        elif holding <= 0:
            total.append(balance)
    if holding > 0:
        balance = balance + data[-1] * holding
    else:
        balance = balance + (entry_price - data[-1]) * holding
    history.append(balance)
    output = [history, success, fail, total]
    return output


def optimize_aroon(data):
    max_profit = ideal = 0
    for x in range(5, len(data)):
        aroon_signals = aroon_signal(data, x)
        if execute_trades(aroon_signals, data)[0][-1] > max_profit:
            ideal = x
            max_profit = execute_trades(aroon_signals, data)[0][-1]
    return ideal


def optimal_aroon_display(data, begin, difference):
    signals = []
    # Algorithm divides into four, optimizes, then gets the optimal within the quarter of the data given
    for x in range(begin + 1, len(data)):
        aroon_up = aroon(data[x - begin:x], optimize_aroon(data[x - begin:x]))[0]
        aroon_down = aroon(data[x - begin:x], optimize_aroon(data[x - begin:x]))[1]
        add = 0
        if aroon_up > difference * aroon_down:
            if (len(signals) > 0):
                if (signals[-1] == 1):
                    add = 0
                else:
                    add = 1
        elif aroon_down > difference * aroon_up:
            if (len(signals) > 0):
                if (signals[-1] == -1):
                    add = 0
                else:
                    add = -1
        signals.append(add)
    total_history = execute_trades(signals, data)
    print('Final Profit', total_history[0][-1])
    print('Successes', total_history[1])
    print('Failures', total_history[2])
    plt.plot(total_history[3])
    plt.ylabel(total_history[3])
    plt.show()
    return total_history[3]


def optimal_aroon(data, begin, difference):
    signals = []
    # Algorithm divides into four, optimizes, then gets the optimal within the quarter of the data given
    for x in range(begin + 1, len(data)):
        aroon_up = aroon(data[x - begin:x], optimize_aroon(data[x - begin:x]))[0]
        aroon_down = aroon(data[x - begin:x], optimize_aroon(data[x - begin:x]))[1]
        add = 0
        if aroon_up > difference * aroon_down:
            if (x > 52) & (signals[-1] == 1):
                add = 0
            else:
                add = 1
        elif aroon_down > difference * aroon_up:
            if (x > 52) & (signals[-1] == -1):
                add = 0
            else:
                add = -1
        signals.append(add)
    total_history = execute_trades(signals, data)
    plt.plot(total_history[3])
    plt.show()
    return total_history[0][-1]

