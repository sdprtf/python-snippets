#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path



agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers0 = {
    "Host": "www.itouzi.com",
    "Referer": "https://www.itouzi.com/login",
    'User-Agent': agent}

headers1 = {
    "Host": "www.itouzi.com",
    "Referer": "https://www.itouzi.com/user",
    'User-Agent': agent}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie can't load")

def isLogin():
    url = "https://www.itouzi.com/user"
    login_res = session.get(url, headers=headers0, allow_redirects=False)
    if login_res.status_code == 200:
        pattern = r'"user_id": "(.*?)",'
        user_id = re.findall(pattern, login_res.text)[0]
        return user_id
    else:
        return False


def login(secret, account):
    res = session.get("https://www.itouzi.com/login", headers=headers0, verify = False)
    session.cookies.save()
    pattern = r"window.login_ct = '(.*?)'"
    itz_csrftoken = re.findall(pattern, res.text)[0].replace("&amp;","&")
    headers = {
        "Host": "www.itouzi.com",
        "Referer": "https://www.itouzi.com/login",
        'User-Agent': agent,
        "itz-csrftoken": itz_csrftoken}
    post_url = 'https://www.itouzi.com/user/ajax/login'
    postdata = {
        'password': secret,
        'username': account,
        'valicode': "",
        'remember_me': 1
    }
    login_page = session.post(post_url, data=postdata, headers=headers, verify = False)
    login_code = login_page.json()
    print login_code['data']["user_id"]
    session.cookies.save()
    login_page = session.post("https://www.itouzi.com/user/ajax/doSign", data=dict(user_id=login_code['data']["user_id"]), headers=headers1, verify=False)
    login_code = login_page.json()
    print login_code

try:
    input = raw_input
except:
    pass


if __name__ == '__main__':
    user_id = isLogin()
    if user_id:
        login_page = session.post("https://www.itouzi.com/user/ajax/doSign", data=dict(user_id=user_id), headers=headers1, verify=False)
        login_code = login_page.json()
        print login_code
    else:
        login("ouck7274", "sdprtf")
