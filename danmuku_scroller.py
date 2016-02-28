import sys
from PySide.QtCore import *
from PySide.QtGui import *
import platform
import time
import threading
import copy


class RightScroller(QWidget):

    # 测试用，可删
    speaker = Signal(int, str, str)

    def __init__(self, x, y, wid, hgt, font_size, interval, is_top, parent=None):
        QWidget.__init__(self, parent)
        # 获得屏幕宽高
        screen = QDesktopWidget().availableGeometry(-1)
        self.__screen_width = screen.width()
        self.__screen_height = screen.height()
        # 窗口位置和大小
        self.__window_width = 250
        self.__window_height = self.__screen_height
        if wid > 0:
            self.__window_width = wid
        if hgt > 0:
            self.__window_height = hgt
        self.__window_pos_x = self.__screen_width - self.__window_width
        self.__window_pos_y = self.__screen_height - self.__window_height
        if x > 0:
            self.__window_pos_x = x
        if y > 0:
            self.__window_pos_y = y
        # QGraphicsView
        self.__view = QGraphicsView()
        self.__view.setGeometry(self.__window_pos_x, self.__window_pos_y, self.__window_width, self.__window_height)
        self.__view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        if is_top is True:
            self.__view.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow | Qt.WindowStaysOnTopHint)
        else:
            self.__view.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.__view.setAttribute(Qt.WA_TranslucentBackground, True)
        self.__view.setStyleSheet("background: transparent; border: 0px;")
        # self.__view.setStyleSheet("background: transparent;")
        self.__view.setContentsMargins(0, 0, 0, 0)
        # QGraphicsTextItem 相关
        self.__font = QFont()
        if 'Windows' in platform.system():
            self.__font = QFont("微软雅黑", font_size, QFont.Normal)
        else:
            self.__font.setPointSize(font_size)
        # QGraphicsScene
        self.__scene = QGraphicsScene()
        self.__scene.setSceneRect(0, 0, self.__window_width, self.__window_height)
        self.__scene.setBackgroundBrush(QBrush(QColor(0, 0, 0, 96)))
        # self.__back_palette = QPalette()
        # self.__back_palette.setColor(QPalette.Background, QColor(255, 0, 0, 64))
        # self.__view.setPalette(self.__back_palette)
        # 动画相关
        # self.__isscrolling = False
        self.__anime_and_timelines = {}
        self.__last_timer = None
        self.__tobe_remove_items = []
        self.__update_interval = 20
        if interval > 0:
            self.__update_interval = interval
        self.__items_tobe_add = []
        self.__mutex = threading.Lock()
        # self.__last_added_item = None

    def start(self):
        self.__view.setScene(self.__scene)
        self.__view.show()
        print("侧边栏已启用")

    def stop(self):
        items_to_remove = self.__scene.items()
        for item in items_to_remove:
            if item in self.__scene.items():
                self.__scene.removeItem(item)

    def __scroll(self):
        # if self.__isscrolling is False:
            # print(self.__scene.itemsBoundingRect())
        rect = self.__scene.itemsBoundingRect()
        right_buttom_y = rect.y() + rect.height()
        if right_buttom_y > self.__window_height:
            # self.__isscrolling = True
            # rect = self.__scene.itemsBoundingRect()
            # right_buttom_y = rect.y() + rect.height()
            right_buttom_x = rect.x() + rect.width()
            buttom_item = self.__scene.itemAt(QPoint(right_buttom_x - 1, right_buttom_y - 1))
            scroll_height = buttom_item.y() - self.__window_height + buttom_item.boundingRect().height()
            # print(buttom_item.toPlainText())
            # print(scroll_height)
            # print(str(self.__window_height))
            self.__last_timer = None
            for item in self.__scene.items():
                animation = QGraphicsItemAnimation()
                animation.setItem(item)
                after_scroll_pos_y = item.y() - scroll_height
                if after_scroll_pos_y < 0:
                    animation.setScaleAt(1, 0, 0)
                    self.__tobe_remove_items.append(item)
                else:
                    animation.setPosAt(1, QPointF(0, after_scroll_pos_y))
                timer = QTimeLine(500)
                timer.setLoopCount(1)
                # timer.setFrameRange(0, 500)
                timer.setUpdateInterval(self.__update_interval)
                timer.setCurveShape(QTimeLine.LinearCurve)
                animation.setTimeLine(timer)
                self.__anime_and_timelines[timer] = animation
                self.__last_timer = timer
                timer.start()
            if self.__last_timer is not None:
                self.__last_timer.finished.connect(self.__after_scrolling)

    def __after_scrolling(self):
        # if self.__isscrolling is True:
        timers = self.__anime_and_timelines.keys()
        for timer in timers:
            self.__anime_and_timelines[timer].setStep(1)
            self.__anime_and_timelines[timer].clear()
            self.__anime_and_timelines[timer].deleteLater()
            timer.deleteLater()
        self.__anime_and_timelines = {}
        for item in self.__tobe_remove_items:
            if item in self.__scene.items():
                self.__scene.removeItem(item)
        self.__tobe_remove_items = []
        # self.__isscrolling = False
        # self.__scroll()
        self.__mutex.release()
        if len(self.__items_tobe_add) > 0:
            self.add_one_comment(-1, None, None)

    @Slot(int, str, str)
    def add_one_comment(self, msg_type, speaker, comment):
        if msg_type == 2:
            return
        if msg_type == 0 or msg_type == 1:
            # QGraphicsTextItem
            new_text_item = QGraphicsTextItem()
            new_text_item.setFont(self.__font)
            new_text_item.setTextWidth(self.__window_width)
            new_text_item.document().setDocumentMargin(0)
            # html
            # text_html = '<div style="background:rgba(0,0,0,96);">'
            text_html = '<div">'
            if msg_type == 0:
                text_html += '<span style="color:#FFFF00;">' + speaker + '</span>'
            elif msg_type == 1:
                text_html += '<span style="color:#FF0000;">' + speaker + '</span>'
            text_html += '<span style="color:#FFFFFF;">' + comment + '</span></div>'
            new_text_item.setHtml(text_html)
            self.__items_tobe_add.append(new_text_item)
        # 瞬间多条弹幕，需要处理一下
        if self.__mutex.acquire(0):
            for item in self.__items_tobe_add:
                if len(self.__scene.items()) > 0:
                    upper_y = self.__scene.itemsBoundingRect().y() + self.__scene.itemsBoundingRect().height()
                else:
                    upper_y = self.__window_height
                item.setPos(0, upper_y)
                self.__scene.addItem(item)
                self.__items_tobe_add.pop(self.__items_tobe_add.index(item))
                # self.__last_added_item = new_text_item
                # self.__item_tobe_add.append(new_text_item)
                # if self.__isscrolling is False:
                #     for item in self.__item_tobe_add:
                #         self.__scene.addItem(item)
                #     self.__item_tobe_add = []
            # self.__last_added_item = self.__items_tobe_add[-1]
            self.__scroll()

    def test(self):
        while True:
            time.sleep(1)
            print(len(self.__scene.items()))
            self.speaker.emit(1, "欢迎老爷 ", " 进入直播间adsadsadssadad")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scroller = RightScroller(100, 50, 250, 800, 14, 20, True)
    scroller.start()
    scroller.speaker.connect(scroller.add_one_comment)
    threading.Thread(target=scroller.test).start()
    sys.exit(app.exec_())


