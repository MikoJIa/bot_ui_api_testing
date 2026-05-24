from selenium.webdriver.common.by import By

loc_all_products = (By.XPATH, '//div[@class="t-store__card-list "]'
                              '//div[@class="js-product t-store__card t-store__stretch-col t-store__stretch-col_33 t-align_left t-item"]')
loc_button_Leave_request = By.XPATH, '//span[@class="t-btnflex__text" and contains(text(), "Оставить заявку")]'
loc_text_next_page = By.XPATH, '//div[@id="popuptitle_1629545171"]'
loc_input_name = By.XPATH, '//input[@id="input_6911158238961"]'
loc_input_phone_number = By.XPATH, '//input[@id="input_6711158238962"]'
loc_input_describe_task = By.XPATH, '//textarea[@id="input_1764507691858"]'
loc_button_select_file =  By.XPATH, '//button[@class="uploadcare--widget__button uploadcare--widget__button_type_open"]'
loc_button_link_to_file = By.XPATH, '//div[@class="uploadcare--menu__item uploadcare--menu__item_tab_url"]'
loc_provide_link = By.XPATH, '//input[@placeholder="Укажите здесь ссылку..."]'
loc_download_link = By.XPATH, '//button[@class="uploadcare--button uploadcare--button_primary uploadcare--tab__action-button"]'
loc_soft_pixar = (By.XPATH, '//div[@class="js-product t-store__card t-store__stretch-col t-store__stretch-col_33 t-align_left t-item"]'
                            '//a[@href="http://artmas.by/catalog/tproduct/1568598351-130013763202-modulnii-divan-pixar"]'
                            '//div[@class="t-store__card__imgwrapper  t-store__card__imgwrapper_1-1"]')


loc_button_order = By.XPATH, '//span[contains(text(), "Заказать")]'
loc_text_soft_pixar = By.XPATH, '//a[contains(text(), "Модульный диван «PIXAR»")]'
loc_quantity_soft_to_basket = By.XPATH, '//span[@class="t706__product-quantity"]'
loc_soft_form_name = By.XPATH, '//input[@id="input_6919899894910"]'
loc_soft_form_phone = By.XPATH, '//input[@id="input_6919899894911"]'
loc_soft_form_desc = By.XPATH, '//input[@id="input_6919899894912"]'
loc_soft_form_checkbox = By.XPATH, '//div[@class="t-checkbox__indicator"]'
loc_button_soft_form = By.XPATH, '//div[@class="t-form__submit"]//span[@class="t-btnflex__text" and contains(text(), "Отправить")]'
loc_delete_soft = By.XPATH, '//span[@class="t706__product-del"]'
loc_soft_order_success = By.XPATH, '//span[@class="js-successbox t-form__successbox t-text t-text_md"]'

