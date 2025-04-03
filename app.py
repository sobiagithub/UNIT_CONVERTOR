
import streamlit as st
#functionality
def distance_convertor(from_unit,to_unit,value):
    units ={
        "Meters":1,
        "Kilometers":1000,
        "Feet":0.3048,
        "Miles":1609.34
    }
    result =value * units[from_unit] / units[to_unit]
    return result

def temperature_convertor(from_unit,to_unit,value):
    if from_unit == "Celcius" and to_unit == "Fahrenheit":
        result =(value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == to_unit =="Celcius":
        result = (value - 32) * 5/9
    else:
        result = value
    return result  

def weight_convertor(from_unit,to_unit,value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "pounds": 0.453592,
        "Ounces": 0.0283495
    }  
    result = value * units[from_unit] / units[to_unit]  
    return result     

def Pressure_convertor(from_unit,to_unit,value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }  
    result = value * units[from_unit] / units[to_unit]  
    return result

#ui
st.title("Unit Converter")
categury = st.selectbox("select categury",["Distance","Temperature","Weight","Pressure"])

if categury == "Distance":
    from_unit = st.selectbox("From",["Meters","Kilometers","Feet","Miles"])
    to_unit = st.selectbox("To",["Meters","Kilometers","Feet","Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result =  distance_convertor(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif categury == "Temperature":
    from_unit = st.selectbox("From",["Celcius","Fahrenheit"])
    to_unit = st.selectbox("To",["Celcius","Fahrenheit"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result = temperature_convertor(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif categury == "Weight":
    from_unit = st.selectbox("From",["Kilograms","Grams","Pounds","Ounces"])
    to_unit = st.selectbox("To",["Kilograms","Grams","Pounds","Ounces"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result =weight_convertor(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")       

elif categury == "Pressure":
    from_unit = st.selectbox("From",["Pascals","Hectopascals","Kilopascals","Bar"])
    to_unit = st.selectbox("To",["Pascals","Hectopascals","Kilopascals","Bar"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result =Pressure_convertor(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")


