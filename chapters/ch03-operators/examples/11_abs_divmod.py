# file: examples/11_abs_divmod.py
temperature_change = -7.5
print(abs(temperature_change))           # sign hata deta hai

minutes = 135
hours, mins = divmod(minutes, 60)        # (//, %) aik saath
print(f"{minutes} minutes = {hours} ghante {mins} minute")
print(divmod(17, 5))
