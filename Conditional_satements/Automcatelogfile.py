log_file=[
    "INFO: operation successfull",
    "ERROR: file not found",
    "DEBUG: connection established",
    "ERROR: database connection failed",
]
for line in log_file:
    if "DEBUG" in line:
      print(line)