```markdown
# 📄 Auto-Form-Filler

**Auto-Form-Filler** is a Python-based automation tool designed to read URLs from a CSV file and automatically submit forms on those web pages using Selenium WebDriver. This tool is particularly useful for testing purposes or performing bulk form submissions across multiple websites.

## 🌟 Features

- **CSV File Input:** Effortlessly select a CSV file containing the URLs of the web pages with forms.
- **Automated Form Submission:** Automatically fill out and submit forms on the specified web pages.
- **Customizable Form Fields:** Easily customize the form fields such as name, email, and message.
- **Error Handling:** Logs any errors encountered during form submission, along with the URL where the error occurred.

## 🛠️ Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**
- `pandas` library
- `tkinter` library (included with most Python installations)
- `selenium` library
- **Chrome WebDriver** (Ensure the executable is in your PATH)

To install the necessary Python libraries, run:

```bash
pip install pandas selenium
```

## 🚀 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/quarkum-0/Auto-Form-Filler.git
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
- **GitHub:** [quarkum-0](https://github.com/quarkum-0)
```