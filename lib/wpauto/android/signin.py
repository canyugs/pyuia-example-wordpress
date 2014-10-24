from pyuia.appium import AppiumPageObject as AppiumPO

__all__ = ['SignInScreen']

class SignInScreen(AppiumPO):

    def _username_field(self):
        return self._driver.find_elements_by_class_name('android.widget.EditText')[0]

    def _password_field(self):
        return self._driver.find_elements_by_class_name('android.widget.EditText')[1]

    def _signin_button(self):
        return self._driver.find_element_by_name('Sign in')

    def assert_on_this_page(self):
        self._assert_visible(self._signin_button)

    def sign_in(self, username, password):
        self._username_field().send_keys(username)
        self._password_field().send_keys(password)
        self._press_back() # to reveal 'Sign in' button
        self._signin_button().click()


