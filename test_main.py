import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description(
    'Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):

    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")


    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",  "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()

    with allure.step(f"Verifying the page heading for {expected_menu_items[3]}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step(f"Clicking on menu item: {expected_menu_items[4]}"):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step(f"Clicking on menu item: {expected_menu_items[5]}"):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Clicking on menu item: {expected_menu_items[6]}"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h2')))
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f"Clicking on menu item: {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()


@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])
@allure.feature('Nested Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Nested Menu Navigation')
@allure.description('Verifies that nested menu items navigate to the correct pages.')
@allure.severity(allure.severity_level.NORMAL)
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Hovering over menu item: {menu_locator[1]} and clicking submenu"):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f"Verifying the page heading for {result_text}"):
        assert driver.find_element(By.TAG_NAME, 'h2').text == result_text


@allure.feature('Product Search')
@allure.suite('UI Tests')
@allure.title('Test Product Search')
@allure.description('Verifies that searching for a product returns correct results.')
@allure.severity(allure.severity_level.NORMAL)
def test_search_product(driver):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Performing product search for 'MacBook'"):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step("Verifying search results contain 'MacBook'"):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
        assert len(products) == len(new_list)


@allure.feature('Shopping Cart')
@allure.suite('UI Tests')
@allure.title('Test Add to Cart')
@allure.description('Verifies that adding a product to the cart works correctly.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Adding product to cart"):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step("Waiting for success message to appear"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text

    with allure.step("Waiting for the cart to be updated"):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step("Clicking the cart button"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step("Waiting for the cart dropdown to load"):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got {cart_contents.text}"


@allure.feature('Slider Functionality')
@allure.suite('UI Tests')
@allure.title('Test Slider Functionality')
@allure.description('Verifies that the slider functions correctly.')
@allure.severity(allure.severity_level.NORMAL)
def test_slider_functionality(driver):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Locating the slider element"):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step("Locating the first active slide"):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step("Interacting with the slider control (next arrow)"):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step("Locating the new active slide"):
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")

        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step("Testing the left arrow to return to the first slide"):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')
        prev_arrow.click()

        WebDriverWait(driver, 10).until_not(
            EC.element_to_be_clickable(new_slide)
        )

        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img").get_attribute("src")
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@allure.feature('Wishlist Functionality')
@allure.suite('UI Tests')
@allure.title('Test Add to Wishlist')
@allure.description('Verifies that adding a product to the wishlist works correctly.')
@allure.severity(allure.severity_level.NORMAL)
def test_add_to_wishlist(driver, login):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step("Adding a product to the wishlist"):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    with allure.step("Waiting for the success message"):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Failed to add product to the wishlist."

    with allure.step("Navigating to the wishlist page"):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()


@pytest.mark.parametrize("button, header, expected_text", [
    (
            (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),  # 'About Us' link
            (By.XPATH, '//*[@id="content"]/h1'),  # 'About Us' header
            "About Us"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),  # 'Contact Us' link
            (By.XPATH, '//*[@id="content"]/h1'),  # 'Contact Us' header
            "Contact Us"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),  # 'Product Returns' link
            (By.XPATH, '//*[@id="content"]/h1'),  # 'Product Returns' header
            "Product Returns"
    ),
    (
            (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),  # 'Find Your Favorite Brand' link
            (By.XPATH, '//*[@id="content"]/h1'),  # 'Find Your Favorite Brand' header
            "Find Your Favorite Brand"
    ),
    (
            (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),  # 'Purchase a Gift Certificate' link
            (By.XPATH, '//*[@id="content"]/h1'),  # 'Purchase a Gift Certificate' header
            "Purchase a Gift Certificate"
    )
])
@allure.feature('Footer Links')
@allure.suite('UI Tests')
@allure.title('Test Footer Links')
@allure.description('Verifies that footer links navigate to the correct pages.')
@allure.severity(allure.severity_level.NORMAL)
def test_footer(driver, button, header, expected_text):
    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f"Clicking footer link: {expected_text}"):
        footer_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button)
        )
        footer_button.click()

    with allure.step(f"Waiting for the page header to be visible for {expected_text}"):
        footer_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(header)
        )

    with allure.step("Verifying the header text matches the expected value"):
        footer_header_text = footer_header.text
        assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'."
