from pyuia.appium import AppiumPageObject as AppiumPO

__all__ = ['MainScreen', 'PostsScreen', 'PagesScreen', 'SettingsScreen']

ACTION_BAR_OPEN = 'Open'
ACTION_BAR_CLOSE = 'Close'
ACTION_BAR_UP = 'Up'

class ActionBar(object):

    def _action_bar(self):
        return self._driver.find_element_by_id('android:id/action_bar')

    def _action_indicator(self):
        return self._action_bar().find_element_by_class_name('android.widget.LinearLayout')

    def _action_title(self):
        return self._driver.find_element_by_id('android:id/action_bar_title') 

    def _action_menu_item(self, item):
        # werid? all menu items have the same content description 'Posts'
        xpath = "//android.widget.ListView[2]//android.widget.TextView[@text='%s']" % item
        return self._driver.find_element_by_xpath(xpath)

    def _navigation_type(self):
        indicator = self._action_indicator()

        # http://stackoverflow.com/questions/26049651/appium-unable-to-get-content-desc-attribute-data
        label = indicator.get_attribute('name') # 'content-desc' doesn't work
        if label.endswith(', Navigation up'):
            navtype = ACTION_BAR_UP
        elif label.endswith(', Open drawer'):
            navtype = ACTION_BAR_OPEN
        elif label.endswith(', Close drawer'):
            navtype = ACTION_BAR_CLOSE
        else:
            assert False, label
        return navtype, indicator

    @property
    def _title(self):
        return self._action_title().text

    def _open_navigation_drawer(self):
        navtype, indicator = self._navigation_type()
        assert navtype in [ACTION_BAR_OPEN, ACTION_BAR_CLOSE], navtype
        if navtype == ACTION_BAR_OPEN:
            indicator.click()

    def _close_navigation_drawer(self):
        navtype, indicator = self._navigation_type()
        assert navtype in [ACTION_BAR_OPEN, ACTION_BAR_CLOSE], navtype
        if navtype == ACTION_BAR_CLOSE:
            indicator.click()

class MainScreen(AppiumPO, ActionBar):

    def _menu_settings(self):
        return self._driver.find_element_by_name('Settings')

    def _context_menu_item(self, item):
        self._press_menu()
        self._log_screenshot('Context menu opened.')
        return self._driver.find_element_by_name(item)

    def _signout_accept(self):
        return self._driver.find_elements_by_name('Sign out')[1]

    def go_to_posts(self):
        self._open_navigation_drawer()
        self._action_menu_item('Posts').click()
        return self._page_object(PostsScreen)

    def go_to_pages(self):
        self._open_navigation_drawer()
        self._action_menu_item('Pages').click()
        return self._page_object(PagesScreen)

    def go_to_settings(self):
        self._press_menu()
        self._menu_settings().click()
        return self._page_object(SettingsScreen)

    def sign_out(self):
        self._context_menu_item('Sign out').click()
        self._log_screenshot('Confirmation dialog appeared.')
        self._signout_accept().click()
        from .signin import SignInScreen
        return self._page_object(SignInScreen)

class PagesScreen(AppiumPO, ActionBar):

    def assert_on_this_page(self):
        title = self._title
        assert title == 'Pages', title

class PostsScreen(AppiumPO, ActionBar):

    def assert_on_this_page(self):
        title = self._title
        assert title == 'Posts', title

class SettingsScreen(AppiumPO, ActionBar):

    def _username_label(self):
        xpath = "//android.widget.TextView[@text='Username']/following-sibling::android.widget.TextView"
        return self._driver.find_element_by_xpath(xpath)

    def assert_on_this_page(self):
        title = self._title
        assert title == 'Settings', title

    def get_username(self):
        return self._username_label().text

    def back_to_main_screen(self):
        self._action_indicator().click()
        return self._page_object(MainScreen)

