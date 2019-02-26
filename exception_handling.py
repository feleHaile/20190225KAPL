#!/usr/bin/env python

try:
    with open('SPAM/wombat_pizza.txt') as wp_in:
        pass

    print("HI MOM!")

except FileNotFoundError as err:
    print(err)

print("All done.")


for value in 5, 8, 19, 0, 55, 4:
    try:
        result = 25 / value
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print("WHOA!", err)
    else:
        print("result is", result)
    finally:
        print("OK")
