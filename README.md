PyUIA Example - WordPress
=========================

Test Case in Natural Language
-----------------------------

[`test/sigin.txt`](test/signin.txt)
```
*** Test Cases ***
Sign in with valid credentials.
    Open the app, and the sign-in screen appears.
    Sign in with a valid username and password, and the main screen appears.
    Go to 'Settings', and check if the username is correct.
    Sign out, and the sign-in screen appears again.
    [Teardown]    Close App
```

Setup
-----

 1. Clone this repository.
 2. Install [Appium](http://appium.io/getting-started.html) and start an Appium server.

    ```shell
    $ appium
    info: Welcome to Appium v1.2.1 (REV 2a4b624a708e580709006b697dc4c9c4e3007863)
    info: Appium REST http interface listener started on 0.0.0.0:4723
    info: LogLevel: debug
    ```
 
 3. Get the APK file of [WordPress for Android](https://play.google.com/store/apps/details?id=org.wordpress.android&hl=en). You can either extract the APK file from the device, or build it from [source](https://github.com/wordpress-mobile/WordPress-Android).
 4. Install [PyUIA](https://github.com/imsardine/pyuia) and [Appium client](https://github.com/appium/python-client):

   ```
    pip install pyuia
    pip install Appium-Python-Client
    ```

 5. Replace placeholders in [test/resource.txt](test/resource.txt) with your credentials and the serialno of your Android device.

    ```
    *** Variables ***
    ${username}       <USERNAME>
    ${password}       <PASSWORD>
    ${device_id}      <SERIALNO>
    ```

 6. Provide APK location in [lib/WordPress.py](lib/WordPress.py).

    ```python
    PATH_TO_WORDPRESS_APK = '/path/to/wordpress.apk'
    ```

Run the Test
------------

```shell
export VERSIONER_PYTHON_PREFER_32_BIT=yes
export PYTHONPATH=lib/
pybot --loglevel TRACE --outputdir output test/signin.txt
```

Then you will get a detailed log file like [this](https://cdn.rawgit.com/imsardine/pyuia-example-wordpress/master/output/log.html).
