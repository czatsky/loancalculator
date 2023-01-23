import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type",choices=["annuity", "diff"],help='Incorrect parameters')
parser.add_argument("--payment",type=float)
parser.add_argument("--principal",type=float)
parser.add_argument("--periods",type=int)
parser.add_argument("--interest",type=float,help='Incorrect parameters')
args = parser.parse_args()

if args.type is None:
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment is not None:
    print("Incorrect parameters")
elif args.interest is None:
    print('Incorrect parameters')
elif args.payment is None and args.principal is None and args.periods is None:
    print('Incorrect parameters')
elif args.payment is None and args.principal is not None and args.periods is None:
    print('Incorrect parameters')
elif args.payment is None and args.principal is None and args.periods is not None:
    print('Incorrect parameters')
elif args.payment is not None and args.principal is None and args.periods is None:
    print('Incorrect parameters')
elif args.payment is not None and args.payment < 0:
    print('Incorrect parameters')
elif args.principal is not None and args.principal < 0:
    print('Incorrect parameters')
elif args.periods is not None and args.periods < 0:
    print('Incorrect parameters')
elif args.interest is not None and args.interest < 0:
    print('Incorrect parameters')

if args.type == 'diff' and args.principal is not None and args.periods is not None and args.interest is not None:
    n = args.periods
    i = args.interest / (12 * 100)
    P = args.principal
    s = []
    for m in range(n):
        m += 1
        D = ((P/n)+(i*(P-((P*(m-1))/n))))
        D = math.ceil(D)
        s.append(D)
        print(f'Month {m}: payment is {D}')
    print('Overpayment =',math.ceil(sum(s)-P))
if args.type == 'annuity' and args.payment is not None and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    A = args.payment
    n = args.periods
    P = math.floor(A / ((i * (math.pow(1 + i, n))) / ((math.pow(1 + i, n) - 1))))
    print(f'Your loan principal = {P}!')
    print('Overpayment =', math.ceil(n*A - P))
if args.type == 'annuity' and args.principal is not None and args.payment is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    P = args.principal
    A = args.payment
    a = i + 1
    b = (A / (A - i * P))
    n = math.log(b, a)
    yrs = math.floor(n / 12)
    mth = math.ceil(n % 12)
    if n % 12 != 0 and 1 < mth < 12:
        print(f'It will take {yrs} years and {mth} months to repay this loan!')
        print('Overpayment =', math.ceil(n)*A-P)
    if yrs == 1 and mth == 12:
        print()
        print(f'It will take {yrs+1} years to repay this loan!')
        print('Overpayment =',math.ceil(n)*A-P)
    if n < 12:
        print(f'It will take {mth} months to repay this loan!')
        print('Overpayment =', math.ceil(n)*A-P)
if args.type == 'annuity' and args.principal is not None and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)
    P = args.principal
    n = args.periods
    A = math.ceil(P * ((i * (math.pow((1 + i), n))) / (math.pow(1 + i, n) - 1)))
    print(f'Your annuity payment = {A}!')
    print('Overpayment =', math.ceil(n * A - P))
