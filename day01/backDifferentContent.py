"""
@Time : 2021/1/8 21:13 
@Author : 孙全刚
@File : backDifferentContent.py
@Software: PyCharm
"""

import socket

# 创建socket对象
sk = socket.socket()

# 绑定ip和端口
sk.bind(('127.0.0.1', 8000))

# 监听
sk.listen()
def model1(url):
    return '欢迎访问 model1'
def model2(url):
    return '欢迎访问 model2'

list1 = [
    ('/sun', model1),
    ('/quan', model2),
]


# 等待连接
while True:
    conn, addr = sk.accept()  # 建立连接
    # 接受数据
    data = conn.recv(2048).decode('utf-8')
    url = data.split()[1]
    print(url)
    # 返回数据
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')

    func = None
    for i in list1:
        if url == i[0]:
            func = i[1]
            break

    if func:
        ret = func(url)

    else:
        ret = '404 not found'

    conn.send(ret.encode('utf-8'))
    # 断开连接
    conn.close()