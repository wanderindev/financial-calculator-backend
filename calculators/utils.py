from math import ceil


def fut_val(_rate, nper, pv):
    return -pv * pow((1 + _rate), nper)


def payment(_rate, nper, pv, fv=0, t=0):
    q = pow(1 + _rate, nper)

    return - (_rate * (fv + (q * pv))) / ((-1 + q) * (1 + _rate * t))


def pres_val(_rate, nper, fv):
    return -fv / pow((1 + _rate), nper)


def rate(nper, pmt, pv, fv=0, t=0, guess=0.1):
    low = 0
    high = 1
    tolerance = abs(0.00000005 * pmt) or 0.001

    # Try to find a solution in 60 iterations.
    for i in range(60):
        # Reset the balance to the original pv.
        balance = pv

        # Calculate the final balance, based on loan conditions.
        for j in range(ceil(nper)):
            if not t:
                # Apply interests before payment
                balance = balance * (1 + guess) + pmt
            else:
                # Apply payment before interests
                balance = (balance + pmt) * (1 + guess)

        # Return success and guess if balance is within tolerance.
        if abs(balance + fv) < tolerance:
            return True, guess
        elif balance + fv > 0:
            # Adjust high, since guess was too big.
            high = guess
        else:
            # Adjust low, since guess was too small.
            low = guess

        # Calculate a new guess.
        guess = (high + low) / 2

    # Return success False, rate None, since no acceptable result was found.
    return False, None
