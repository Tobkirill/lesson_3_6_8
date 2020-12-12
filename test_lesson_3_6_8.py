import time


def test_should_be_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), f"add to cart button is not found on the page"
