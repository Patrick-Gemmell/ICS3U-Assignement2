#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This program shows how global and local variables work

import math


def main():
    # this function adds two integers together

    major_radius = float(input("Enter the Major Radius (cm) "))
    minor_radius = float(input("Enter the Minor Radius (cm)"))

    volume = (math.pi*minor_radius**2)*(2*math.pi*major_radius)

    print("The volume is {:,.2f}cm^3".format(volume))


if __name__ == "__main__":
    main()
