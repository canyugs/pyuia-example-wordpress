from pyuia.robot import BasePageLibrary
from wpauto import android

class MainScreen(BasePageLibrary):

     _page_class_android = android.MainScreen

     def __init__(self):
         BasePageLibrary.__init__(self, 'WordPress')

     def should_be_on_main_screen(self):
         self._page_object.assert_on_this_page()

     def go_to_settings(self):
         self._page_object.go_to_settings()

     def sign_out(self):
         self._page_object.sign_out()

