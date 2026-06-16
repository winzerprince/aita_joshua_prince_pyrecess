# Difference between global and local vairable

global_variable = "GLOBAL"

for i in range(1, 6):
    local_variable = "LOCAL"
    print(local_variable)

print(global_variable)
print(local_variable)  # This is possibly unbound but still accessible
