# Temperature Converter

# Ask for temperature in Celsius.

# Convert to Fahrenheit.

# Show both with string formatting.

temperature = float(input("what's the temperature? : "))
converted_to_fahrenheit = (temperature * 1.8) + 32

print(
    f"""== the temp in celcuis: {temperature} 
== the temp in fahrenheit : {converted_to_fahrenheit}"""
)
