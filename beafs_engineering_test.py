"""
Test file for BEAFS engineering bundle.
"""

import beafs_engineering

__name__ = "__main__"


def class_vector_test():
    v1 = beafs_engineering.Vector(x=3, y=4)

    if abs(v1.magnitude() - 5) < 0.001:
        print("PASS - magnitude method for Vector class in 2D")
    else:
        print("FAIL - magnitude method for Vector class in 2D")


def main():
    print("-----BEAFS Engineering Bundle test-----")
    class_vector_test()

if __name__ == "__main__":
    main()
