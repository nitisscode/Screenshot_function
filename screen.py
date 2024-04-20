# libraries for run this program

from selenium import webdriver
from PIL import Image
from io import BytesIO

def TakeScreenshot():
#input for paste url of webpage
    print('Note: Please do not use "https://"')
    url=input("Enter website link here: ")

    #url = "https://google.com"        


    #open browser
    driver = webdriver.Chrome()  

    # Open the webpage
    driver.get("https://"+url)

    #window size
    driver.set_window_size(1920, 1080) 

    # Capture screenshot
    screenshot = driver.get_screenshot_as_png()

    # Convert the screenshot to PIL Image
    img = Image.open(BytesIO(screenshot))
    img.show() # show captured image

    # Save the screenshot
    img.save("screenshot.png")

    # Close the browser
    driver.quit()
TakeScreenshot()