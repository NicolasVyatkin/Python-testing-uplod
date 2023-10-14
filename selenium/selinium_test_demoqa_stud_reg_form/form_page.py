# from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import os
# from datetime import time
from base_page import BasePage
from form_page_locators import FormPageLocators as Locators
from generator.generator import generated_person, generated_file


class FormPage(BasePage):
    """class that worcks with curent page"""

    def fill_fields_and_submit(self):
        """function that finds elements by locator and make a action"""
        ###
        person = generated_person()
        path = generated_file()
        # first_name = 'Kolin'
        # last_name = 'Xend'
        # email = 'somemail@somewhere.com'
        # mobile_phone = '5675675757'
        # subject_text = 'English'
        # adress = 'Somewhere, 99775, OGA'
        ###
        self.remove_footer()
        self.element_is_visible(
            Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile_phone)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        ###
        # self.element_is_visible(Locators.FILE_INPUT).send_keys(
        #     r'G:\Python\PycharmProjects\selenium\selinium_test_demoqa_stud_reg_form\test.txt')
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(Locators.CURRENT_ADRESS).send_keys(
            person.current_adress)
        self.element_is_visible(Locators.SUBMIT).click()
        # time.sleap(10)
        # return first_name, last_name, email
        return person

    def from_result(self):
        """function that saves data to the list"""
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        # for i in result_list:
        #     result_text.append(i.text)

        return result_text
