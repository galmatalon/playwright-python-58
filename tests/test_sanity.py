import pytest
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")
class Test1(BaseTest):

    def test_01_wizards(self):
        self.wizard1_page.fill_page("Gal","Matalon","gal@gmail.com")

    def test_02_wizards(self):
        self.wizard2_page.choose_option("beginner")

    def test_03_wizards(self):
        self.wizard3_page.fill_page("Dudu", "1", "Netanya", "Italy")


