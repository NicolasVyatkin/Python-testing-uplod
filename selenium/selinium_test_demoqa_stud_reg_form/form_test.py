# from pages.form_page import FormPage
# start the tests - 'python -m pytest'
from form_page import FormPage
# from save_result_to_file import WorkWithInfo


class TestFormPage:

    def test_form(self, driver):
        """function that starts the test"""
        form_page = FormPage(
            driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        # first_name, last_name, email = form_page.fill_fields_and_submit()
        person = form_page.fill_fields_and_submit()
        result = form_page.from_result()
        # print(first_name, last_name, email)
        # print(result)
        # WorkWithInfo.save_result_to_file(self, "result.txt", person)
        """checks of the result"""
        # assert f'{first_name} {last_name}' == result[0], 'the form has not been filled'
        # assert email == result[1], 'the form has not been filled'
        assert f'{person.first_name} {person.last_name}' == result[
            0], 'the form has not been filled'
        assert person.email == result[1], 'the form has not been filled'
