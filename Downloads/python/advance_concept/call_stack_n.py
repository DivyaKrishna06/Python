def recursive_function(n):
    if n == 0:
        print(f"Base case reached with n = {n}")
        return 0
    else:
        print(f"Entering function with n = {n}")
        result = n + recursive_function(n - 1)
        print(f"Exiting function with n = {n}")
        return result

n = 4
print(f"Starting simulation with n = {n}")
result = recursive_function(n)
print(f"Simulation complete. Result = {result}")