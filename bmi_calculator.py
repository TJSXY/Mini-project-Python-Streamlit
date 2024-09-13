import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    st.title("BMI Calculator")
    
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Enter your height (m)", min_value=0.1, max_value=3.0, value=1.7)
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 25:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")

if __name__ == "__main__":
    main()