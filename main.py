from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.firefox.options import Options


EMAIL = "#"
PASSWORD = "#"
driver = None


def click_on_element_when_available(selector: str):
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, selector)))
    element = driver.find_element_by_css_selector(selector)
    element.click()


def play():

    # log in page
    driver.get("https://www.grandkafa.rs/play/start")

    username_input = driver.find_element_by_id("email")
    username_input.click()
    username_input.send_keys(EMAIL)

    password_input = driver.find_element_by_id("password")
    password_input.click()
    password_input.send_keys(PASSWORD)

    # submit the form
    password_input.send_keys(Keys.RETURN)

    # when new page opened redirect to the game page
    WebDriverWait(driver, 60).until(EC.staleness_of(username_input))

    while True:
        try:
            button_start_selector = ".sh-button.sh-button--primary.js-shake-play"
            click_on_element_when_available(button_start_selector)

            button_add_coffee_selector = ".sh-button.sh-button--primary.js-shake-add-coffee"
            click_on_element_when_available(button_add_coffee_selector)

            button_add_water_selector = ".sh-button.sh-button--primary.js-shake-add-water"
            click_on_element_when_available(button_add_water_selector)

            button_mix_button_selector = ".sh-button.sh-button--primary.js-shake-mix"
            click_on_element_when_available(button_mix_button_selector)

            button_mix_more_selector = ".sh-button.sh-button--primary.js-shake-mix-more"
            click_on_element_when_available(button_mix_more_selector)
            click_on_element_when_available(button_mix_more_selector)

            button_play_again_selector = ".sh-button.sh-button--primary.sh-button--bottom.js-shake-restart-game"
            click_on_element_when_available(button_play_again_selector)
        except UnexpectedAlertPresentException:
            button_reset_selector = ".sh-button.sh-button--primary.sh-button--bottom.js-shake-restart-game"
            click_on_element_when_available(button_reset_selector)


if __name__ == '__main__':
    while True:
        try:
            # Define headless as true to make this work in background
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            play()
        except Exception:
            driver.close()

