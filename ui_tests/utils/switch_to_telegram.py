def switching_to_desktop_telegram(Options):
    chrome_options = Options()
    prefs = {
        "protocol_handler": {
            "allowed_origin_protocol_pairs": {
                "https://t.me": {"tg": True}
            }
        }
    }
    chrome_options.add_experimental_option("prefs", prefs)