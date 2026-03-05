#Time Converter
time=int(input("Enter Time in secons: "))
hour=time//3600
rem_sec=time%3600
min=rem_sec//60
sec=rem_sec%60
print(f"Time will be {hour} hours, {min} Minutes and {sec} Seconds")