from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://adnabuteststore.myshopify.com")

wait = WebDriverWait(driver, 10)

# Search product
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("shirt")
search_box.send_keys(Keys.RETURN)

# Click first product
product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item a")))
product.click()

# Add to cart
add_to_cart = wait.until(EC.element_to_be_clickable((By.NAME, "add")))
add_to_cart.click()

print("Product added to cart successfully")

driver.quit()
