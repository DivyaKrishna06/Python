# Extended Function as argument syntax
def hyperVolume(*lengths):
    if len(lengths) < 2:
        raise ValueError("At least two arguments are required for hyperVolume calculation")
    
    v = lengths[0]
    for length in lengths[1:]:
        v *= length
    return v

print(hyperVolume(1, 2, 3, 4, 5))