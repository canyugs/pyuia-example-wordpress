from pyuia.robot import BasePageLibrary
from wpauto import android

class SignInScreen(BasePageLibrary):

     _page_class_android = android.SignInScreen

     def __init__(self):
         BasePageLibrary.__init__(self, 'WordPress')

     def should_be_on_sign_in_screen(self):
         self._page_object.assert_on_this_page()

     def sign_in(self, username, password):
         self._page_object.sign_in(username, password)


