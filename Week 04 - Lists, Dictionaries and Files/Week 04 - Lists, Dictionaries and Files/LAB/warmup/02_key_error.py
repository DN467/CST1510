# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

try:
    print(record["limit"])
except KeyError:
    print("Key not found.")
