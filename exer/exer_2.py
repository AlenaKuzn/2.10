#!/usr/bin/env python3
# -*- coding: utf-8 -*

def sred_garmonik(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        a = 0
        for i in values:
            a = a + (1 / i)
        return n / a
    else:
        return None


if __name__ == "__main__":
    print(sred_garmonik())
    print(sred_garmonik(5, 7, 17, 22))
