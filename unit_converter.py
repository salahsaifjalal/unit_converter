import streamlit as st  # type: ignore

# Greetings! 👋
st.write("Hello! Let's convert some units! 🚀")

def length_conversion(value, from_unit, to_unit):     
    """Converts length units."""
    length_units = {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084, "inches": 39.3701}
    conversion_factor = length_units[to_unit] / length_units[from_unit]
    result = value * conversion_factor     
    # Display the formula
    return result, f"Formula: Value * ({length_units[to_unit]} / {length_units[from_unit]})"

def weight_conversion(value, from_unit, to_unit):
    """Converts weight units."""
    weight_units = {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462}
    conversion_factor = weight_units[to_unit] / weight_units[from_unit]
    result = value * conversion_factor
     # Display the formula
    return result, f"Formula: Value * ({weight_units[to_unit]} / {weight_units[from_unit]})"

def temperature_conversion(value, from_unit, to_unit):
    """Converts temperature units."""
    if from_unit == to_unit:
        return value, ""
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = value * 9/5 + 32
            # Display the formula
            return result, "Formula: Value * 9/5 + 32"
        else:
            result = value + 273.15
            # Display the formula
            return result, "Formula: Value + 273.15"
    if from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value - 32) * 5/9
            # Display the formula
            return result, "Formula: (Value - 32) * 5/9"
        else:
            result = (value - 32) * 5/9 + 273.15
            # Display the formula
            return result, "Formula: (Value - 32) * 5/9 + 273.15"
    if from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
            # Display the formula
            return result, "Formula: Value - 273.15"
        else:
            result = (value - 273.15) * 9/5 + 32
            # Display the formula
            return result, "Formula: (Value - 273.15) * 9/5 + 32"

def speed_conversion(value, from_unit, to_unit):
    """Converts speed units."""
    speed_units = {"m/s": 1, "km/h": 3.6, "mph": 2.23694}
    conversion_factor = speed_units[to_unit] / speed_units[from_unit]
    result = value * conversion_factor
    # Display the formula
    return result, f"Formula: Value * ({speed_units[to_unit]} / {speed_units[from_unit]})"

# Main Streamlit app
st.title("Unit Converter 📏 ⚖️ 🌡️ 🏎️")
category = st.selectbox("What do you want to convert ?",
                        ["Length", "Weight", "Temperature", "Speed"], index=None, placeholder="Select from here...")

value = st.number_input("Enter value", min_value=0.0, format="%.3f")

if category:
    if category == "Length":
        units = ["meters", "kilometers", "miles", "feet", "inches"]
        convert_function = length_conversion
    elif category == "Weight":
        units = ["grams", "kilograms", "pounds"]
        convert_function = weight_conversion
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        convert_function = temperature_conversion
    elif category == "Speed":
        units = ["m/s", "km/h", "mph"]
        convert_function = speed_conversion

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units)
    with col2:
        to_unit = st.selectbox("To", units)

    if st.button("Press me to convert!"):
        result, formula = convert_function(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.3f} {to_unit}")
        if formula:
            st.write(formula)
else:
    st.write("Please select a category to begin.")