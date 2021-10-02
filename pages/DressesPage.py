import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class DressesPage(BasePage):
    SummerDresses_link = (By.XPATH,"//*[@id='categories_block_left']//child::div//child::ul//child::li[3]")
    add_to_cart_button = (By.XPATH,"//button[@type='submit' and @name='Submit']")
    products_id = (By.XPATH,"//ul[@class='product_list grid row']")
    Dresses_page_link = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")
    SummerDresses_on_Cart = (By.XPATH, "//*[@title='Summer Dresses']//parent::div")
    Countinue_shopping_cart = (By.XPATH, "//span[@class='continue btn btn-default button exclusive-medium']")
    cart_quantity = (By.XPATH, "//span[@class='ajax_cart_quantity']//parent::a[@title='View my shopping cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_summer_dresses_to_cart_and_return_number_of_items(self):
        print('add_summer_dresses_to_cart called')
        self.do_click(self.Dresses_page_link)
        self.do_click(self.SummerDresses_link)
        html_list = self.driver.find_element_by_xpath("//ul[@class='product_list grid row']")
        #items = html_list.find_elements_by_tag_name("li")
        items = html_list.find_elements_by_xpath("//ul[@class='product_list grid row']//child::li[contains(@class, 'ajax_block_product')]")
        items_len = len(items)
        print('items list is ', items, items_len)
        print('items length is ', items_len)
        for item in range(1, items_len+1):
            str1 = str(item)
            text = 'li[' + str1 + ']'
            element_location = "//*[@id='center_column']/ul/" + text
            print(element_location)
            element = (By.XPATH, element_location)
            self.do_click(element)
            #self.mouse_hover(element)
            self.do_click(self.add_to_cart_button)
            time.sleep(5)
            self.driver.refresh()
            self.do_click(self.SummerDresses_on_Cart)

        return items_len

    def get_cart_quantity(self):
        return self.get_text(self.cart_quantity)

