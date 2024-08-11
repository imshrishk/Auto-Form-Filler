import pandas as pd
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title='Select a CSV File',
        filetypes=(('CSV files', '*.csv'), ('All files', '*.*'))
    )
    return file_path

# Read CSV
def read_csv_and_extract_urls(csv_file_path):
    data = pd.read_csv(csv_file_path)
    # For column 'E'; Change the value '4' if you want to use other column
    urls = data.iloc[:, 4].tolist()
    return urls

# Selenium for automation
def automate_form_submission(urls):
    # Initialize WebDriver (make sure to have the chromedriver executable in your PATH)
    driver = webdriver.Chrome()

    # Write the name, email, message you want to fill in the form
    contact_name = 'Your Name'
    contact_email = 'your_email@example.com'
    contact_message = 'This is a test message.'

    for url in urls:
        driver.get(url)
        
        try:
            # To locate
            name_field = driver.find_element(By.CSS_SELECTOR, 'input[name="name"], input[type="text"]')
            email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="email"], input[type="email"]')
            message_field = driver.find_element(By.CSS_SELECTOR, 'textarea[name="message"], textarea')
            
            name_field.send_keys(contact_name)
            email_field.send_keys(contact_email)
            message_field.send_keys(contact_message)
            
            # For click button
            submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"]')
            submit_button.click()
            
            # Check if the form is submitted
            time.sleep(5)
        except Exception as e:
            print(f"Error occurred at {url}: {e}")
    
    # Close WebDriver
    driver.quit()

if __name__ == "__main__":
    # CSV file path
    csv_file = select_file()
    
    if csv_file:
        # Extract URLs
        urls = read_csv_and_extract_urls(csv_file)
        
        # Automate
        automate_form_submission(urls)
    else:
        print("No file selected.")
