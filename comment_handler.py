import threading
import struct
import json
from PySide.QtCore import *


class SocketDataHandler(QObject):
    speaker = Signal(int, str, str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.__SOCKET_RECV_BUFFER_LENGTH = 10240
        self.__keep_connect = True

    def __handle_data(self, data):
        data_length = len(data)
        if data_length < 16:
            print("错误的数据")
        else:
            info = struct.unpack("!ihhii" + str(data_length - 16) + "s", data)
            length = info[0]
            if length < 16:
                print("协议失败或不正确的数据")
            elif length > 16 and length == data_length:
                action = info[3] - 1
                if action == 2:
                    user_count = struct.unpack("!ihhiii", data)[5]
                    # print("人数：" + str(user_count))
                    self.speaker.emit(2,  "当前房间人数：", str(user_count))
                if action == 4:
                    msg_str = info[5].decode("utf-8")
                    msg_json = json.loads(msg_str)
                    msg_type = msg_json['cmd']
                    if msg_type == "DANMU_MSG":
                        user_id = msg_json['info'][2][0]
                        user_name = msg_json['info'][2][1]
                        comment = msg_json['info'][1]
                        # print(user_name, comment)
                        self.speaker.emit(0,  user_name + "：", comment)
                    elif msg_type == "SEND_GIFT":
                        gift_name = msg_json['data']['giftName']
                        user_name = msg_json['data']['uname']
                        user_id = msg_json['data']['uid']
                        gift_num = str(msg_json['data']['num'])
                        # print(user_name + " 赠送 " + gift_name + "*" + gift_num)
                        self.speaker.emit(1, "礼物：", user_name + " 赠送 " + gift_name + "*" + gift_num)
                    elif msg_type == "WELCOME":
                        user_id = msg_json['data']['uid']
                        user_name = msg_json['data']['uname']
                        # print("欢迎老爷 " + user_name + " 进入直播间")
                        self.speaker.emit(1, "欢迎老爷：", user_name + " 进入直播间")
            elif 16 < length < data_length:
                # 处理合并的信息
                single_data = data[0:length]
                threading.Thread(target=self.__handle_data, args=(single_data,)).start()
                remain_data = data[length:data_length]
                threading.Thread(target=self.__handle_data, args=(remain_data,)).start()

    def recv_msg_loop(self, sock):
        while self.__keep_connect:
            # 一秒钟服务器发送一次数据，所以会出现多条信息合并发送的情况
            try:
                recv_data = sock.recv(self.__SOCKET_RECV_BUFFER_LENGTH)
                threading.Thread(target=self.__handle_data, args=(recv_data,)).start()
            except ConnectionAbortedError:
                print("信息接收线程已终止")

    def stop(self):
        self.__keep_connect = False


# if __name__ == "__main__":
#     # 连接服务器
#     client = comment_client.CommentClient()
#     live_sock = client.connect("102")
#
#     danmuji = Danmuji()
#
#     if live_sock is not None:
#         # 启动屏幕弹幕绘制
#         app = QApplication(sys.argv)
#
#         wg = QWidget()
#         form = mainForm.Ui_Form()
#         form.setupUi(wg)
#         wg.show()
#         danmuji.speaker.connect(form.add_comment)
#
#         scroller = danmuku_scroller.RightScroller(-1, 500, 250, 500, 14, 30, True)
#         scroller.start()
#         danmuji.speaker.connect(scroller.add_one_comment)
#
#         recv_thread = threading.Thread(target=danmuji.recv_msg_loop, args=(live_sock,), name="recv_thread")
#         recv_thread.start()
#
#         app.exec_()
#
#         recv_thread.join()
#         client.disconnect(live_sock)
#         print("等待线程结束")
#     else:
#         print("连接不成功")
#
#     sys.exit()


