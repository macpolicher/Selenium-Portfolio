import time
import pytest

import PageLocators.Locator as Pl
from CommonPackage.CommonActions import GlobalCommonActions

ga = GlobalCommonActions()


@pytest.fixture(autouse=True)
def open_browser_and_go_to_base_url(set_up_configuration):
    ga.driver.get(Pl.CommonData.BASE_URL)
    print("Navigate to BaseURL")


@pytest.fixture(scope="class")
def set_up_configuration():
    print("\nTHIS IS A SETUP CONFIGURATION!")

    yield
    print("\nTHIS IS A TEARDOWN CONFIGURATION!")
    ga.driver.quit()
    # ga.navigate_to_base_url()






