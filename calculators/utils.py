def aggregate(_list, periods):
    return [round(sum(_list[:x]), 2) for x in periods]


def format_tables(calculator, ff):
    ff = int(ff)

    if ff > 0:
        return [dict(p='{:0,.0f}'.format(calculator.periods[x-1]),
                     d='{:0,.2f}'.format(sum(calculator.deposits[x-ff:x])),
                     i='{:0,.2f}'.format(sum(calculator.interests[x-ff:x])),
                     b='{:0,.2f}'.format(calculator.balances[x-1]))
                for x in calculator.periods if x % ff == 0]

    return None
