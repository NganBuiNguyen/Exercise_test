import base64
import os
import urllib.parse as urlparse
from time import sleep
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from datetime import datetime
from selenium import webdriver

DRIVER = '/usr/local/bin/chromedriver/chromedriver'

def get_screenshot(request):
    """
    Take a screenshot and return a png file based on the url.
    """
    width = 1024
    height = 768

    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        if url is not None and url != '':
            driver = webdriver.Chrome(DRIVER)
            driver.get(url)
            sleep(2)
            driver.set_window_size(width, height)

            now = datetime.today()
            img_dir = os.getcwd()
            img_name = ''.join(["Screen Shot " + str(now.date().strftime('%Y-%m-%d')) + " at " + str(now.time().strftime('%H.%M.%S %p')) + '.png'])
            full_img_path = os.path.join(img_dir, img_name)
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
            driver.save_screenshot(full_img_path)
            screenshot = open(full_img_path, 'rb').read()
            screenshot = driver.get_screenshot_as_png()
            image_64_encode = base64.encodestring(screenshot)
            var_dict = {'screenshot': image_64_encode}

            driver.quit()    
            return render(request, 'home.html', var_dict)
    else:
        return HttpResponse('Error')
