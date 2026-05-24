def test_name_main_page(main_page):
    main_page.open_page()
    main_page.check_main_page("ARTMAS")


def test_catalog_page(main_page):
    main_page.open_page()
    main_page.check_link_catalog_page("Диваны")


def test_projects_page(main_page):
    main_page.open_page()
    main_page.check_projects_page("Проекты от Artmas")


def test_designers_page(main_page):
    main_page.open_page()
    main_page.check_designers("Стать партнером")


def test_blog_page(main_page):
    main_page.open_page()
    main_page.check_blog_page("Последние новости в блоге")


def test_contacts_page(main_page):
    main_page.open_page()
    main_page.check_contacts("The furniture made in belarus")


def test_link_whats_app(main_page):
    main_page.open_page()
    main_page.check_link_whatsapp("Привет! Хочу сделать заказ")


def test_link_telegram(main_page):
    main_page.open_page()
    main_page.check_link_telegram("https://t.me/Artmas_mebel")


def test_link_instagram(main_page):
    main_page.open_page()
    main_page.check_link_instagram()


def test_scroll_to_footer_main(main_page):
    main_page.open_page()
    main_page.check_text_main_footer("ООО «Артмас Мебель»")


def test_element_meddle_page(main_page):
    main_page.open_page()
    main_page.check_text_in_middle_page('Кровать "LISBON"', 1300)

def test_callback(main_page):
    main_page.open_page()
    main_page.check_callback_button('I need specialist help')


