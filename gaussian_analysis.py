import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # Raise an error if the lower bound is greater than the upper bound
    if lower_bound > upper_bound:
        raise ValueError("Lower bound cannot be greater than upper bound")
    
    # Raise an error if the scale is less than or equal to zero
    if scale <= 0:
        raise ValueError("Scale must be greater than zero")
    
    # Raise an error if the loc is not within the bounds
    if loc < lower_bound or loc > upper_bound:
        raise ValueError("Loc must be within the bounds")
    
    # Raise an error if the bounds, loc and scale are not integers or floats
    if not isinstance(loc, (int, float)) or not isinstance(scale, (int, float)) or not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
        raise TypeError("Loc, scale, lower_bound and upper_bound must be integers or floats")
    
    # Create a normal distribution with the given loc and scale
    normal_dist = np.random.normal(loc, scale, 100)

    # Create a mask for the values that are within the bounds
    mask = (normal_dist >= lower_bound) & (normal_dist <= upper_bound)

    # Calculate the mean and standard deviation of the values within the bounds
    mean = np.mean(normal_dist[mask])
    std = np.std(normal_dist[mask])

    return (mean, std)


if __name__ == "__main__":
    # use this for your own testing!

    pass
