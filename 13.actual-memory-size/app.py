'''
The Actual Memory Size of Your USB Flash Drive
Create a function that takes the memory size (ms) as an argument and returns the actual memory size.

Examples
actualMemorySize("32GB")
output = "29.76GB"

actualMemorySize("2GB")
output = "1.86GB"

actualMemorySize("512MB")
output = "476MB"
Notes
The actual storage loss on a USB device is 7% of the overall memory size!

If the actual memory size was greater than 1 GB, round your result to two decimal places.

If the memory size after adjustment is smaller then 1 GB, return the result in MB.

For the purposes of this challenge, there are 1000 MB in a Gigabyte.
'''
def actualMemorySize(s):
    unit="MB"
    real_size=float(s[:-2])
    if s[-2:]=="GB":
        real_size= real_size * (1 - 0.07)*1000
        if real_size>=1000:
            return str(round(real_size/1000,2)) + "GB"
        return str(round(real_size)) + "MB"
    elif s[-2:]=="MB":
        return str(round(real_size - 0.07* real_size)) + "MB"
    else:
        return "Input not in correct format"

print(actualMemorySize("32GB")) #29.75GB
print(actualMemorySize("2GB")) #1.86GB
print(actualMemorySize("512MB")) #476MB
print(actualMemorySize("1GB")) #930MB