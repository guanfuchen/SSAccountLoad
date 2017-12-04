#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import subprocess

if __name__ == '__main__':
    print('SelectSSServer----in----')
    res_sslocal = subprocess.check_output(['pgrep', '--sslocal'], stderr=subprocess.STDOUT)
    res_sslocal_pid = res_sslocal.split('\n')[1]
    res = subprocess.check_output(['speedtest-cli', '--json', '--no-upload'], stderr=subprocess.STDOUT)
    res_json_str = res.split('\n')[1]
    res_json = json.loads(res_json_str)
    ping = res_json['ping']
    # res_pkill = subprocess.check_output(['pkill', res_sslocal_pid], stderr=subprocess.STDOUT)
    print('SelectSSServer----out----')
