#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import subprocess
import os
import time
import GoIshadowsocks
import FreessCX

if __name__ == '__main__':
    print('SelectSSServer----in----')
    shadowsocksAccountsList = []

    shadow = FreessCX.FreessCX()
    shadowsocksAccountsList += shadow.update()

    shadow = GoIshadowsocks.GoIshadowsocks()
    shadowsocksAccountsList += shadow.update()

    shadowsocksAccount = None
    select_shadow_ping = None

    for shadowsocksAccount in shadowsocksAccountsList:
        batcmd = 'sh netstat_pid.sh'
        res_sslocal_pid_netstat = subprocess.check_output(batcmd, shell=True)
        res_sslocal_pid_netstat = res_sslocal_pid_netstat.strip()
        if res_sslocal_pid_netstat != '':
            os.system('sudo kill ' + res_sslocal_pid_netstat)


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
            try:
                batcmd = 'sh speedtest.sh'
                res = subprocess.check_output(batcmd, shell=True)
                #  print(res.split('\n'))
                res_json_str = res.split('\n')[1]
                res_json = json.loads(res_json_str)
                ping = res_json['ping']
                print(ping)
                if select_shadow_ping is None:
                    select_shadow_ping = ping
                    select_shadow = shadowsocksAccount
                else:
                    if ping < select_shadow_ping:
                        select_shadow_ping = ping
                        select_shadow = shadowsocksAccount
            except subprocess.CalledProcessError as e:
                print('speedtest error')
                pass
            os.system('sudo kill ' + res_sslocal_pid_netstat)
    if select_shadow is not None:
        shadowsocksAccount = select_shadow
        batcmd = 'sudo sslocal -s ' + shadowsocksAccount.server + ' -p ' + shadowsocksAccount.port + ' -l ' + '1082' + ' -k ' + shadowsocksAccount.passwd +  ' -m ' + shadowsocksAccount.lockMethod + ' -d start'
        print(batcmd)
        subprocess.check_output(batcmd, shell=True)

    print('SelectSSServer----out----')

