from steps.base_page import Base_page


class Basic_Auth(Base_page):

    def check_current_url(self):
        expected_url = "https://the-internet.herokuapp.com/basic_auth"
        actual_url = self.chrome.current_url
        assert expected_url == actual_url, f"Expected {expected_url}, but got {actual_url} instead"