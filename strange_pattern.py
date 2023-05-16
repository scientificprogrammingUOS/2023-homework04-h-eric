import numpy as np


def strange_pattern(dimensions):
    # initialise a numpy array full of zeros with the given tuple dimensions
    p = np.zeros(dimensions, dtype=bool)
    # every third diagonal is True
    p[::3,::3] = True
    p[1::3,2::3] = True
    p[2::3,1::3] = True

    return p


if __name__ == "__main__":
    # use this for your own testing!
    pattern = (7,7)
    print(strange_pattern(pattern))
