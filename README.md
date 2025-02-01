# 📄 Auto-Form-Filler

**Auto-Form-Filler** is a Python tool designed to automate the submission of forms on multiple web pages by reading URLs from a CSV file and using Selenium WebDriver. It's perfect for testing or performing bulk form submissions across various websites.

## 🌟 Features

- **CSV File Input:** Easily select a CSV file that contains URLs of web pages with forms.
- **Automated Form Submission:** The tool automatically fills out and submits forms on the specified web pages.
- **Customizable Form Fields:** You can personalize the form fields, such as name, email, and message.
- **Robust Error Handling:** Any errors encountered during form submission are logged, along with the URL where the error occurred.

## 🛠️ Prerequisites

Before running the script, make sure you have the following:

- **Python 3.x**
- The `pandas` library
- The `tkinter` library (typically included with Python)
- The `selenium` library
- **Chrome WebDriver** (Ensure the executable is in your system PATH)

To install the necessary Python libraries, run the following command in your terminal:

```bash
pip install pandas selenium
```

## 🚀 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/imshrishk/Auto-Form-Filler.git
   cd Auto-Form-Filler
   ```

2. **Download and Install Chrome WebDriver:**

   Download the appropriate version of Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your PATH.

## 📝 Usage

1. **Run the Script:**

   Execute the `main.py` script:

   ```bash
   python main.py
   ```

2. **Select the CSV File:**

   A file dialog will appear prompting you to select a CSV file. The script will extract URLs from the specified column in the CSV file.

3. **Automated Form Submission:**

   The script will open each URL, fill out the form with the pre-defined values, and submit it.

## 🔧 Customization

- **Custom Form Fields:** 
  - Modify the `contact_name`, `contact_email`, and `contact_message` variables in the `automate_form_submission` function to use your desired values.
  
- **CSS Selectors:** 
  - If the form fields on the target websites have different attributes, adjust the `By.CSS_SELECTOR` in the script to match the correct CSS selectors.

## ⚠️ Error Handling

- If the script encounters an error while processing a URL, it will log the error in the console along with the URL where the error occurred.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving this tool, feel free to fork the repository and submit a pull request.

## 📬 Contact

For any inquiries or issues, you can reach out via:

- **Email:** [shrishk.work@gmail.com](mailto:shrishk.work@gmail.com)
- **GitHub:** [imshrishk](https://github.com/imshrishk)
