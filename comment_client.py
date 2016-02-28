import socket
import struct
import random
import time
import threading
import util


class CommentClient(object):

    def __init__(self):
        self.__CID_INFO_URL = "http://live.bilibili.com/api/player?id=cid:"
        self.__DEFAULT_COMMENT_HOST = "livecmt-1.bilibili.com"
        self.__DEFAULT_COMMENT_PORT = 788
        self.__PROTOCOL_VERSION = 1
        self.__SOCKET_RECV_BUFFER_LENGTH = 1024
        self.__connected = False
        self.__beat_thread = None
        self.__loop_count = -1

    def __get_socket_server_url(self, roomid):
        cid_info_xml = str(util.http_get(self.__CID_INFO_URL + roomid))
        start = cid_info_xml.find("<server>") + len("<server>")
        end = cid_info_xml.find("</server>", start)
        if 0 < start < end:
            socket_server_url = cid_info_xml[start:end]
            return socket_server_url
        else:
            return None

    @staticmethod
    def __send_socket_data(sock, total_len, head_len, version, action, param5=1, data=b''):
        send_data = struct.pack("!IHHII" + str(len(data)) + "s", total_len, head_len, version, action, param5, data)
        try:
            sock.send(send_data)
            # response_data = sock.recv(self.__SOCKET_RECV_BUFFER_LENGTH)
            return True
        except socket.error:
            return False

    def __send_join_room_msg(self, sock, roomid):
        userid = 100000000000000 + int(200000000000000 * random.random())
        body = ('{"roomid": ' + roomid + ', "uid": ' + str(userid) + '}').encode("utf-8")
        return self.__send_socket_data(sock, 16 + len(body), 16, self.__PROTOCOL_VERSION, 7, 1, body)

    def __send_heart_beat_msg(self, sock):
        while self.__connected:
            time.sleep(1)
            self.__loop_count += 1
            if self.__loop_count > 20 or self.__loop_count == 0:
                self.__send_socket_data(sock, 16, 16, self.__PROTOCOL_VERSION, 2)
                self.__loop_count = 0
        sock.close()
        print("与服务器的连接已关闭")

    def connect(self, roomid):
        real_roomid = util.get_real_roomid(roomid)
        socket_server_url = self.__get_socket_server_url(real_roomid)
        if socket_server_url is None:
            socket_server_url = self.__DEFAULT_COMMENT_HOST
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((socket_server_url, self.__DEFAULT_COMMENT_PORT))
            if self.__send_join_room_msg(sock, real_roomid) is True:
                self.__connected = True
                self.__beat_thread = threading.Thread(target=self.__send_heart_beat_msg, args=(sock,))
                self.__beat_thread.start()
                print("连接服务器成功！")
                return sock
        except socket.error:
            print("连接服务器失败！")
            return None

    def disconnect(self, sock):
        self.__connected = False
        # if self.__beat_thread is not None:
        #     self.__beat_thread.exit()
