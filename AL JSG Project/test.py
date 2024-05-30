import sys
import os
from collections import Counter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

# 현재 스크립트의 디렉터리를 지정해주는 코드
script_dir = os.path.dirname(os.path.abspath(__file__))

# 파일의 경로를 지정해주는 코드
orderui = os.path.join(script_dir, "ordermenu.ui")
orderlistui = os.path.join(script_dir, "orderlist.ui")
adminui = os.path.join(script_dir, "admin.ui")
loginui = os.path.join(script_dir, "login.ui")
totalui = os.path.join(script_dir, "total.ui")
paidui = os.path.join(script_dir, "Paid.ui")
b1 = os.path.join(script_dir, "ramen.png")
b2 = os.path.join(script_dir, "udong.png")
b3 = os.path.join(script_dir, "kimchiudong.png")
b4 = os.path.join(script_dir, "dongas.png")
b5 = os.path.join(script_dir, "sundubu.png")
b6 = os.path.join(script_dir, "kimchizzige.png")
b7 = os.path.join(script_dir, "jjolmen.png")
b8 = os.path.join(script_dir, "toboki.png")
b9 = os.path.join(script_dir, "jeyouk.png")

# 파일 로드를 위한 코드
form_class_order, base_class = uic.loadUiType(orderui)
form_class_orderlist, base_class = uic.loadUiType(orderlistui)
form_class_admin, base_class = uic.loadUiType(adminui)
form_class_login, base_class = uic.loadUiType(loginui)
form_class_total, base_class = uic.loadUiType(totalui)
form_class_paid, base_class = uic.loadUiType(paidui)

# 음식주문 목록을 저장하기위한 리스트
order_list = []

# 분할정렬 함수로 정렬함
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 중복값 처리 함수로 중복값을 지우고 음식의 이름과 개수를 튜플형식으로 리턴하기위한 함수 (1개여도 이 과정을 거침)
def process_duplicates(arr):
    counter = Counter(arr)
    result = [(item, count) for item, count in counter.items()]
    return result

