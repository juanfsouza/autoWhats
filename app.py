from asyncio import wait
import time
from random import uniform
import pyautogui
import pyperclip
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def usleep(a, b):
    """Sleep for a random amount of time between a and b seconds."""
    time.sleep(uniform(a, b))

if __name__ == "__main__":
    while True:  # Start an infinite loop
        chrome_opt = uc.ChromeOptions()
        options = uc.ChromeOptions()

        try:
            # Clear the log file
            with open("app_log.txt", "w") as log_file:
                log_file.write("")

            # Initialize the Chrome browser
            driver = uc.Chrome(options=chrome_opt)
            print('\nIniciando Bot\n')

            driver.get('https://web.whatsapp.com/')
            usleep(20, 20)

            pyautogui.hotkey('f10')
            pyautogui.hotkey('f10')

            while True:
                try:
                    # Check for unread message element
                    unread_message_element = driver.find_element(By.XPATH, "//span[contains(@class, 'x1rg5ohu') and @aria-label='1 mensagem não lida']")
                    print("Elemento de mensagem não lida encontrado!")
                    usleep(3, 5)
                    unread_message_element.click()  # Click the unread message element
                    break  # Exit the inner loop after clicking the element
                except NoSuchElementException:
                    print("Elemento de mensagem não lida não encontrado, aguardando 30 segundos...")
                    usleep(30, 30)
                    continue  # Continue checking after 30 seconds

            # Read the content of the first message file and copy it to the clipboard
            with open(r'C:\Users\juan\Desktop\AutoWhats\msg\primeiro.txt', 'r', encoding='utf-8') as file:
                message = file.read()
            pyperclip.copy(message)
            print("Mensagem enviada!")

            # Paste the content in the message input field
            pyautogui.hotkey('ctrl', 'v')
            usleep(3, 5)

            pyautogui.hotkey('enter')

            # Wait for the last message element to appear
            time.sleep(10)  # Wait for 10 seconds to allow the last message to appear

            # Find the last message element and check its content
            for i in range(3):  # Check for 3 rounds (1:30 seconds total)
                try:
                    last_message_element = driver.find_element(By.XPATH, "(//div[@class='_amjv _aotl']//span[contains(@class, 'selectable-text')])[last()]")
                    span_text = last_message_element.find_element(By.TAG_NAME, 'span').text
                    print(f"Texto dentro do último <span>: {span_text}")

                    usleep(3, 5)

                    # Check if the last message contains "1", "2", or "3"
                    if '1' in last_message_element.text or '2' in last_message_element.text or '3' in last_message_element.text:
                        key = last_message_element.text.strip()[-1]  # Get the last character as key
                        message_file_map = {
                            '1': r'C:\Users\juan\Desktop\AutoWhats\msg\segundo.txt',
                            '2': r'C:\Users\juan\Desktop\AutoWhats\msg\terceiro.txt',
                            '3': r'C:\Users\juan\Desktop\AutoWhats\msg\quarto.txt'
                        }

                        # Read the corresponding message file and copy it to the clipboard
                        with open(message_file_map[key], 'r', encoding='utf-8') as file:
                            follow_up_message = file.read()
                        pyperclip.copy(follow_up_message)

                        # Paste the content in the message input field
                        pyautogui.hotkey('ctrl', 'v')
                        usleep(3, 5)

                        pyautogui.hotkey('enter')
                        usleep(3, 5)
                        break  # Exit the loop after sending the follow-up message

                except NoSuchElementException:
                    print(f"Tentativa {i+1}/3: Nenhuma mensagem encontrada, aguardando mais 10 segundos...")
                    time.sleep(10)
                    continue

            usleep(9999, 5)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            usleep(3, 3)
            driver.quit()
            continue  # Restart the loop
        finally:
            if driver:
                driver.quit()  # Ensure the driver is always closed
