---

# Simple File Integrity Checker using Streamlit

This project is a lightweight web application that helps users verify the integrity of files by comparing their hash values (SHA-256). It allows users to upload two files and checks if they are identical, ensuring that no unauthorized changes or corruption have occurred.

## Features

- **File Upload**: Easily upload two files of any type through the web interface.
- **Hash Comparison**: Calculates the SHA-256 hash of both files and compares them to ensure they are identical.
- **Real-Time Feedback**: Displays whether the files are the same or different based on the comparison.
- **Streamlit Powered**: The app uses Streamlit for a clean and simple user interface that runs in the browser.

## How It Works

1. **Upload Two Files**: Select and upload any two files you want to compare.
2. **Hash Calculation**: The app computes the SHA-256 hash of each file.
3. **File Comparison**: The app displays the hash values of both files and informs you whether they are identical or different.

## Installation and Running

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/simple-file-integrity-checker.git
    cd simple-file-integrity-checker
    ```

2. Install the required dependencies:

    ```bash
    pip install streamlit
    ```

3. Run the application:

    ```bash
    streamlit run simple_integrity_checker.py
    ```

4. Open the web app in your browser and start comparing files.


## Requirements

- Python 3.x
- Streamlit

## Future Improvements

- Support for additional hash algorithms (e.g., MD5, SHA-1).
- Option to compare files by size or content.
- Enhanced UI/UX with more detailed file metadata.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
