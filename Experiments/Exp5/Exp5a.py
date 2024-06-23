from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date
print("Current date:", current_datetime.strftime("%Y-%m-%d"))

# Print the current time
print("Current time:", current_datetime.strftime("%H:%M:%S"))

# Print the current date and time
print("Current date and time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
