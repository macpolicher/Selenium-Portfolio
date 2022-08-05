import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from CommonPackage.CommonActions import GlobalCommonActions
from PageLocators import Locator
import os.path


class TestTheInternet(GlobalCommonActions):

    def test_add_remove_elements(self):
        test_add_remove_elements_steps = {
            1: "Navigate to Add/Remove Elements Page",
            2: "Verify that 'Delete Element' button is not visible",
            3: "Click 'Add Element' Button",
            4: "Verify that 'Delete' button shows up on the page",
            5: "Click 'Delete' Button",
            6: "Verify that the 'Delete' Button is no longer visible"
        }
        self.print_test_step(test_add_remove_elements_steps[1])
        self.locate_and_click(Locator.AddRemoveElements.ADD_REMOVE_ELEMENTS_LINK)
        self.print_test_step(test_add_remove_elements_steps[2])
        self.wait_until_element_not_visible(Locator.AddRemoveElements.delete_element_button)
        self.print_test_step(test_add_remove_elements_steps[3])
        self.locate_and_click(Locator.AddRemoveElements.add_element_button)
        self.print_test_step(test_add_remove_elements_steps[4])
        self.wait_until_element_visible(Locator.AddRemoveElements.delete_element_button)
        self.print_test_step(test_add_remove_elements_steps[5])
        self.locate_and_click(Locator.AddRemoveElements.delete_element_button)
        self.print_test_step(test_add_remove_elements_steps[6])
        self.wait_until_element_not_visible(Locator.AddRemoveElements.delete_element_button)

    def test_broken_image(self):
        test_broken_image_steps = {
            1: "Navigate to Broken Images Page",
            2: "Get all images",
            3: "Look through all images and sort them if they are Broken Image or Not",
            4: "Verify that the total broken images is 2"
        }
        # Get all images
        self.print_test_step(test_broken_image_steps[1])
        self.locate_and_click(Locator.BrokenImage.BROKEN_IMAGE_LINK)
        self.print_test_step(test_broken_image_steps[2])
        images = self.locate_elements_xpath(Locator.BrokenImage.all_images)
        total_count = 0
        total_broken_image = 0
        total_valid_image = 0
        self.print_test_step(test_broken_image_steps[3])
        for image in images:
            total_count += 1
            # assert valid image path has "img" in source
            image_src = image.get_attribute("src")
            if "/img/" in image_src:
                total_valid_image += 1
            else:
                total_broken_image += 1
        print(f"Total Image count is: " + str(total_count))
        print(f"Total Valid Image count is: " + str(total_valid_image))
        print(f"Total Broken Image count is: " + str(total_broken_image))
        self.print_test_step(test_broken_image_steps[4])
        assert int(total_broken_image) == 2
        print(f"Verified Successfully. total broken image is: {total_broken_image}")

    def test_checkboxes(self):
        test_checkboxes_steps = {
            1: "Navigate to Checkboxes Page",
            2: "Verify that Checkbox 1 is unchecked by default",
            3: "Verify that Checkbox 2 is checked by default",
            4: "Click and mark Checkbox 1 as checked",
            5: "Verify that Checkbox 1 is checked",
            6: "Click and mark Checkbox 2 as unchecked",
            7: "Verify that Checkbox 2 is unchecked"
        }
        self.print_test_step(test_checkboxes_steps[1])
        self.locate_and_click(Locator.CheckBoxes.CHECKBOXES_LINK)
        self.print_test_step(test_checkboxes_steps[2])
        self.verify_checkbox_is_checked_false(Locator.CheckBoxes.Checkbox_1)
        self.print_test_step(test_checkboxes_steps[3])
        self.verify_checkbox_is_checked_true(Locator.CheckBoxes.Checkbox_2)
        self.print_test_step(test_checkboxes_steps[4])
        self.locate_and_click(Locator.CheckBoxes.Checkbox_1)
        self.print_test_step(test_checkboxes_steps[5])
        self.verify_checkbox_is_checked_true(Locator.CheckBoxes.Checkbox_1)
        self.print_test_step(test_checkboxes_steps[6])
        self.locate_and_click(Locator.CheckBoxes.Checkbox_2)
        self.print_test_step(test_checkboxes_steps[7])
        self.verify_checkbox_is_checked_false(Locator.CheckBoxes.Checkbox_2)

    def test_context_menu(self):
        test_context_menu_steps = {
            1: "Navigate to Context Menu Page",
            2: "Right Click on Context Menu Box",
            3: "Assert Alert Text and Accept",
            4: "Open new tab to remove context menu options",
            5: "Switch to old tab",
            6: "Close current tab to remove context menu options",
            7: "Switch to the new and remaining window tab"
        }
        self.print_test_step(test_context_menu_steps[1])
        self.locate_and_click(Locator.ContextMenu.CONTEXT_MENU_LINK)
        self.print_test_step(test_context_menu_steps[2])
        self.action_right_click(Locator.ContextMenu.context_menu_box)
        self.print_test_step(test_context_menu_steps[3])
        self.action_get_alert_assert_text_and_accept("You selected a context menu")
        self.print_test_step(test_context_menu_steps[4])
        self.open_new_window_tab()
        self.print_test_step(test_context_menu_steps[5])
        self.switch_to_window_tab(0)
        self.print_test_step(test_context_menu_steps[6])
        self.close_current_tab()
        self.print_test_step(test_context_menu_steps[7])
        self.switch_to_window_tab(0)

    def test_disappearing_elements(self):
        test_disappearing_elements_test = {
            1: "Navigate to Disappearing Elements Page",
            2: "Refresh Page 5 times and record if gallery is visible and not visible",
            3: "Print Result of 'Gallery visible times' "
        }
        #   Navigate to Disappearing Elements Page
        self.print_test_step(test_disappearing_elements_test[1])
        self.locate_and_click(Locator.DisappearingElements.DISAPPEARING_ELEMENTS_LINK)

        gallery_visible_count = 0
        gallery_not_visible_count = 0
        refresh_count = 0
        #   Refresh Page 5 times and record if gallery is visible and not visible
        self.print_test_step(test_disappearing_elements_test[2])
        for _ in range(5):
            try:
                self.wait_until_element_not_visible(Locator.DisappearingElements.gallery_button, 3)
                print(f"refresh count {refresh_count}: Gallery Button not available")
                gallery_not_visible_count += 1
                self.driver.refresh()
            except TimeoutException:
                print(f"refresh count {refresh_count}: Gallery Button is available")
                gallery_visible_count += 1
                self.driver.refresh()

            refresh_count += 1
            self.driver.refresh()
            time.sleep(3)

        self.print_test_step(test_disappearing_elements_test[3])
        print(f"gallery visible times: " + str(gallery_visible_count))
        print(f"gallery not visible times: " + str(gallery_not_visible_count))
        print(f"total refresh times: " + str(refresh_count))

    def test_drag_and_drop(self):
        test_drag_and_drop_steps = {
            1: "Navigate to Drag and Drop Page",
            2: "Wait for Page to be fully Loaded. Wait 10 seconds",
            3: "Start Drag and Drop Action",
            4: "Verify if Drag and Drop Successful",
            5: "Verify that the Drag and Drop amount is the same as expected"
        }
        self.print_test_step(test_drag_and_drop_steps[1])
        self.navigate_to_url(Locator.DragAndDrop.DRAG_AND_DROP_LINK[1])
        self.print_test_step(test_drag_and_drop_steps[2])
        self.time_sleep(10)
        self.print_test_step(test_drag_and_drop_steps[3])
        self.action_drag_and_drop_from_to(Locator.DragAndDrop.source, Locator.DragAndDrop.target)
        self.print_test_step(test_drag_and_drop_steps[4])
        self.wait_until_element_visible(Locator.DragAndDrop.debit_movement_amount)
        self.print_test_step(test_drag_and_drop_steps[5])
        self.verify_text_present_in_element(Locator.DragAndDrop.debit_movement_amount, "5000")

    def test_dropdown(self):
        test_dropdown_steps = {
            1: "Navigate to Dropdown Page",
            2: "Select Item from Dropdown using value: '1' and verify.",
            3: "Select different item from dropdown. Using value: '2' and verify.",
            4: "Select item from dropdown using index: '1' and verify.",
            5: "Select different item from dropdown. Using index: '2' and verify.",
            6: "Select item from dropdown using visible text: 'Option 1' and verify.",
            7: "Select different item from dropdown. Using visible text: 'Option 2' and verify."
        }
        #   Navigate to Dropdown Page
        self.print_test_step(test_dropdown_steps[1])
        self.locate_and_click(Locator.Dropdown.DROPDOWN_LINK)
        self.print_test_step(test_dropdown_steps[2])
        self.locate_and_select_from_dropdown_by_value(Locator.Dropdown.open_dropdown_list, "1")
        self.print_test_step(test_dropdown_steps[3])
        self.locate_and_select_from_dropdown_by_value(Locator.Dropdown.open_dropdown_list, "2")
        self.print_test_step(test_dropdown_steps[4])
        self.locate_and_select_from_dropdown_by_index(Locator.Dropdown.open_dropdown_list, "1")
        self.print_test_step(test_dropdown_steps[5])
        self.locate_and_select_from_dropdown_by_index(Locator.Dropdown.open_dropdown_list, "2")
        self.print_test_step(test_dropdown_steps[6])
        self.locate_and_select_from_dropdown_by_visible_text(Locator.Dropdown.open_dropdown_list, "Option 1")
        self.print_test_step(test_dropdown_steps[7])
        self.locate_and_select_from_dropdown_by_visible_text(Locator.Dropdown.open_dropdown_list, "Option 2")

    def test_dynamic_content(self):
        test_dynamic_content_steps = {
            1: "Navigate to Dynamic Content Page",
            2: "Get 3 paragraphs and add it to a list and put it to 'old_list' ",
            3: "Refresh Page to load new paragraphs",
            4: "Get 3 paragraphs and add it to a list and put it to 'new_list' ",
            5: "Verify that old_list and new_list is not the same"
        }
        old_list = []
        new_list = []

        self.print_test_step(test_dynamic_content_steps[1])
        self.locate_and_click(Locator.DynamicContent.DYNAMIC_CONTENT_LINK)
        self.print_test_step(test_dynamic_content_steps[2])
        self.locate_and_add_to_list_element_text(Locator.DynamicContent.list_of_paragraphs_data_locator, old_list)
        self.print_test_step(test_dynamic_content_steps[3])
        self.refresh_page(8)
        self.print_test_step(test_dynamic_content_steps[4])
        self.locate_and_add_to_list_element_text(Locator.DynamicContent.list_of_paragraphs_data_locator, new_list)
        self.print_test_step(test_dynamic_content_steps[5])
        self.verify_lists_are_not_the_same(old_list, new_list)

    def test_dynamic_controls(self):
        """
        #   --- Test Remove/add Button ---
        #   Navigate to DynamicControls URL
        #   Verify that Checkbox is visible
        #   put a check on checkbox
        #   Click 'Remove' button
        #   Verify that Checkbox is no longer visible
        #   Verify element text --It's gone!-- is visible
        #   Click 'Add' button
        #   Verify that the checkbox is back
        #   Verify element text --It's back!-- is visible

        #   --- Test Enabled/disabled button ---
        #   Find and Verify Input textbox is disabled
        #   Verify Text is for enable button
        #   Click 'Enable' Button to enable Textbox
        #   Verify that the Input Textbox is now enabled
        #   Verify that the message says it is Enabled
        #   Verify  text is enabled by sending dummy text to it
        """
        test_dynamic_controls_steps = {
            1: "--- Test Remove/add Button ---",
            2: "Navigate to DynamicControls URL",
            3: "Verify that Checkbox is visible",
            4: "put a check on checkbox",
            5: "Click 'Remove' button",
            6: "Verify that Checkbox is no longer visible",
            7: "Verify element text --It's gone!-- is visible",
            8: "Click 'Add' button",
            9: "Verify that the checkbox is back",
            10: "Verify element text --It's back!-- is visible",
            11: "#   --- Test Enabled/disabled button ---",
            12: "Find and Verify Input textbox is disabled",
            13: "Verify Text is for enable button",
            14: "Click 'Enable' Button to enable Textbox",
            15: "Verify that the Input Textbox is now enabled",
            16: "Verify that the message says it is Enabled",
            17: "Verify  text is enabled by sending dummy text to it"
        }
        self.print_test_step(test_dynamic_controls_steps[1])
        self.print_test_step(test_dynamic_controls_steps[2])
        self.locate_and_click(Locator.DynamicControls.DYNAMIC_CONTROLS_LINK)
        self.print_test_step(test_dynamic_controls_steps[3])
        self.wait_until_element_visible(Locator.DynamicControls.checkbox_default, 15)
        self.print_test_step(test_dynamic_controls_steps[4])
        self.locate_and_click(Locator.DynamicControls.checkbox_default)
        self.print_test_step(test_dynamic_controls_steps[5])
        self.locate_and_click(Locator.DynamicControls.remove_or_add_button)
        self.print_test_step(test_dynamic_controls_steps[6])
        self.wait_until_element_not_visible(Locator.DynamicControls.checkbox_default, 15)
        self.print_test_step(test_dynamic_controls_steps[7])
        self.verify_text_present_in_element(Locator.DynamicControls.message, "It's gone!")
        self.print_test_step(test_dynamic_controls_steps[8])
        self.locate_and_click(Locator.DynamicControls.remove_or_add_button)
        self.print_test_step(test_dynamic_controls_steps[9])
        self.wait_until_element_visible(Locator.DynamicControls.checkbox_showing_back, 15)
        self.print_test_step(test_dynamic_controls_steps[10])
        self.verify_text_present_in_element(Locator.DynamicControls.message, "It's back!")

        self.print_test_step(test_dynamic_controls_steps[11])
        self.print_test_step(test_dynamic_controls_steps[12])
        self.verify_element_have_attribute(Locator.DynamicControls.input_text_box, 'disabled', 'true')
        self.print_test_step(test_dynamic_controls_steps[13])
        self.verify_text_present_in_element(Locator.DynamicControls.enable_or_disable_button, 'Enable')
        self.print_test_step(test_dynamic_controls_steps[14])
        self.locate_and_click(Locator.DynamicControls.enable_or_disable_button)
        self.print_test_step(test_dynamic_controls_steps[15])
        self.verify_element_does_not_have_attribute(Locator.DynamicControls.input_text_box, 'disabled')
        self.print_test_step(test_dynamic_controls_steps[16])
        self.verify_text_present_in_element(Locator.DynamicControls.message, "It's enabled!")
        self.print_test_step(test_dynamic_controls_steps[17])
        self.locate_and_send_keys(Locator.DynamicControls.input_text_box, "Test Only")
        time.sleep(5)

    def test_dynamic_loading(self):
        """
        #   Navigate to Dynamic Loading Page
        #   --- Test Element on page that is hidden ---
        #   Click Example 1: Element on page that is hidden
        #   Verify that element is not visible
        #   Verify that element is attached to the page
        #   Click button "Start"
        #   Verify Element is Visible


        #   Navigate to Dynamic Loading Page
        #   --- Test Element rendered after the fact ---
        #   Click Example 2: Element rendered after the fact
        #   Verify that element is NOT visible
        #   Verify that element is NOT attached to the page
        #   Click button "Start"
        #   Verify Element is Visible
        #   Verify Element is attached to the page

        :return:
        """

        #   Navigate to Dynamic Loading Page
        self.locate_and_click(Locator.DynamicLoading.DYNAMIC_LOADING_LINK)
        #   --- Test Element on page that is hidden ---
        #   Click Example 1: Element on page that is hidden
        self.locate_and_click(Locator.DynamicLoading.example_1)
        #   Verify that element is not visible
        self.wait_until_element_not_visible(Locator.DynamicLoading.dynamic_element_visibility, 10)
        #   Verify that element is attached to the page
        self.wait_until_element_attached_to_page(Locator.DynamicLoading.dynamic_element_visibility, 10)
        #   Click button "Start"
        self.locate_and_click(Locator.DynamicLoading.start_button)
        #   Verify Element is Visible
        self.wait_until_element_visible(Locator.DynamicLoading.dynamic_element_visibility, 30)

        #   Navigate to Dynamic Loading Page
        self.driver.get(Locator.DynamicLoading.DYNAMIC_LOADING_URL[1])
        #   --- Test Element rendered after the fact ---
        #   Click Example 2: Element rendered after the fact
        self.locate_and_click(Locator.DynamicLoading.example_2)
        #   Verify that element is NOT visible
        self.wait_until_element_not_visible(Locator.DynamicLoading.dynamic_element_visibility, 30)
        #   Verify that element is NOT attached to the page
        self.wait_until_element_not_attached_to_page(Locator.DynamicLoading.dynamic_element_visibility, 30)
        #   Click button "Start"
        self.locate_and_click(Locator.DynamicLoading.start_button)
        #   Verify Element is Visible
        self.wait_until_element_visible(Locator.DynamicLoading.dynamic_element_visibility)
        #   Verify Element is attached to the page
        self.wait_until_element_attached_to_page(Locator.DynamicLoading.dynamic_element_visibility)

    def test_entry_ad(self):
        """
        #   Navigate to Entry Ad Page
        #   Verify Entry Ad Modal is showing up
        #   Close the modal
        #   Refresh Page
        #   Verify that the modal is no longer showing up
        #   Re-enable the Ad to show on next page refresh
        #   Refresh Page
        #   Verify that the Ad is showing up again after page refresh

        :return:
        """

        #   Navigate to Entry Ad Page
        self.locate_and_click(Locator.EntryAd.ENTRY_AD_LINK)
        #   Verify Entry Ad Modal is showing up
        self.wait_until_element_visible(Locator.EntryAd.close_modal)
        time.sleep(5)
        #   Close the modal
        self.locate_and_click(Locator.EntryAd.close_modal)
        time.sleep(5)
        #   Refresh Page
        self.driver.refresh()
        #   Verify that the modal is no longer showing up
        self.wait_until_element_not_visible(Locator.EntryAd.close_modal)
        #   Re-enable the Ad to show on next page refresh
        self.locate_and_click(Locator.EntryAd.re_enable_modal)
        time.sleep(5)
        #   Refresh Page
        self.driver.refresh()
        #   Verify that the Ad is showing up again after page refresh
        time.sleep(5)
        self.wait_until_element_visible(Locator.EntryAd.close_modal)

    def test_file_download(self):
        """
        #   Navigate to File Download Link
        #   Download test_image.png
        #   Wait for few seconds for file to be downloaded
        #   Verify that the file has been downloaded successfully


        :return:
        """
        #   Navigate to File Download Link
        self.locate_and_click(Locator.FileDownload.FILE_DOWNLOAD_LINK)

        #   Download test_image.png
        time.sleep(10)
        self.locate_and_click(Locator.FileDownload.test_image_png)
        #   Wait for few seconds for file to be downloaded
        time.sleep(10)
        #   Verify that the file has been downloaded successfully
        if os.path.isfile('C:\\Users\\Administrator\\Downloads\\test_image.png'):
            print("File Download is Complete!")
        else:
            raise "File Upload FAILED!"

    def test_file_upload(self):
        """
        #   Navigate to File Upload Link
        #   Choose a File to Upload
        #   Click Upload Button
        #   Verify File Uploaded
        :return:
        """
        #   Navigate to File Upload Link
        self.locate_and_click(Locator.FileUpload.FILE_UPLOAD_LINK)
        #   Choose a File to Upload
        time.sleep(5)
        self.locate_and_send_keys(Locator.FileUpload.choose_file_to_upload_button,
                                  'C:\\Users\\Administrator\\Downloads\\test_image.png', False)
        #   Click Upload Button
        self.locate_and_click(Locator.FileUpload.submit_file_upload_button)
        #   Verify File Uploaded
        self.wait_until_element_visible(Locator.FileUpload.success_file_upload_label)

    def test_floating_menu(self):
        """
        #   Navigate to Floating Menu Link
        #   Scroll to the bottom of the page
        #   Verify that the floating menu is still visible
        :return:
        """
        #   Navigate to Floating Menu Link
        self.locate_and_click(Locator.FloatingMenu.FLOATING_MENU_LINK)
        #   Scroll to the bottom of the page
        self.actions.send_keys(Keys.END).perform()
        #   Verify that the floating menu is still visible
        time.sleep(5)
        self.wait_until_element_visible(Locator.FloatingMenu.home_floating_menu)
        self.wait_until_element_visible(Locator.FloatingMenu.news_floating_menu)
        self.wait_until_element_visible(Locator.FloatingMenu.about_floating_menu)
        self.wait_until_element_visible(Locator.FloatingMenu.contact_floating_menu)

    def test_form_authentication(self):
        """
        #   Navigate to Form Authentication Page
        #   --- Test Invalid Credentials ---
        #   Enter wrong username
        #   Enter wrong password
        #   Click submit button
        #   Verify that login failed
        #   --- Test Valid Credentials ---
        #   Enter valid username
        #   Enter wrong password
        #   Click submit button
        #   Verify that Login is Successful
        :return:
        """
        #   Navigate to Form Authentication Page
        self.locate_and_click(Locator.FormAuthentication.FORM_AUTHENTICATION_LINK)
        #   --- Test Invalid Credentials ---
        #   Enter wrong username
        self.locate_and_send_keys(Locator.FormAuthentication.username_input, 'test_wrong_username')
        #   Enter wrong password
        self.locate_and_send_keys(Locator.FormAuthentication.password_input, 'test_wrong_password')
        #   Click submit button
        self.locate_and_click(Locator.FormAuthentication.submit_button)
        #   Verify that login failed
        self.verify_text_present_in_element(Locator.FormAuthentication.info_label, 'Your username is invalid!')
        #   --- Test Valid Credentials ---
        #   Enter valid username
        self.locate_and_send_keys(Locator.FormAuthentication.username_input, 'tomsmith')
        #   Enter wrong password
        self.locate_and_send_keys(Locator.FormAuthentication.password_input, 'SuperSecretPassword!')
        #   Click submit button
        self.locate_and_click(Locator.FormAuthentication.submit_button)
        #   Verify that Login is Successful
        self.verify_text_present_in_element(Locator.FormAuthentication.info_label, 'You logged into a secure area!')

    def test_frames_nested_frames(self):
        """
        #   Navigate to Frames Page
        #   --- Test Nested Frames ---
        #   Navigate to Left Frame
        #   Verify on Left Frame
        #   Print "Left" Frame
        #   Switch to Middle Frame
        #   Verify on Middle Frame
        #   Print "Middle" Frame
        #   Switch to Right Frame
        #   Verify on Right Frame
        #   Print "Right" Frame

        :return:
        """

        #   Navigate to Frames Page
        self.locate_and_click(Locator.Frames.FRAMES_LINK)
        #   --- Test Nested Frames ---
        #   Click Nested Frame
        self.locate_and_click(Locator.Frames.nested_frames_link)
        #   Navigate to Left Frame
        time.sleep(5)
        self.driver.switch_to.frame('frame-top')
        print('switched to top')
        self.driver.switch_to.frame(Locator.Frames.name_of_left_frame[1])
        print(f'switched to: {Locator.Frames.name_of_left_frame[1]}')
        #   Verify on Left Frame
        self.verify_text_present_in_element(Locator.Frames.nested_frame_body, 'LEFT')
        #   Print "LEFT" Frame
        body_text = self.locate_and_get_text(Locator.Frames.nested_frame_body)
        print(body_text)

    def test_frames_i_frame(self):
        """
        #   --- Test iFrames ---
        #   Navigate to Frame Link
        #   Navigate iFrame Page
        #   Switch To iFrame View
        #   Type Sample Test data inside TextArea

        :return:
        """

        #   --- Test iFrames ---
        #   Navigate to Frame Link
        self.locate_and_click(Locator.Frames.FRAMES_LINK)
        #   Navigate iFrame Page
        self.locate_and_click(Locator.Frames.iframe_link)
        #   Switch To iFrame View
        self.driver.switch_to.frame(0)
        #   Type Sample Test data inside TextArea
        self.locate_and_send_keys(Locator.Frames.iframe_input, 'Testing Only', True)
        time.sleep(5)
        self.verify_text_present_in_element(Locator.Frames.iframe_input, 'Testing Only')
        time.sleep(5)

    def test_geolocation(self):
        """
        #   Navigate to Geolocation Page
        #   Click "Where am I" Button
        #   Verify Latitude have value
        #   Verify Longitude have value
        :return:
        """
        #   Navigate to Geolocation Page
        self.locate_and_click(Locator.Geolocation.GEOLOCATION_LINK)
        #   Click "Where am I" Button
        self.locate_and_click(Locator.Geolocation.where_am_i_button)
        #   Verify Latitude have value
        latitude_value = self.locate_and_get_text(Locator.Geolocation.latitude_label)
        print(latitude_value)
        #   Verify Longitude have value
        longitude_value = self.locate_and_get_text(Locator.Geolocation.longitude_value)
        print(longitude_value)

    def test_horizontal_slider(self):
        """
        #   Navigate to Horizontal Slider Page
        #   Drag and Drop Slider by offset -- x_position Until Value is 4
        :return:
        """

        #   Navigate to Horizontal Slider Page
        self.locate_and_click(Locator.HorizontalSlider.HORIZONTAL_SLIDER_LINK)
        #   Drag and Drop Slider by offset -- x_position Until Value is 4
        current_slider_value = "0"
        x_position = 0
        while current_slider_value != "4":
            current_slider_value = self.locate_and_get_text(Locator.HorizontalSlider.slider_value)
            self.actions.drag_and_drop_by_offset(self.locate_xpath(Locator.HorizontalSlider.slider),
                                                 x_position, 0).perform()
            print(f"try using x_position value is offset by: " + current_slider_value)
            x_position += 10

    def test_hovers(self):
        """
        #   Navigate to Hovers Page
        #   Verify that element is not yet showing since it is not yet hovered
        #   Hover on profile_image_1
        #   Verify that name is showing up
        :return:
        """

        #   Navigate to Hovers Page
        self.locate_and_click(Locator.Hovers.HOVERS_LINK)
        #   Verify that element is not yet showing since it is not yet hovered
        self.wait_until_element_not_visible(Locator.Hovers.name1)
        time.sleep(5)
        #   Hover on profile_image_1
        self.action_hover_on_element(Locator.Hovers.profile_image_1)
        #   Verify that name is showing up
        self.wait_until_element_visible(Locator.Hovers.name1)
        time.sleep(5)

    def test_infinite_scroll(self):
        """
        #   Navigate to Infinite Scroll Page
        #   Get Default Number of Divs Available
        #   Press KeyboardKey "End" 10 times
        #   Verify that the default number of divs available is no longer the same as current divs
        :return:
        """
        #   Navigate to Infinite Scroll Page
        self.locate_and_click(Locator.InfiniteScroll.INFINITE_SCROLL_LINK)
        #   Get Default Number of Divs Available
        divs_default_count = len(self.locate_elements_xpath(Locator.InfiniteScroll.number_of_divs))
        time.sleep(5)
        print(f"Total divs before scroll: {divs_default_count}")
        #   Press KeyboardKey "End" 10 times
        for _ in range(1, 11):
            self.actions.send_keys(Keys.END).perform()
            print(f"scroll times: {_}")
            time.sleep(2)
        #   Verify that the default number of divs available is no longer the same as current divs
        divs_after_scroll_count = len(self.locate_elements_xpath(Locator.InfiniteScroll.number_of_divs))
        print(f"Total divs after scroll: {divs_after_scroll_count}")
        assert divs_default_count != divs_after_scroll_count

    def test_inputs(self):
        """
        #   Navigate to Inputs
        #   Enter Number on InputField
        #   Verify inputted value on InputField
        :return:
        """

        #   Navigate to Inputs
        self.locate_and_click(Locator.Inputs.INPUT_PAGE_LINK)
        #   Enter Number on InputField
        self.locate_and_send_keys(Locator.Inputs.input_field, '777')
        #   Verify inputted value on InputField
        sent_key_value = self.get_attribute_value_text(Locator.Inputs.input_field)
        print(sent_key_value)
        assert '777' in sent_key_value
        time.sleep(5)

    def test_jquery_ui_menus(self):
        """
        #   Navigate to Jquery UI Menus Page
        #   Hover on menu > enabled > downloads
        #   Verify available options are PDF, CSV, Excel
        #   Click "Back to Jquery UI"
        #   Verify Page URL is "https://the-internet.herokuapp.com/jqueryui"
        :return:
        """

        #   Navigate to Jquery UI Menus Page
        self.locate_and_click(Locator.JQueryUIMenus.JQUERY_UI_MENUS_LINK)
        time.sleep(3)
        #   Hover on menu > enabled > downloads
        self.action_hover_on_element(Locator.JQueryUIMenus.menu_option_enabled)
        time.sleep(3)
        self.action_hover_on_element(Locator.JQueryUIMenus.menu_option_downloads)
        time.sleep(3)
        #   Verify available options are PDF, CSV, Excel
        self.wait_until_element_visible(Locator.JQueryUIMenus.menu_option_pdf)
        self.wait_until_element_visible(Locator.JQueryUIMenus.menu_option_csv)
        self.wait_until_element_visible(Locator.JQueryUIMenus.menu_option_excel)
        #   Click "Back to Jquery UI"
        self.locate_and_click(Locator.JQueryUIMenus.menu_option_back_to_jquery_ui)
        #   Verify Page URL is "https://the-internet.herokuapp.com/jqueryui"
        current_url = self.driver.current_url
        assert current_url == "https://the-internet.herokuapp.com/jqueryui"
        time.sleep(3)

    def test_javascript_alerts(self):
        """
        #   Navigate to JS Alert Page
        #   Click JS Alert Button
        #   Accept Alert and assert text
        #   Verify Result Label is as expected
        #   Click JS Confirm Button
        #   Click OK
        #   Verify Clicked OK
        #   Click JS Confirm Button
        #   Click Cancel
        #   Verify Clicked Cancel
        #   Click for JS Prompt
        #   Send Keys "Test Only"
        #   Verify result is "Test Only"
        :return:
        """
        #   Navigate to JS Alert Page
        self.locate_and_click(Locator.JavaScriptAlerts.JAVASCRIPT_ALERTS_LINK)
        #   Click JS Alert Button
        self.locate_and_click(Locator.JavaScriptAlerts.regular_alert)
        #   Accept Alert and assert text
        self.action_get_alert_assert_text_and_accept('I am a JS Alert')
        #   Verify Result Label is as expected
        self.verify_text_present_in_element(Locator.JavaScriptAlerts.result_label,
                                            'You successfully clicked an alert')
        #   Click JS Confirm Button
        self.locate_and_click(Locator.JavaScriptAlerts.confirm_alert)
        #   Click OK
        self.action_get_alert_assert_text_and_accept('I am a JS Confirm')
        #   Verify Clicked OK
        self.verify_text_present_in_element(Locator.JavaScriptAlerts.result_label,
                                            'You clicked: Ok')
        #   Click JS Confirm Button
        self.locate_and_click(Locator.JavaScriptAlerts.confirm_alert)
        #   Click Cancel
        self.action_get_alert_assert_text_and_dismiss('I am a JS Confirm')
        #   Verify Clicked Cancel
        self.verify_text_present_in_element(Locator.JavaScriptAlerts.result_label, 'You clicked: Cancel')
        #   Click for JS Prompt
        self.locate_and_click(Locator.JavaScriptAlerts.prompt_alert)
        #   Send Keys "Test Only"
        self.action_get_alert_assert_text_and_send_keys('Test Only', 'I am a JS prompt')
        #   Verify result is "Test Only"
        self.verify_text_present_in_element(Locator.JavaScriptAlerts.result_label, 'You entered: Test Only')

    def test_key_presses(self):
        """
        #   Navigate to Key Presses Page
        #   Enter "a" in input field
        #   Assert pressed Key
        #   Enter "1" in input field
        #   Assert pressed Key
        #   Press Key "ESCAPE" in input field
        #   Assert pressed Key


        :return:
        """
        #   Navigate to Key Presses Page
        self.locate_and_click(Locator.KeyPress.KEY_PRESS_LINK)
        #   Enter "a" in input field
        time.sleep(2)
        self.locate_and_send_keys(Locator.KeyPress.input_field, 'a')
        #   Assert pressed Key
        self.verify_text_present_in_element(Locator.KeyPress.result_label, 'You entered: A')
        #   Enter "1" in input field
        time.sleep(2)
        self.locate_and_send_keys(Locator.KeyPress.input_field, '1')
        #   Assert pressed Key
        self.verify_text_present_in_element(Locator.KeyPress.result_label, 'You entered: 1')
        #   Press Key "ESCAPE" in input field
        time.sleep(3)
        self.actions.send_keys(Keys.ESCAPE).perform()
        #   Assert pressed Key
        self.verify_text_present_in_element(Locator.KeyPress.result_label, 'ESCAPE')
        time.sleep(3)

    def test_large_and_deep_dom(self):
        """
        #   Navigate to Large and Deep DOM Page
        #   Print the last sibling's Number
        #   Verify the last sibling's Number
        #   Print the last number on Table
        #   Verify the last sibling's Number
        :return:
        """

        #   Navigate to Large and Deep DOM Page
        self.locate_and_click(Locator.LargeAndDeepDOM.LARGE_AND_DEEP_DOM_LINK)
        #   Print the last sibling's Number
        self.wait_until_element_visible(Locator.LargeAndDeepDOM.last_sibling_number)
        sibling_number = self.locate_and_get_text(Locator.LargeAndDeepDOM.last_sibling_number)
        print('last sibling number: ' + sibling_number)
        #   Verify the last sibling's Number
        assert '50.3' in sibling_number
        #   Print the last number on Table
        self.wait_until_element_visible(Locator.LargeAndDeepDOM.last_sibling_from_table)
        table_number = self.locate_and_get_text(Locator.LargeAndDeepDOM.last_sibling_from_table)
        print('last table number: ' + table_number)
        #   Verify the last sibling's Number
        assert '50.50' in table_number

    def test_multiple_window(self):
        """
        #   Navigate to Multiple windows Page
        #   Click the "Click Here" link to open new window
        #   Move to the new window
        #   Verify New window is created
        :return:
        """

        #   Navigate to Multiple windows Page
        self.locate_and_click(Locator.MultipleWindows.MULTIPLE_WINDOWS_PAGE_LINK)
        #   Click the "Click Here" link to open new window
        self.locate_and_click(Locator.MultipleWindows.open_new_window_link)
        time.sleep(5)
        #   Move to the new window
        self.switch_to_window_tab(1)
        #   Verify New window is created
        self.verify_current_url('https://the-internet.herokuapp.com/windows/new')
        time.sleep(5)

    def test_notification_message(self):
        """
        #   Navigate to Notification Message Page
        #   Get Notification Message
        #   Click "Click here" link to load new message and keep clicking until new message is loaded

        :return:
        """

        print("Navigate to Notification Message Page")
        self.locate_and_click(Locator.NotificationMessage.NOTIFICATION_MESSAGE_PAGE_LINK)
        print("Get Notification Message")
        notification_message = self.locate_and_get_text(Locator.NotificationMessage.notification_message)
        print("Click \"Click here\" link to load new message and keep clicking until new message is loaded")
        refresh_count = 1
        while True:
            self.locate_and_click(Locator.NotificationMessage.load_new_notification_message_link)
            time.sleep(3)
            new_message = self.locate_and_get_text(Locator.NotificationMessage.notification_message)
            if notification_message != new_message:
                print(new_message)
                print(f"Loaded different message successfully. \n Old message: {notification_message} \n"
                      f"New message: {new_message}")
                break
            else:
                print(new_message)
                print(f"Message still the same. Try again. Refresh count: {refresh_count}")
                refresh_count += 1

    def test_redirect_link(self):
        """
        #   --- Navigate to redirect link ---
        #   --- click 'here' link to redirect to status codes page ---
        #   --- Verify page url is 'https://the-internet.herokuapp.com/status_codes' ---

        :return:
        """
        print("--- Navigate to redirect link ---")
        self.locate_and_click(Locator.RedirectLink.REDIRECT_PAGE_LINK)
        print("--- click 'here' link to redirect to status codes page ---")
        self.locate_and_click(Locator.RedirectLink.redirect_trigger_link)
        print("--- Verify page url is 'https://the-internet.herokuapp.com/status_codes' ---")
        self.verify_current_url("https://the-internet.herokuapp.com/status_codes")
        time.sleep(5)

    def test_shifting_content(self):
        """
        #   --- Navigate to Shifting Content Page ---
        #   --- Click on Example 1: Menu Element ---
        #   --- Get "Gallery" Nav current position
        #   --- Refresh Page and Keep refreshing until new position is generated ---
        :return:
        """

        print("#   --- Navigate to Shifting Content Page ---")
        self.locate_and_click(Locator.ShiftingContent.SHIFTING_CONTENT_PAGE_LINK)
        print("#   --- Click on Example 1: Menu Element ---")
        self.locate_and_click(Locator.ShiftingContent.example_1_link)
        print("#   --- Get 'Gallery' Nav current position")
        old_location = self.get_element_location(Locator.ShiftingContent.nav_gallery)
        print("#   --- Refresh Page and Keep refreshing until new position is generated ---")
        refresh_count = 0
        while True:
            new_location = self.get_element_location(Locator.ShiftingContent.nav_gallery)
            if old_location == new_location:
                print(f"Old location is the same as New Location. Refresh the page and try again.")
                refresh_count += 1
                print(f"Refresh count: {refresh_count}")
                self.driver.refresh()
                time.sleep(5)
            else:
                print("Old location is not the same as New Location.")
                print(f"Old Location: {old_location}")
                print(f"New Location: {new_location}")
                return False

    def test_sortable_data_tables(self):
        """
        # --- Navigate to Sortable Data Tables Page ---
        # --- Get All Last Names and save as default_list ---
        # --- Sort the 'default_list' ---
        # --- Click Table Header 'Last Name' to sort the table via Last Name ---
        # --- Get All Last Names and save as sorted_list ---
        # --- Verify that the sorted default_list is the same as sorted_list ---
        :return:
        """

        # --- Navigate to Sortable Data Tables Page ---
        print("# --- Navigate to Sortable Data Tables Page ---")
        self.locate_and_click(Locator.SortableDataTables.SORTABLE_DATA_TABLES_PAGE_LINK)
        time.sleep(5)
        print("# --- Get All Last Names and save as default_list ---")
        default_list = []
        last_names = self.locate_elements_xpath(Locator.SortableDataTables.get_all_last_names)
        for last_name in last_names:
            print(f"Added to default_list: {last_name.text}")
            default_list.append(last_name.text)
        print(f"unsorted default_list: {default_list}")
        print("# --- Sort the 'default_list' ---")
        default_list.sort()
        print(f"sorted default_list: {default_list}")
        print("# --- Click Table Header 'Last Name' to sort the table via Last Name ---")
        self.locate_and_click(Locator.SortableDataTables.sort_by_last_name)
        print("# --- Get All Last Names and save as sorted_list ---")
        sorted_list = []
        last_names = self.locate_elements_xpath(Locator.SortableDataTables.get_all_last_names)
        for last_name in last_names:
            print(f"Added to sorted_list: {last_name.text}")
            sorted_list.append(last_name.text)
        print("# --- Verify that the sorted default_list is the same as sorted_list ---")
        assert default_list == sorted_list
        print("Sort descending success")
        print(f"Data of sorted_list: {sorted_list}")
        print(f"sorted default_list: {default_list}")

    def test_wysiwyg_editor(self):
        """
        #   --- Navigate to WYSIWYG Editor Page ---
        #   --- Switch to iFrame ---
        #   --- Enter "Test Only" on Editor ---
        #   --- Verify entered data is "Test Only" ---

        :return:
        """

        print("#   --- Navigate to WYSIWYG Editor Page ---")
        self.locate_and_click(Locator.WYSIWYGEditor.WYSIWYG_PAGE_LINK)
        print("#   --- Switch to iFrame ---")
        self.driver.switch_to.frame('mce_0_ifr')
        print("#   --- Enter 'Test Only' on Editor ---")
        self.locate_and_click(Locator.WYSIWYGEditor.input_field)
        time.sleep(5)
        self.locate_and_send_keys(Locator.WYSIWYGEditor.input_field, "Test Only")
        print("#   --- Verify entered data is 'Test Only' ---")
        time.sleep(10)
        self.verify_text_present_in_element(Locator.WYSIWYGEditor.input_field, "Test Only")


















