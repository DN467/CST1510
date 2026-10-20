# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ['M0123','M0124','M0125']

try:
    result = labels[2]
except IndexError: 
    print('IndexError: list index out of range')
else:
    print(result)

