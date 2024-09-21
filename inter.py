import hashlib
import streamlit as st

# Function to calculate the hash (SHA-256) of a file
def calculate_hash(file):
    file_hash = hashlib.sha256(file.read()).hexdigest()  # Calculate the SHA-256 hash
    return file_hash

# Streamlit App Interface
st.title("Simple File Integrity Checker")

# File upload
file1 = st.file_uploader("Upload the first file")
file2 = st.file_uploader("Upload the second file")

if file1 and file2:
    # Reset file pointer to start before reading again
    file1.seek(0)
    file2.seek(0)

    # Calculate hashes
    hash1 = calculate_hash(file1)
    hash2 = calculate_hash(file2)

    # Display hash values
    st.write(f"Hash of File 1: {hash1}")
    st.write(f"Hash of File 2: {hash2}")

    # Compare hashes
    if hash1 == hash2:
        st.success("Files are identical!")
    else:
        st.error("Files are different!")
else:
    st.info("Please upload two files to compare.")
