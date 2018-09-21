from socket import *
from multiprocessing import Process

def deal(conn):
    recv_data = conn.recv(1024).decode('gb2312')
    print(recv_data)
    conn.send("""HTTP/1.1 200 OK \r\n\r\n
    <div style="width: 1024px; height: 350px;border: 0px solid;text-align:center;">
    <h1>补录音操作</h1>
    <h2>六位编号<input name="id" ></h2>
    <input type="submit" value="根据ID查找"></h2>
    <h2>******************************</h2>
    <h2>通话时长<input name="long" ></h2>
    <h2>录音名称<input name="name" ></h2>
    <h2><input type="submit" value="写入"></h2>
    </div>
    """.encode('gb2312'))

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('',8800))
    s.listen(1023)

    while (1):
        conn, user_info = s.accept()
        print(user_info)
        p = Process(target=deal, args=(conn,))
        p.start()
        conn.close()


if __name__ == '__main__':
    main()
