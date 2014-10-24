from pyuia.robot import BasePageLibrary
from wpauto import android

class SettingsScreen(BasePageLibrary):

     _page_class_android = android.SettingsScreen

     def __init__(self):
         BasePageLibrary.__init__(self, 'WordPress')

     def should_be_on_settings_screen(self):
         self._page_object.assert_on_this_page()

     def get_username(self):
         return self._page_object.get_username()

     def back_to_main_screen(self):
         return self._page_object.back_to_main_screen()

