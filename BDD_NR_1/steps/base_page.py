from steps.browser import Browser


class Base_page(Browser):
    def check_error_message(self, by, selector, expected_error_message):
        actual_error_message = self.chrome.find_element(by, selector).text
        assert expected_error_message in actual_error_message, f'Error, expected {expected_error_message}, but got {actual_error_message} instead'