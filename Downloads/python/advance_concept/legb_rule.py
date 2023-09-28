# Global variable
global_var = "I'm a global variable"

def enclosing_function():
    # Enclosing (non-local) variable
    enclosing_var = "I'm an enclosing variable"
    
    def local_function():
        # Local variable
        local_var = "I'm a local variable"
        
        # Access variables in the following order: Local -> Enclosing -> Global
        print("Inside local_function:")
        print("Local variable:", local_var)
        print("Enclosing variable:", enclosing_var)
        print("Global variable:", global_var)
    
    local_function()

# Access variables in the following order: Global -> Enclosing
print("Outside functions:")
print("Global variable:", global_var)

enclosing_function()