#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('allancortezvd@gmail.com', 'zixon64GER0')

    response = session.get(url)

    if response.ok:
        print(response.content)
    else:
        print(response.content)