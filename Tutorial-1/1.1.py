seconds = int(input("Enter time in seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"Time in HH:MM:SS format: {hours:02d}:{minutes:02d}:{remaining_seconds:02d}")
