from appium import webdriver
from pyuia.robot import BaseAppLibrary, BasePageLibrary
from pyuia.appium import AppiumContext

__all__ = ['WordPress', 'WPPageLibrary']

class WordPress(BaseAppLibrary):

    def _init_context(self, device_id):
        return AppiumContext(self._init_driver(device_id))

    def _init_driver(self, device_id):
        desired_caps = {
            'udid': device_id,
            'deviceName': 'My Phone',
            'platformName': 'Android',
            'platformVersion': '4.3',
            'app': '/path/to/wordpress.apk',
            'appPackage': 'org.wordpress.android',
            'appActivity': '.ui.posts.PostsActivity',
            'appWaitActivity': '.ui.accounts.WelcomeActivity',
            'newCommandTimeout': 10 * 60,
        }

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(3)
        return driver

class WPPageLibrary(BasePageLibrary):

    def __init__(self):
        BasePageLibrary.__init__(self, 'WordPress')

