import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class GlobalCommonActions:
    options = webdriver.EdgeOptions()
    prefs = {'download.default_directory': 'C:\\Users\\Administrator\\Downloads'}
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("start-maximized")
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(version="103.0.1264.37").install()),
                            options=options)
    webdriver_wait = WebDriverWait(driver, 20)
    webdriver_short_wait = WebDriverWait(driver, 3)
    actions = ActionChains(driver)

    use_ec = ec

    #   ----------  DRIVER METHODS   ----------

    def switch_to_window_tab(self, index_of_window_to_switch):
        self.driver.switch_to.window(self.driver.window_handles[index_of_window_to_switch])
        print(f"You switched to tab with the index of: {index_of_window_to_switch}")

    def open_new_window_tab(self):
        self.driver.switch_to.new_window("tab")
        print(f"You opened new tab")

    def close_current_tab(self):
        current_page_url = self.driver.current_url
        current_page_title = self.driver.title
        print(f"You closed the current tab!")
        print(f"Closed tab page url: {current_page_url}")
        print(f"Closed tab page title: {current_page_title}")
        self.driver.close()

    def navigate_to_url(self, url):
        self.driver.get(url)
        print(f"Go to url: {url}")

    def refresh_page(self, time_to_sleep=10):
        self.driver.refresh()
        print("Refreshing the Page.")
        self.time_sleep(time_to_sleep)

    #   ----------  GENERAL STATIC METHODS   ----------

    @staticmethod
    def print_test_step(step_to_be_printed):
        print(f"\n#################### TEST STEP: {step_to_be_printed}  ####################\n")

    @staticmethod
    def time_sleep(seconds_to_sleep):
        print(f"Sleep for a few seconds: {seconds_to_sleep}")
        time.sleep(seconds_to_sleep)

    @staticmethod
    def copy_existing_list_to_new_list(old_list: list):
        new_list = old_list.copy()
        print(f"List data of {old_list} is copied to a new list.")
        return new_list

    @staticmethod
    def verify_lists_are_not_the_same(list_1, list_2):
        assert list_1 != list_2
        print(f"Verified! 'List 1' with data: \n{list_1}\nis not the same as 'List 2' with data: \n{list_2}")

    #   ----------  LOCATE METHODS  ----------
    def locate_xpath(self, xpath_locator: list, seconds_to_wait=30):
        dynamic_wait = WebDriverWait(self.driver, seconds_to_wait)
        dynamic_wait.until(ec.visibility_of_element_located((By.XPATH, xpath_locator[1])))
        print(f"Locating element: {xpath_locator[0]}")
        return self.driver.find_element(By.XPATH, xpath_locator[1])

    def locate_elements_xpath(self, xpath_locator: list):
        print(f"Locating all elements of: {xpath_locator[0]}")
        return self.driver.find_elements(By.XPATH, xpath_locator[1])

    def locate_and_get_text(self, xpath_locator: list):
        print(f"Getting the element text of: *** {xpath_locator[0]} ***")
        print(f"The element text is: *** {self.locate_xpath(xpath_locator).text} ***")
        return self.locate_xpath(xpath_locator).text

    def locate_and_click(self, xpath_locator: list):
        self.locate_xpath(xpath_locator).click()
        print(f"Clicked on element: {xpath_locator[0]}")

    def locate_and_select_from_dropdown_by_value(self, xpath_locator: list, value=""):
        Select(self.locate_xpath(xpath_locator)).select_by_value(value)
        print(f"Selecting from dropdown element of: {xpath_locator[0]}")
        print(f"With the value of: {value}")
        print(f"Verifying if option is selected successfully.")
        selected_item = self.locate_xpath(xpath_locator).find_element(By.XPATH, '//option[@selected]')
        print(f"The text of selected item is: {selected_item.text}")
        selected_item_attribute = selected_item.get_attribute("value")
        print(f"The item attribute used is 'value' and the data is: **{selected_item_attribute}**")
        assert value in selected_item_attribute
        print(f"Verified Successfully! expected value: **{value}** "
              f"is present on selected item's actual value: **{selected_item_attribute}**")

    def locate_and_select_from_dropdown_by_index(self, xpath_locator: list, index):
        Select(self.locate_xpath(xpath_locator)).select_by_index(index)
        print(f"Selecting from dropdown element of: {xpath_locator[0]}")
        print(f"With the index of: {index}")
        print(f"Verifying if option is selected successfully.")
        selected_item = self.locate_xpath(xpath_locator).find_element(By.XPATH, '//option[@selected]')
        print(f"The text of selected item is: {selected_item.text}")
        selected_item_attribute = selected_item.get_attribute("index")
        print(f"The item attribute used is 'index' and the data is: **{selected_item_attribute}**")
        assert index in selected_item_attribute
        print(f"Verified Successfully! expected index: **{index}** "
              f"is present on selected item's actual index: **{selected_item_attribute}**")

    def locate_and_select_from_dropdown_by_visible_text(self, xpath_locator: list, visible_text):
        Select(self.locate_xpath(xpath_locator)).select_by_visible_text(visible_text)
        print(f"Selecting from dropdown element of: {xpath_locator[0]}")
        print(f"With the visible text of: {visible_text}")
        print(f"Verifying if option is selected successfully.")
        selected_item = self.locate_xpath(xpath_locator).find_element(By.XPATH, '//option[@selected]')
        print(f"The text of selected item is: {selected_item.text}")
        assert visible_text in selected_item.text
        print(f"Verified Successfully! expected text: **{visible_text}** "
              f"is present on selected item's visible text: **{selected_item.text}**")

    def locate_and_add_to_list_element_text(self, xpath_locator: list, name_of_list: list):
        print(f"Finding all elements with xpath of: {xpath_locator[0]}")
        elements_found = self.locate_elements_xpath(xpath_locator)
        print(f"Adding all element text to the list.")
        for element in elements_found:
            name_of_list.append(element.text)
        print(f"The list data is: {name_of_list}")

    def locate_and_send_keys(self, xpath_locator: list, keys_to_send, clear=True):
        if clear:
            print("Clearing all previously inputted text.")
            self.locate_xpath(xpath_locator).send_keys(Keys.CONTROL + "A")
            time.sleep(5)
            print(f"Sending data to **{xpath_locator[0]}**.")
            self.locate_xpath(xpath_locator).send_keys(keys_to_send)
            print(f"The sent data is: **{keys_to_send}**")
        else:
            print(f"Sending keys to **{xpath_locator}**")
            self.locate_xpath(xpath_locator).send_keys(keys_to_send)
            print(f"The sent data is: **{keys_to_send}**")
    #   ----------  GET METHODS ----------

    def get_inputted_value_and_assert(self, xpath_locator: list, expected_input_value):

        input_value = self.locate_xpath(xpath_locator).get_attribute('value')
        print(f"the value of the textbox is: " + str(input_value))
        assert expected_input_value in input_value
        print(f"Verified Successfully. {expected_input_value} is inside the element value of: {input_value}")
        return input_value

    def get_attribute_value_text(self, xpath_locator: list):
        attribute_value = self.locate_xpath(xpath_locator).get_attribute('value')
        print(f"getting the attribute value of {xpath_locator[0]}. The value is: {attribute_value}")
        return attribute_value

    def get_element_location(self, xpath_locator: list):
        current_location = self.locate_xpath(xpath_locator).location
        print(f"The current location of **{xpath_locator[0]}** is: {current_location}")
        return current_location

    #   ----------  VERIFY  ----------
    def verify_checkbox_is_checked_true(self, xpath_locator: list):
        self.webdriver_wait.until(ec.element_located_selection_state_to_be((By.XPATH, xpath_locator[1]), True))
        print(f"Verified successfully. Checkbox of **{xpath_locator[0]}** is marked as 'True' ")

    def verify_checkbox_is_checked_false(self, xpath_locator: list):
        self.webdriver_wait.until(ec.element_located_selection_state_to_be((By.XPATH, xpath_locator[1]), False))
        print(f"Verified successfully. Checkbox of **{xpath_locator[0]}** is marked as 'False' ")

    def verify_current_url(self, url_to_verify):
        current_url = self.driver.current_url
        print("The current url is: " + current_url)
        assert url_to_verify == current_url
        print(f"Verified Successfully! the current url: **{current_url}** "
              f"matches with expected url: **{url_to_verify}**")

    def verify_current_title(self, title_to_verify):
        current_title = self.driver.title
        print("The current page title is: " + current_title)
        assert title_to_verify == current_title
        print(f"Verified Successfully! the current title: **{current_title}** "
              f"matches with expected title: **{title_to_verify}**")

    def verify_text_present_in_element(self, xpath_locator: list, expected_text_to_be_verified):
        text_of_current_element = self.locate_xpath(xpath_locator).text
        print(f"the text in **{xpath_locator[0]}** is: *** {text_of_current_element} ***\n")
        assert expected_text_to_be_verified in text_of_current_element
        print(f"Verified Successfully! expected text: **{expected_text_to_be_verified}** "
              f"is in actual text of **{xpath_locator[0]}**: **{text_of_current_element}**")

    def verify_element_have_attribute(self, xpath_locator: list, attribute_to_get, expected_attribute=""):
        all_element_attribute = self.locate_xpath(xpath_locator).get_attribute(attribute_to_get)
        print(f"All attributes of the **{xpath_locator[0]}** is: {all_element_attribute}")
        assert expected_attribute in all_element_attribute
        print(f"expected attribute: **{expected_attribute}** "
              f"is present in all element attribute of **{xpath_locator[0]}**: **{all_element_attribute}**")

    def verify_element_does_not_have_attribute(self, xpath_locator: list, attribute_to_get):
        self.webdriver_wait.until_not(ec.element_attribute_to_include((By.XPATH, xpath_locator[1]), attribute_to_get))
        print(f"Verified Successfully. Element **{xpath_locator[0]}** does NOT have attribute: **{attribute_to_get}**")

    #   ----------  WAIT    ----------
    def dynamic_wait(self, seconds_to_wait=30):
        return WebDriverWait(self.driver, seconds_to_wait)

    def wait_until_element_visible(self, xpath_locator: list, seconds_to_wait=30):
        print(f"waiting for {seconds_to_wait} seconds until element: **{xpath_locator[0]}** is visible ")
        dynamic_wait = WebDriverWait(self.driver, seconds_to_wait)
        dynamic_wait.until(ec.visibility_of_element_located((By.XPATH, xpath_locator[1])))

    def wait_until_element_not_visible(self, xpath_locator: list, seconds_to_wait=30):
        print(f"waiting for {seconds_to_wait} seconds until element: **{xpath_locator[0]}** is NOT visible ")
        dynamic_wait = WebDriverWait(self.driver, seconds_to_wait)
        dynamic_wait.until(ec.invisibility_of_element_located((By.XPATH, xpath_locator[1])))

    def wait_until_element_attached_to_page(self, xpath_locator: list, seconds_to_wait=30):
        print(f"waiting for {seconds_to_wait} seconds until element: **{xpath_locator[0]}** is attached to page. ")
        self.dynamic_wait(seconds_to_wait).until(ec.presence_of_element_located((By.XPATH, xpath_locator[1])))

    def wait_until_element_not_attached_to_page(self, xpath_locator: list, seconds_to_wait=30):
        print(f"waiting for {seconds_to_wait} seconds until element: **{xpath_locator[0]}** is NOT attached to page. ")
        self.dynamic_wait(seconds_to_wait).until_not(ec.presence_of_element_located((By.XPATH, xpath_locator[1])))

    #   ----------  ACTIONS ----------
    def action_right_click(self, xpath_locator: list):
        print(f"Right clicking on element: {xpath_locator[0]}")
        self.actions.context_click(self.locate_xpath(xpath_locator)).perform()

    def action_get_alert_assert_text_and_accept(self, expected_alert_text=""):
        self.webdriver_wait.until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_msg = alert.text
        print(f"actual alert message: {alert_msg}")
        assert expected_alert_text in alert_msg
        print(f"Verified Successfully. expected alert: **{expected_alert_text}** "
              f"is in actual alert message: **{alert_msg}**")
        alert.accept()
        print("Action: Alert Accepted!")

    def action_get_alert_assert_text_and_dismiss(self, expected_alert_text=""):
        self.webdriver_wait.until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_msg = alert.text
        print(f"actual alert message: {alert_msg}")
        assert expected_alert_text in alert_msg
        print(f"Verified Successfully. expected alert: **{expected_alert_text}** "
              f"is in actual alert message: **{alert_msg}**")
        alert.dismiss()
        print("Action: Alert Dismissed!")

    def action_get_alert_assert_text_and_send_keys(self, keys_to_send, expected_alert_text=""):
        self.webdriver_wait.until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_msg = alert.text
        print(f"actual alert message: {alert_msg}")
        assert expected_alert_text in alert_msg
        print(f"Verified Successfully. expected alert: **{expected_alert_text}** "
              f"is in actual alert message: **{alert_msg}**")
        alert.send_keys(keys_to_send)
        print(f"Sent Keys on alert. Keys: **{keys_to_send}**")
        alert.accept()
        print("Action: Alert Accepted!")

    def action_drag_and_drop_from_to(self, source: list, target: list):
        self.actions.drag_and_drop(self.locate_xpath(source), self.locate_xpath(target))
        self.actions.perform()
        print(f"Dragged source element: **{source[0]}** to target: ***{target[0]}**")

    def action_hover_on_element(self, xpath_locator: list):
        self.actions.move_to_element(self.locate_xpath(xpath_locator)).perform()
        print(f"Hovered on element: {xpath_locator[0]}")








