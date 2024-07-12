import streamlit as st
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.write('Hello, *World!* :sunglasses:')
number = st.number_input("Insert a number")
st.write("The current number is ", number)


def is_even(n):
    return n % 2 == 0

# Fungsi untuk mengalikan dua bilangan dan memeriksa apakah hasilnya genap atau ganjil
def multiply_and_check(num1, num2):
    result = num1 * num2
    if is_even(result):
        return result, "Genap"
    else:
        return result, "Ganjil"

# Meminta input angka dari pengguna
number1 = st.number_input("Insert the first number", step=1)
number2 = st.number_input("Insert the second number", step=1)

# Mengalikan dua bilangan dan memeriksa hasilnya
if number1 and number2:
    result, odd_or_even = multiply_and_check(number1, number2)
    st.write(f"Hasil perkalian: {result}")
    st.write(f"Bilangan tersebut adalah bilangan {odd_or_even}")