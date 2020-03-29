def aggregate(_list, periods):
    return [round(sum(_list[:x]), 4) for x in periods]


def format_tables(calculator, ff, _type):
    ff = int(ff)

    if ff > 0 and _type is "cc":
        return [
            dict(
                p="{:0,.0f}".format(x / ff),
                pt="{:0,.2f}".format(sum(calculator.payments[x - ff : x])),
                pp="{:0,.2f}".format(sum(calculator.payments_p[x - ff : x])),
                pi="{:0,.2f}".format(sum(calculator.interests[x - ff : x])),
                b="{:0,.2f}".format(calculator.balances[x - 1]),
            )
            for x in calculator.periods
            if x % ff == 0
        ]

    if ff > 0 and _type is "savings":
        return [
            dict(
                p="{:0,.0f}".format(x / ff),
                d="{:0,.2f}".format(sum(calculator.deposits[x - ff : x])),
                i="{:0,.2f}".format(sum(calculator.interests[x - ff : x])),
                b="{:0,.2f}".format(calculator.balances[x - 1]),
            )
            for x in calculator.periods
            if x % ff == 0
        ]

    if ff > 0 and _type is "loans":
        return [
            dict(
                p="{:0,.0f}".format(x / ff),
                pe="{:0,.2f}".format(sum(calculator.payments_e[x - ff : x])),
                pr="{:0,.2f}".format(sum(calculator.payments_r[x - ff : x])),
                pi="{:0,.2f}".format(sum(calculator.interests[x - ff : x])),
                pc="{:0,.2f}".format(
                    calculator.payments_e[x - 1]
                    + calculator.payments_r[x - 1]
                    - calculator.interests[x - 1]
                ),
                b="{:0,.2f}".format(calculator.balances[x - 1]),
            )
            for x in calculator.periods
            if x % ff == 0
        ]

    if ff > 0 and _type is "retirements":
        return [
            dict(
                p="{:0,.0f}".format(x / ff),
                w="{:0,.2f}".format(sum(calculator.withdrawals[x - ff : x])),
                i="{:0,.2f}".format(sum(calculator.interests[x - ff : x])),
                b="{:0,.2f}".format(calculator.balances[x - 1]),
            )
            for x in calculator.periods
            if x % ff == 0
        ]

    return None
