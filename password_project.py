import streamlit as st 
import string
import random
import os
import time
# Character groups
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)

# Usage limit
max_uses = 3
if os.path.exists("mohamed.txt"):
    with open("mohamed.txt", "r") as file:
        content = file.read().strip()
        if content.isdigit():
            uses = int(content)
        else:
            uses = 0
else:
    uses = 0

st.title("🔐 Password Generator")

if uses >= max_uses:
    st.error("Access denied. You have already used this generator 3 times.")
else:
    total_length = st.number_input("How many characters should the password have?", min_value=1, step=1)

    if total_length:
        num_lower = st.number_input("How many lowercase letters?", min_value=0, max_value=total_length, step=1)
        num_upper = st.number_input("How many uppercase letters?", min_value=0, max_value=total_length, step=1)
        num_digits = st.number_input("How many digits?", min_value=0, max_value=total_length, step=1)
        num_punct = st.number_input("How many punctuation characters?", min_value=0, max_value=total_length, step=1)

        if num_lower + num_upper + num_digits + num_punct == total_length:
            if st.button("Generate Password"):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                
                random.shuffle(lowercase)
                random.shuffle(uppercase)
                random.shuffle(digits)
                random.shuffle(punctuation)

                password = []
                password += lowercase[:num_lower]
                password += uppercase[:num_upper]
                password += digits[:num_digits]
                password += punctuation[:num_punct]

                random.shuffle(password)
                final_password = ''.join(password)

                uses += 1
                with open("mohamed.txt", "w") as file:
                    file.write(str(uses))

                st.success(f"✅ Generated Password: `{final_password}`")
                st.info(f"{max_uses - uses} uses remaining.")
        else:
            st.warning(f"Total doesn't match {total_length}. Adjust the numbers.")