# 관리자 화면UI
class Admin_UI(QMainWindow, form_class_admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 버튼클릭시 UI를 변경하기위한 코드
        self.Order.clicked.connect(self.order_ui)
        self.Total.clicked.connect(self.total_ui)

        # 버튼클릭시 종료하기위한 코드
        self.Exit.clicked.connect(self.exit)

    # Order_UI로 가기위한 함수
    def order_ui(self):
        self.close()
        self.order = Order_UI()
        self.order.show()
    
    # Total_UI로 가기위한 함수
    def total_ui(self):
        self.close()
        self.total = Total_UI()
        self.total.show()
    
    # 프로그램 종료하는 함수
    def exit(self):
        exit()

# 관리자 화면으로 가기 위한 로그인 UI
class Login_UI(QMainWindow, form_class_login):
    PW = "1234"
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
# 버튼클릭시 UI를 변경하기위한 코드
        self.Login.clicked.connect(self.check)

# 비밀번호를 비교하여 맞으면 admin_ui함수 출력
    def check(self):
        if self.PW_Input.text() == self.PW:
            self.admin_ui()

# Admin_UI로 가기위한 함수
    def admin_ui(self):
        self.close()
        self.admin = Admin_UI()
        self.admin.show()

# 총 매출을 구하는 UI
class Total_UI(QMainWindow, form_class_total):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
# 버튼클릭시 UI를 변경하기위한 코드
        self.Admin.clicked.connect(self.admin_ui)

# Admin_UI로 가기위한 함수
    def admin_ui(self):
        self.close()
        self.admin = Admin_UI()
        self.admin.show()

# 메인 UI
class Order_UI(QMainWindow, form_class_order):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
# 음식 버튼에 아이콘 설정
        self.set_food_icon(self.food1, b1)
        self.set_food_icon(self.food2, b2)
        self.set_food_icon(self.food3, b3)
        self.set_food_icon(self.food4, b4)
        self.set_food_icon(self.food5, b5)
        self.set_food_icon(self.food6, b6)
        self.set_food_icon(self.food7, b7)
        self.set_food_icon(self.food8, b8)
        self.set_food_icon(self.food9, b9)
        
# 음식가격 라벨에 가격 입력
        self.foodLB_Pr_1.setText("4000")
        self.foodLB_Pr_2.setText("4500")
        self.foodLB_Pr_3.setText("5500")
        self.foodLB_Pr_4.setText("9000")
        self.foodLB_Pr_5.setText("6000")
        self.foodLB_Pr_6.setText("6000")
        self.foodLB_Pr_7.setText("5000")
        self.foodLB_Pr_8.setText("4500")
        self.foodLB_Pr_9.setText("8000")

# 음식 버튼 클릭 이벤트 연결
        self.food1.clicked.connect(lambda: self.add_to_order(self.foodLB1.text(), self.foodLB_Pr_1.text()))
        self.food2.clicked.connect(lambda: self.add_to_order(self.foodLB2.text(), self.foodLB_Pr_2.text()))
        self.food3.clicked.connect(lambda: self.add_to_order(self.foodLB3.text(), self.foodLB_Pr_3.text()))
        self.food4.clicked.connect(lambda: self.add_to_order(self.foodLB4.text(), self.foodLB_Pr_4.text()))
        self.food5.clicked.connect(lambda: self.add_to_order(self.foodLB5.text(), self.foodLB_Pr_5.text()))
        self.food6.clicked.connect(lambda: self.add_to_order(self.foodLB6.text(), self.foodLB_Pr_6.text()))
        self.food7.clicked.connect(lambda: self.add_to_order(self.foodLB7.text(), self.foodLB_Pr_7.text()))
        self.food8.clicked.connect(lambda: self.add_to_order(self.foodLB8.text(), self.foodLB_Pr_8.text()))
        self.food9.clicked.connect(lambda: self.add_to_order(self.foodLB9.text(), self.foodLB_Pr_9.text()))
        
# 버튼클릭시 UI를 변경하기위한 코드
        self.Orderlist.clicked.connect(self.orderlist_ui)
        self.Admin.clicked.connect(self.login_ui)
        self.Reset.clicked.connect(self.reset_order_list)
    
# 음식 버튼에 아이콘 적용
    def set_food_icon(self, button, image_path):
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(button.size())

# order_list에 클릭한 음식 이름과 가격 입력
    def add_to_order(self, food_name, price):
        order_list.append((food_name, int(price)))

# order_list를 초기화
    def reset_order_list(self):
        order_list.clear()
    
# Login_UI로 가기위한 함수
    def login_ui(self):
        self.close()
        self.login = Login_UI()
        self.login.show()
    
# Order_List_UI로 가기위한 함수
    def orderlist_ui(self):
        self.close()
        self.orderlist = Order_List_UI()
        self.orderlist.show()

# 주문 내역 UI
class Order_List_UI(QMainWindow, form_class_orderlist):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 버튼클릭시 UI를 변경하기위한 코드
        self.Order.clicked.connect(self.order_ui)
        self.Pay.clicked.connect(self.pay)

# order_list를 출력시키기위한 함수로 이동하는 코드
        self.update_order_list()
    
# 3개의 리스트창에 각각 음식이름, 주문개수, 가격을 출력하고 Total_Pr 라벨에 가격 총합계를 출력하는 함수
    def update_order_list(self):
        self.Orderlist_1.clear()
        self.Orderlist_2.clear()
        self.Orderlist_3.clear()

        sorted_list = merge_sort(order_list)                                    # 분할정렬을 하여 정렬시키고
        processed_list = process_duplicates(sorted_list)                        # 중복값을 통합하기위해 process_duplicates로 정렬된 리스트를 보냄
        totalpr=0
        for item, count in processed_list:
            food, price = item
            self.Orderlist_1.addItem(f"{food}")                                 # 음식이름 출력
            self.Orderlist_2.addItem(f"{count}개")                              # 해당음식개수 출력
            self.Orderlist_3.addItem(f"{int(count)*int(price)}원")              # 해당음식가격 출력
            self.Total_Pr.setText(f"{int(totalpr)*(int(count)*int(price))}")    # 총합계가격 출력
    
# Paid_UI로 가기위한 함수 (order_list를 초기화하기전에 텍스트파일에 총합계를 적용시키는 코드 추가예정)
    def pay(self):
        order_list.clear()
        self.paid = Paid_UI()
        self.paid.show()
        self.close()

# Order_UI로 가기위한 함수
    def order_ui(self):
        self.close()
        self.order = Order_UI()
        self.order.show()
        
# 라벨에 주문완료와 주문번호를 출력하기 위한 함수(주문번호 추가예정)
class Paid_UI(QMainWindow, form_class_paid):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
# 버튼클릭시 UI를 변경하기위한 코드
        self.Order.clicked.connect(self.order_ui)
    
    def order_ui(self):
        self.close()
        self.order = Order_UI()
        self.order.show()

# 창을 띄우기 위한 메인함수
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Order_UI()
    myWindow.show()
    sys.exit(app.exec_())
