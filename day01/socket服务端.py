"""
@Time : 2021/1/8 13:47 
@Author : 孙全刚
@File : socket服务端.py
@Software: PyCharm
"""

import socket

# 创建socket对象
sk = socket.socket()

# 绑定ip和端口
sk.bind(('127.0.0.1', 8000))

# 监听
sk.listen()

# 等待连接
while True:
    conn, addr = sk.accept()  # 建立连接
    # 接受数据
    data = conn.recv(2048)
    print(data)
    # 返回数据
    conn.send(b'HTTP/1.1 200 OK\r\n\r\nok')
    # 断开连接
    conn.close()