def find_browsers_windows(driver):
    all_windows = driver.window_handles
    return driver.switch_to.window(all_windows[1])

def get_alert_text(driver):
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Текст alert: {alert_text}")
        return alert_text
    except:
        print("Нет активного alert")
        return None
