from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
# Latihan konfersi satuan temperatur

# Program konversi Celcius ke satuan lain
print("\nProgram Celsius ke satuan lain\n")

celcius = float(input("Masukkan suhu dalam Celcius: "))
print(f"Suhu adalah: {celcius}", "Celsius")

# Reamur
reamur = (4/5)*celcius
print(f"Suhu dalam reamur: {reamur} Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print(f"Suhu dalam Fahrenheit: {fahrenheit} Fahrenheit")

# Kelvin
kelvin = celcius + 273
print(f"Suhu dalam Kelvin: {kelvin} Kelvin")

# Program konversi Reamur ke satuan lain
print("\nProgram Reamur ke satuan lain\n")

reamur = float(input("Masukkan suhu dalam Reamur: "))

# Celcius
celcius = (5/4) * reamur
print(f"Suhu dalam Celcius: {celcius} Celcius")

# Fahrenheit
fahrenheit = ((9/4) * reamur) - 32
print(f"Suhu dalam Fahrenheit: {fahrenheit} Fahreheit")

# Kelvin
kelvin = ((5 / 4) * reamur) + 273
print(f"Suhu dalam Kelvin: {kelvin} Kelvin")

# Program konversi Fahrenheit ke satuan lain

print("\nProgram Fahrenheit ke satuan lain")

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Celcius
celcius = 5/9 * (fahrenheit - 32)
print(f"Suhu dalam Celcius: {celcius} Celcius")

# Reamur
reamur = ((4/9) * (fahrenheit) - 32)
print(f"Suhu dalam Reamur: {reamur} Reamur")

# Kelvin 
kelvin = 5/4 * reamur + 273
print(f"Suhu dalam Kelvin: {kelvin} Kelvin")

# Program konversi Kelvin ke satuan lain
print("\nProgram Kelvin ke satuan lain")

kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Celcius
celcius = kelvin - 273
print(f"Suhu dalam Celcius: {celcius} Celcius")

# Reamur
reamur = 4/5 * (kelvin - 273)
print(f"Suhu dalam Reamur: {reamur} Reamur")

# Fahrenheit
fahrenheit = ((kelvin) - 273.15) * 9/5 + 32
print(f"Suhu dalam Fahrenheit: {fahrenheit} Fahrenheit")