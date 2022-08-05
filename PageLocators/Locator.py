
class CommonData:
    BASE_URL = 'https://the-internet.herokuapp.com/'


class AddRemoveElements:
    ADD_REMOVE_ELEMENTS_LINK = ["ADD_REMOVE_ELEMENTS_LINK", '//*[@href="/add_remove_elements/"]']
    add_element_button = ["add_element_button", '//*[@onclick="addElement()"]']
    delete_element_button = ["delete_element_button", '//*[@onclick="deleteElement()"]']


class BrokenImage:
    BROKEN_IMAGE_LINK = ['BROKEN_IMAGE_LINK', '//*[@href="/broken_images"]']
    all_images = ['all_images', '//*[@class="example"]/img']


class CheckBoxes:
    CHECKBOXES_LINK = ['CHECKBOXES_LINK', '//*[@href="/checkboxes"]']
    Checkbox_1 = ['Checkbox_1', '//*[@id="checkboxes"]/input[1]']
    Checkbox_2 = ['Checkbox_2', '//*[@id="checkboxes"]/input[2]']


class ContextMenu:
    CONTEXT_MENU_LINK = ['CONTEXT_MENU_LINK', '//*[@href="/context_menu"]']
    context_menu_box = ['context_menu_box', '//*[@oncontextmenu="displayMessage()"]']
    context_menu_header = ['context_menu_header', '//h3']


class DisappearingElements:
    DISAPPEARING_ELEMENTS_LINK = ['DISAPPEARING_ELEMENTS_LINK', '//*[@href="/disappearing_elements"]']
    elements_button = ['elements_button', '//li/a']
    gallery_button = ['gallery_button', '//*[@href="/gallery/"]']


class DragAndDrop:
    DRAG_AND_DROP_LINK = ['DRAG_AND_DROP_LINK', 'https://demo.guru99.com/test/drag_drop.html']
    source = ['source', '//li[2][@id="fourth"]']
    target = ['target', '//*[@id="amt7"]']
    debit_movement_amount = ['debit_movement_amount', '//*[@id="t7"]']


class Dropdown:
    DROPDOWN_LINK = ['DROPDOWN_LINK', '//*[@href="/dropdown"]']
    open_dropdown_list = ['open_dropdown_list', '//*[@id="dropdown"]']


class DynamicContent:
    #   Locators:
    DYNAMIC_CONTENT_LINK = ['DYNAMIC_CONTENT_LINK', '//*[@href="/dynamic_content"]']
    list_of_paragraphs_data_locator = ['list_of_paragraphs_data_locator', '//*[@id="content"]/div[@class="row"]/div[2]']

    #   Data and variables:
    list_of_paragraphs_data_variable = []


class DynamicControls:
    #   Locators
    DYNAMIC_CONTROLS_LINK = ['DYNAMIC_CONTROLS_LINK', '//*[@href="/dynamic_controls"]']
    checkbox_default = ['checkbox_default', '//*[@id="checkbox"]/input']
    checkbox_showing_back = ['checkbox_showing_back', '//*[@id="checkbox"]']
    remove_or_add_button = ['remove_or_add_button', '//*[@onclick="swapCheckbox()"]']
    message = ['message', '//*[@id="message"]']
    input_text_box = ['input_text_box', '//*[@id="input-example"]/input']
    enable_or_disable_button = ['enable_or_disable_button', '//*[@onclick="swapInput()"]']


class DynamicLoading:
    # Locators
    DYNAMIC_LOADING_LINK = ['DYNAMIC_LOADING_LINK', '//*[@href="/dynamic_loading"]']
    example_1 = ['example_1', '//*[@href="/dynamic_loading/1"]']
    example_2 = ['example_2', '//*[@href="/dynamic_loading/2"]']
    start_button = ['start_button', '//*[@id="start"]/button']
    dynamic_element_visibility = ['dynamic_element_visibility', '//*[@id="finish"]/h4']

    # Data
    DYNAMIC_LOADING_URL = ['DYNAMIC_LOADING_URL', 'https://the-internet.herokuapp.com/dynamic_loading']


class EntryAd:
    # Locators
    ENTRY_AD_LINK = ['ENTRY_AD_LINK', '//*[@href="/entry_ad"]']
    close_modal = ['close_modal', '//*[@class="modal-footer"]/p']
    re_enable_modal = ['re_enable_modal', '//*[@id="restart-ad"]']


