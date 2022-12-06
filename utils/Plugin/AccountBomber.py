from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def unfriend_all(token: str):
    
    # 옵션 설정정
    options = Options()
    options.headless = True
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    driver.get(url="https://discord.com/app")
    
    # 토큰으로 로그인하는 스크립트 
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

    show_all_friend_nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tabBar-ra-EuL.topPill-3DJJNV :nth-child(2)")))
    show_all_friend_nav.click()

    try:
        extra_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "svg.icon-1WVg4I")))[1::2]
    except TimeoutException:
        return

    for extra_button in extra_buttons:
        extra_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.label-2gNW3x")))[1].click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".lookFilled-yCfaCM > div.contents-3ca1mk"))).click()

    time.sleep(1)
    driver.quit()


def accounts_bomber():
    with open("token.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 주석 처리된 문장 무시
            if line.startswith("#"):
                continue
            unfriend_all(line)
