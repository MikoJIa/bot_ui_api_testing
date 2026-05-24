from selenium.webdriver.common.by import By

name_main_page = (By.XPATH, "//h1//span[2]")
catalog_loc = (
    By.XPATH,
    '//div[@class="t228__centerside"]'
    '//ul[@class="t228__list t-menu__list"]//a[@href="/catalog"]',
)
catalog_page_name_loc = (
    By.XPATH,
    '//div[@data-storepart-uid="Диваны"]'
    '//div[@class="t-store__parts-tree-btn-title"]',
)
projects_loc = (
    By.XPATH,
    "//div[@id='nav1564868971']/div[@class='t228__maincontainer ']"
    "/div[@class='t228__centerside']"
    "/nav[@class='t228__centercontainer']"
    "/ul[@class='t228__list t-menu__list']"
    "/li[@class='t228__list_item'][2]"
    "/a[@class='t-menu__link-item']",
)
projects_page_name_loc = (
    By.XPATH,
    "//div[@id='rec1565237741']"
    "/div[@class='t1004']"
    "/div[@class='t-section__container t-container t-container_flex']"
    "/div[@class='t-col t-col_12 ']"
    "/div[@class='js-block-header-title t-section__title t-title t-title_xs t-align_center t-margin_auto']",
)
designers_loc = (
    By.XPATH,
    "//div[@id='nav1564868971']"
    "/div[@class='t228__maincontainer ']"
    "/div[@class='t228__centerside']"
    "/nav[@class='t228__centercontainer']"
    "/ul[@class='t228__list t-menu__list']"
    "/li[@class='t228__list_item'][3]"
    "/a[@class='t-menu__link-item']",
)
designers_name_page_loc = (
    By.XPATH,
    "//div[@id='recorddiv1724592731']"
    "/div[@class='t-container']/div[@class='t-col t-col_8 ']"
    "/div[@class='t-cover__wrapper t-valign_middle']"
    "/div[@class='t216 t-align_left']/div/div[@class='t216__wrapper']"
    "/h1[@class='t216__title t-title t-title_xl']",
)
blog_loc = (
    By.XPATH,
    "//div[@id='nav1564868971']"
    "/div[@class='t228__maincontainer ']"
    "/div[@class='t228__centerside']"
    "/nav[@class='t228__centercontainer']"
    "//a[@href='/blog']",
)
blog_name_page_loc = (By.XPATH, "//div[contains(text(), 'Последние новости в блоге')]")
contacts_loc = (By.XPATH, '//li[@class="t228__list_item"] //a[@href="/contacts"]')
contacts_name_page_loc = (
    By.XPATH,
    "//div[@id='rec1629378201']"
    "/div[@class='t1148']"
    "/div[@class='t1148__container_flex t-container t-container_flex']"
    "/div[@class='t-col t-col_10 t1148__col']"
    "/div[@class='t-section__container t-container t-container_flex']"
    "/div[@class='t-col t-col_12']"
    "/div[@class='js-block-header-title t-section__title t-title t-title_xs t-align_left']",
)
element_designers_loc = (By.XPATH, "//a[@id='cardbtn1_1719906451'] //span")
loc_bel = (
    By.XPATH,
    "//div[@id='recorddiv1629421751']"
    "/div[@class='t164']/div[@class='t-container']"
    "/div[@class='t-cover__wrapper t-valign_middle']"
    "/div[@class='t-col t-col_10 t-prefix_1 t-align_left']"
    "/div/div[@class='t164__wrapper']"
    "/div[@class='t164__descr t-descr t-descr_xxxl']"
    "/p/span",
)

all_link_headers_main_page = {
    "catalog": catalog_loc,
    "projects": projects_loc,
    "blog": blog_loc,
}

all_name_in_page = {
    "catalog": catalog_page_name_loc,
    "projects": projects_page_name_loc,
    "blog": blog_name_page_loc,
}

loc_whatsapp = (
    By.XPATH,
    "//div[@id='nav1564868971']"
    "/div[@class='t228__maincontainer ']"
    "/div[@class='t228__rightside']"
    "/div[@class='t228__rightcontainer']"
    "/div[@class='t-sociallinks']"
    "/ul[@class='t-sociallinks__wrapper']"
    "/li[@class='t-sociallinks__item t-sociallinks__item_whatsapp']",
)
loc_text_whatsapp = (By.XPATH, "//p[contains(text(), 'Привет! Хочу сделать заказ')]")
loc_text_whatsapp_2 = (
    By.XPATH,
    "//p[contains(@class, '_9vd5') and contains(text(), 'Привет')]",
)

loc_telegram = (By.XPATH, "//a[@aria-label='telegram' and contains(@href, 't.me')]")
loc_instagram = (
    By.XPATH,
    "//a[@aria-label='instagram' and contains(@href, 'www.instagram.com')]",
)
loc_text_instagram_2 = (
    By.XPATH,
    "//span[contains(text(), 'Sign up and never miss a post from artmas.by.')]",
)
loc_text_instagram = (
    By.XPATH,
    "//span[contains(text(), 'See photos, videos and more from artmas.by')]",
)
loc_text_footer = (By.XPATH, '//span[contains(text(), "ООО «Артмас Мебель»")]')
loc_lisbon = (
    By.XPATH,
    '//div[@class="t754__textwrapper"]//div[@field="li_title__3156925032118"]',
)
loc_callback = By.XPATH, '//div[@class="b24-widget-button-icon-container"]'
loc_open_line = By.XPATH, ("/html[@class='crm-widget-button-mobile']"
                           "/body[@class='t-body']"
                           "/div[2]"
                           "/div"
                           "/div[@class='b24-widget-button-wrapper b24-widget-button-position-bottom-right b24-widget-button-visible b24-widget-button-bottom']"
                           "/div[@class='b24-widget-button-social b24-widget-button-show']"
                           "/a[@class='b24-widget-button-social-item b24-widget-button-openline_livechat']")
loc_input_message = By.XPATH, "//textarea[@placeholder='Введите сообщение...']"
loc_button_message = By.XPATH, '//button[@title="Отправить сообщение"]'
loc_text_message = By.XPATH, '//span[@class="bx-im-message-content-text"]'