class FileDownload:
    # Locators
    FILE_DOWNLOAD_LINK = ['FILE_DOWNLOAD_LINK', '//*[@href="/download"]']
    test_image_png = ['test_image_png', '//*[@href="download/test_image.png"]']
    download_directory = 'C:\\Users\\Administrator\\Downloads'


class FileUpload:
    # Locators
    FILE_UPLOAD_LINK = ['FILE_UPLOAD_LINK', '//*[@href="/upload"]']
    choose_file_to_upload_button = ['choose_file_to_upload_button', '//*[@id="file-upload"]']
    submit_file_upload_button = ['submit_file_upload_button', '//*[@id="file-submit"]']
    success_file_upload_label = ['success_file_upload_label', '//*[@id="uploaded-files"]']


class FloatingMenu:
    # Locators
    FLOATING_MENU_LINK = ['FLOATING_MENU_LINK', '//*[@href="/floating_menu"]']
    home_floating_menu = ['home_floating_menu', '//*[@href="#home"]']
    news_floating_menu = ['news_floating_menu', '//*[@href="#news"]']
    contact_floating_menu = ['contact_floating_menu', '//*[@href="#contact"]']
    about_floating_menu = ['about_floating_menu', '//*[@href="#about"]']


class FormAuthentication:
    #   Locators
    FORM_AUTHENTICATION_LINK = ['FORM_AUTHENTICATION_LINK', '//*[@href="/login"]']
    username_input = ['username_input', '//*[@id="username"]']
    password_input = ['password_input', '//*[@id="password"]']
    submit_button = ['submit_button', '//*[@type="submit"]']
    info_label = ['info_label', '//*[@id="flash"]']


class Frames:
    #   Locators
    FRAMES_LINK = ['FRAMES_LINK', '//*[@href="/frames"]']
    nested_frames_link = ['nested_frames_link', '//*[@href="/nested_frames"]']
    iframe_link = ['iframe_link', '//*[@href="/iframe"]']
    nested_frame_left = ['nested_frame_left', '//*[@src="/frame_left"]']
    nested_frame_body = ['nested_frame_body', '//body']
    iframe_view = ['iframe_view', '//*[@id="mce_0_ifr"]']
    iframe_input = ['iframe_input', '//*[@id="tinymce"]/p']

    #   Data
    name_of_left_frame = ['name_of_left_frame', 'frame-left']
    name_of_middle_frame = ['name_of_middle_frame', 'frame-middle']
    name_of_right_frame = ['name_of_right_frame', 'frame-right']


class Geolocation:
    #   Locators
    GEOLOCATION_LINK = ['GEOLOCATION_LINK', '//*[@href="/geolocation"]']
    where_am_i_button = ['where_am_i_button', '//*[@onclick="getLocation()"]']
    latitude_label = ['latitude_label', '//*[@id="lat-value"]']
    longitude_value = ['longitude_value', '//*[@id="long-value"]']


class HorizontalSlider:
    #   Locators
    HORIZONTAL_SLIDER_LINK = ['HORIZONTAL_SLIDER_LINK', '//*[@href="/horizontal_slider"]']
    slider = ['slider', '//*[@class="sliderContainer"]/input']
    slider_value = ['slider_value', '//*[@id="range"]']


class Hovers:
    #   Locators
    HOVERS_LINK = ['HOVERS_LINK', '//*[@href="/hovers"]']
    profile_image_1 = ['profile_image_1', '//*[@class="example"]/div[1]//img']
    profile_image_2 = ['profile_image_2', '//*[@class="example"]/div[2]//img']
    profile_image_3 = ['profile_image_3', '//*[@class="example"]/div[3]//img']

    name1 = ['name1', '//*[@class="example"]/div[1]//h5']
    name2 = ['name2', '//*[@class="example"]/div[2]//h5']
    name3 = ['name3', '//*[@class="example"]/div[3]//h5']


class InfiniteScroll:
    # Locators
    INFINITE_SCROLL_LINK = ['INFINITE_SCROLL_LINK', '//*[@href="/infinite_scroll"]']
    number_of_divs = ['number_of_divs', '//*[@class="jscroll-inner"]/div']


class Inputs:
    #   Locators
    INPUT_PAGE_LINK = ['INPUT_PAGE_LINK', '//*[@href="/inputs"]']
    input_field = ['input_field', '//*[@type="number"]']


