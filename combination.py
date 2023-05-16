import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a1, a2, axis=0):
    
    # return combined arrays
    return np.concatenate((a1, a2), axis=axis)


if __name__ == "__main__":
    # use this for your own testing!
    a1 = np.array([[1, 2],[3, 4]])
    a2 = np.ones((2,2,2))
    print(combination(a1, a2, axis=0))
    pass
