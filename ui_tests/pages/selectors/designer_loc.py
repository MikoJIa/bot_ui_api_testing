from selenium.webdriver.common.by import By

loc_button_become_partner = By.XPATH, '//span[contains(text(), "Стать партнером")]'
loc_input_name = By.XPATH, '//input[@id="input_9717201386410"]'
loc_input_phone = By.XPATH, '//input[@id="input_9717201386411"]'
loc_input_city = By.XPATH, '//input[@id="input_9717201386412"]'
loc_input_email = By.XPATH, '//input[@id="input_9717201386413"]'
loc_input_comment = By.XPATH, '//input[@id="input_9717201386414"]'
loc_checkbox = By.XPATH, '//div[@class="t702__wrapper"]//div[@class="t-checkbox__indicator"]'
loc_button_send = By.XPATH, '//div[@class="t702__wrapper"]//span[@class="t-btnflex__text" and contains(text(), "Отправить")]'
loc_successe = By.XPATH, '//div[@id="tildaformsuccesspopuptext-new"]'