class JQueryUIMenus:
    #   Locators
    JQUERY_UI_MENUS_LINK = ['JQUERY_UI_MENUS_LINK', '//*[@href="/jqueryui/menu"]']
    menu_option_enabled = ['menu_option_enabled', '//*[@id="menu"]//a[contains(text(), "Enabled")]']
    menu_option_downloads = ['menu_option_downloads', '//*[@id="menu"]//a[contains(text(), "Downloads")]']
    menu_option_pdf = ['menu_option_pdf', '//a[@href="/download/jqueryui/menu/menu.pdf"]']
    menu_option_csv = ['menu_option_csv', '//a[@href="/download/jqueryui/menu/menu.csv"]']
    menu_option_excel = ['menu_option_excel', '//*[@href="/download/jqueryui/menu/menu.xls"]']
    menu_option_back_to_jquery_ui = ['menu_option_back_to_jquery_ui', '//*[@id="menu"]//a[@href="/jqueryui"]']


class JavaScriptAlerts:
    #   Locators
    JAVASCRIPT_ALERTS_LINK = ['JAVASCRIPT_ALERTS_LINK', '//*[@href="/javascript_alerts"]']
    regular_alert = ['regular_alert', '//*[@onclick="jsAlert()"]']
    confirm_alert = ['confirm_alert', '//*[@onclick="jsConfirm()"]']
    prompt_alert = ['prompt_alert', '//*[@onclick="jsPrompt()"]']
    result_label = ['result_label', '//*[@id="result"]']


class KeyPress:
    #   Locators
    KEY_PRESS_LINK = ['KEY_PRESS_LINK', '//*[@href="/key_presses"]']
    input_field = ['input_field', '//*[@id="target"]']
    result_label = ['result_label', '//*[@id="result"]']


class LargeAndDeepDOM:
    #   Locators
    LARGE_AND_DEEP_DOM_LINK = ['LARGE_AND_DEEP_DOM_LINK', '//*[@href="/large"]']
    last_sibling_number = ['last_sibling_number', '//*[@id="sibling-50.3"]']
    last_sibling_from_table = ['last_sibling_from_table', '//*[@class="column-50"][contains(text(), "50.50")]']


class MultipleWindows:
    #   Locators
    MULTIPLE_WINDOWS_PAGE_LINK = ['MULTIPLE_WINDOWS_PAGE_LINK', '//*[@href="/windows"]']
    open_new_window_link = ['open_new_window_link', '//*[@href="/windows/new"]']


class NotificationMessage:
    #   Locators
    NOTIFICATION_MESSAGE_PAGE_LINK = ['NOTIFICATION_MESSAGE_PAGE_LINK', '//*[@href="/notification_message"]']
    notification_message = ['notification_message', '//*[@id="flash"]']
    load_new_notification_message_link = ['load_new_notification_message_link', '//*[@href="/notification_message"]']


class RedirectLink:
    #   Locators
    REDIRECT_PAGE_LINK = ['REDIRECT_PAGE_LINK', '//*[@href="/redirector"]']
    redirect_trigger_link = ['redirect_trigger_link', '//*[@id="redirect"]']


class ShiftingContent:
    #   Locators
    SHIFTING_CONTENT_PAGE_LINK = ['SHIFTING_CONTENT_PAGE_LINK', '//*[@href="/shifting_content"]']
    example_1_link = ['example_1_link', '//*[@href="/shifting_content/menu"]']
    nav_gallery = ['nav_gallery', '//*[@href="/gallery/"]']


class SortableDataTables:
    #   Locators
    SORTABLE_DATA_TABLES_PAGE_LINK = ['SORTABLE_DATA_TABLES_PAGE_LINK', '//*[@href="/tables"]']
    get_all_last_names = ['get_all_last_names', '//*[@id="table1"]//tr/td[1]']
    sort_by_last_name = ['sort_by_last_name', '//*[@id="table1"]//*[contains(text(), "Last Name")]']


class WYSIWYGEditor:
    #   Locators
    WYSIWYG_PAGE_LINK = ['WYSIWYG_PAGE_LINK', '//*[@href="/tinymce"]']
    iframe_id = ['iframe_id', '//*[@id="mce_0_ifr"]']
    input_field = ['input_field', '//*[@id="tinymce"]/p']







