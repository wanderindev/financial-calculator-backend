def aggregate(_list, periods):
    return [round(sum(_list[:x]), 4) for x in periods]


def format_tables(calculator, ff, _type):
    ff = int(ff)

    if ff > 0 and _type is 'savings':
        return [dict(p='{:0,.0f}'.format(calculator.periods[x-1]),
                     d='{:0,.2f}'.format(sum(calculator.deposits[x-ff:x])),
                     i='{:0,.2f}'.format(sum(calculator.interests[x-ff:x])),
                     b='{:0,.2f}'.format(calculator.balances[x-1]))
                for x in calculator.periods if x % ff == 0]

    if ff > 0 and _type is 'loans':
        return [dict(p='{:0,.0f}'.format(calculator.periods[x-1]),
                     pe='{:0,.2f}'.format(sum(calculator.payments_e[x-ff:x])),
                     pr='{:0,.2f}'.format(
                         sum(calculator.payments_r[x - ff:x])),
                     pi='{:0,.2f}'.format(sum(calculator.interests[x-ff:x])),
                     pc='{:0,.2f}'.format(
                         calculator.loan -
                         sum(calculator.payments[x - ff:x]) +
                         sum(calculator.interests[x-ff:x])),
                     b='{:0,.2f}'.format(calculator.balances[x-1]))
                for x in calculator.periods if x % ff == 0]

    if ff > 0 and _type is 'retirements':
        return [dict(p='{:0,.0f}'.format(calculator.periods[x-1]),
                     d='{:0,.2f}'.format(sum(calculator.withdrawals[x-ff:x])),
                     i='{:0,.2f}'.format(sum(calculator.interests[x-ff:x])),
                     b='{:0,.2f}'.format(calculator.balances[x-1]))
                for x in calculator.periods if x % ff == 0]

    return None
