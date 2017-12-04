#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import subprocess
import os
import time
import GoIshadowsocks

if __name__ == '__main__':
    print('SelectSSServer----in----')
    batcmd = 'sh netstat_pid.sh'
    res_sslocal_pid_netstat = subprocess.check_output(batcmd, shell=True)
    res_sslocal_pid_netstat = res_sslocal_pid_netstat.strip()
    if res_sslocal_pid_netstat != '':
        os.system('sudo kill ' + res_sslocal_pid_netstat)

    shadow = GoIshadowsocks.GoIshadowsocks()
    shadowsocksAccountsList = shadow.update()
    shadowsocksAccount = shadowsocksAccountsList[0]
    batcmd = 'sudo sslocal -s ' + shadowsocksAccount.server + ' -p ' + shadowsocksAccount.port + ' -l ' + '1082' + ' -k ' + shadowsocksAccount.passwd +  ' -m ' + shadowsocksAccount.lockMethod + ' -d start'
    subprocess.check_output(batcmd, shell=True)
    time.sleep(1)
    batcmd = 'sh netstat_pid.sh'
    res_sslocal_pid_netstat = subprocess.check_output(batcmd, shell=True)
    res_sslocal_pid_netstat = res_sslocal_pid_netstat.strip()
    print(res_sslocal_pid_netstat)
    #  res_sslocal = subprocess.check_output(['pgrep', 'sslocal'], stderr=subprocess.STDOUT)
    #  res_sslocal_pid = res_sslocal.split('\n')[-2]
    #  print(res_sslocal_pid)
    if res_sslocal_pid_netstat != '':
        batcmd = 'sh speedtest.sh'
        res = subprocess.check_output(batcmd, shell=True)
        #  print(res.split('\n'))
        res_json_str = res.split('\n')[1]
        res_json = json.loads(res_json_str)
        ping = res_json['ping']
        print(ping)
        os.system('sudo kill ' + res_sslocal_pid_netstat)
    print('SelectSSServer----out----')
