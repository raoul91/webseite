def factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def outputText(text):
    # add some comment here...
    if representsInt(text):
        N = int( text )
        upper = 50
        if N < 0:
            result = 'Du hast eine negative Zahl eingegeben...'
        elif N > upper:
            result = 'Diese Zahl ist zu gross. Gib eine Zahl kleiner als {0} ein.'.format(upper)
        else:
            result = '{0}! = {1}'.format(N, factorial(N))
    else:
        result = 'Gib eine natürliche Zahl ein!!!'

    return result
