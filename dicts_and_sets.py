#!/usr/bin/env python
"""
Dict and set examples for KAPL class
"""
# builtin imports
# 3rd-party (CPAN) imports
# org imports
# project imports

def main():
    """
    Program entry point

    :return: None
    """
    # get cmd line options
    dict_examples()
    set_examples()

def dict_examples():
    """
    Examples of using dicts

    :return: None
    """
    d1 = {
        's2': [1, 4, 9, 8],
        's3': [5, 8, 1, 7]
    }

    print(d1['s2'])
    print(d1['s2'][2])
    d1['s4'] = [7, 6, 1, 9]
    print(d1)

    print(d1.keys())
    print(d1.values())
    print()

    for k, values in d1.items():
        print(k, values)
    print()
    print(d1['s2'])
    print(d1.get('s2'))
    print(d1.get('x5'))
    print(d1.get('x5', []))

    del d1['s4']

def set_examples():
    """
    Examples of using sets.

    :return:
    """


    cities1 = {'Albany', 'Colonie', 'Saratoga Springs',
            'Clifton Park'}

    cities2 = {'Clifton Park', 'Colonie', 'Latham',
            'Troy', 'Schenectady'}

    print("Both:", cities1 & cities2)
    print("Just one:", cities1 ^ cities2)
    print("All:", cities1 | cities2)
    print('Just cities1:', cities1 - cities2)
    print('Just cities2:', cities2 - cities1)

    names = ['John', 'John', 'Jacob', 'Jingleheimer',
             'Smith', 'Jacob']

    print(set(names))

if __name__ == '__main__': # if run as script
    main()

