# SSAccountLoad
get free shadowsocks accounts to update

---
# 相关思路

配置proxychains，将代理socks的1082端口配置为proxychains的代理，并设置proxychains为quiet模式
```bash
sudo vim /etc/proxychains.conf
socks5  127.0.0.1 1082
quiet_mode
```
运行```python SelectSSServer.py```即可，此时端口1082已经选择为最好的端口了
将socks5转换为http代理端口8119即可，此时该端口为代理端口。
```bash
sudo vim /etc/privoxy/config
forward-socks5 / 127.0.0.1:1082 .
listen-address 0.0.0.0:8119
# bash命令行中使用proxy
export https_proxy="http://127.0.0.1:8119/"
export http_proxy="http://127.0.0.1:8119/"
```
