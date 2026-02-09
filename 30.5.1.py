import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://petfriends.skillfactory.ru')
    yield driver
    driver.quit()


def test_show_my_pets_with_waits(driver):
    wait = WebDriverWait(driver, 10)

    reg_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-success')))
    reg_btn.click()

    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "У меня уже есть аккаунт")))
    login_link.click()

    driver.find_element(By.ID, 'email').send_keys('fluffycat@yandex.ru')
    driver.find_element(By.ID, 'pass').send_keys('lalala123')

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert len(names) > 0, "Список питомцев на странице пуст!"

    no_photo_count = 0
    no_name_count = 0

    print(f"\nНачинаем проверку {len(names)} питомцев...")

    for i in range(len(names)):
        if images[i].get_attribute('src') == '':
            no_photo_count += 1
            print(f"[INFO] Питомец №{i}: фото отсутствует")

        pet_name = names[i].text
        if pet_name == '':
            no_name_count += 1
            print(f"[WARNING] Питомец №{i}: имя пустое!")
        else:
            print(f"[OK] Питомец №{i}: Имя = '{pet_name}'")

        pet_desc = descriptions[i].text
        assert pet_desc != '', f"Критическая ошибка: у питомца №{i} ({pet_name}) совсем нет описания"
        assert ', ' in pet_desc, f"Критическая ошибка: неверный формат (вид, возраст) у №{i}"

    print(f"\n======= ТЕСТ ЗАВЕРШЕН =======")
    print(f"Всего проанализировано: {len(names)}")
    print(f"Питомцев без фото: {no_photo_count}")
    print(f"Питомцев без имени: {no_name_count}")
    print(f"=============================")
