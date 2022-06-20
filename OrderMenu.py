import tkinter as tk

from tkinter import messagebox
from openpyxl import load_workbook
from datetime import datetime

price = {'에스프레소' : 2000, '아메리카노' : 2500, '카페라떼' : 4500, '카페모카' : 4500 ,
         '바닐라라떼' : 4500, '더치라떼' : 4500}
order = []
order2 = {'에스프레소' : 0, '아메리카노' : 0, '카페라떼' : 0, '카페모카' : 0 ,
         '바닐라라떼' : 0, '더치라떼' : 0}
sum = 0

def clear():
    global sum, order, order2, textarea, entry1, entry2
    textarea.delete('1.0', tk.END)
    label1['text'] = "금액: 0원"
    sum = 0
    order= []
    order2 = {'에스프레소' : 0, '아메리카노' : 0, '카페라떼' : 0, '카페모카' : 0 ,
         '바닐라라떼' : 0, '더치라떼' : 0}
    entry1.delete('0', tk.END)
    entry2.delete('0', tk.END)
    entry1.focus()

def add(item):
    global sum
    
    if item not in price:
        print("no drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    order2[item] += 1
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "금액: " + str(sum) + "원"
   
def send():
    global order, order2, sum, entry1, entry2
    name = str(entry1.get())
    hp = str(entry2.get())
    print(name, hp)
    print(order)
    print(order2)
    
    now_dt = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    wb = load_workbook("drink_order.xlsx")
    ws = wb['Sheet1']
    ws.append([now_dt, name, hp, order2['에스프레소'],order2['아메리카노'], order2['카페라떼'], 
               order2['카페모카'], order2['바닐라라떼'], order2['더치라떼'], sum])
    wb.save('drink_order.xlsx')
    
    clear()
 
def btn_exit():
    name = str(entry1.get())
    hp = str(entry2.get())
    
    if name == "":
        tk.messagebox.showerror("확인", "이름을 입력해주세요!")
        entry1.focus()
        return
    if hp == "":
        tk.messagebox.showerror("확인", "휴대폰번호를 입력해주세요!")
        entry2.focus()
        return
    
    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        send()


window = tk.Tk()
window.title("음료 주문")
window.geometry("470x550")

frame1 = tk.Frame(window)
frame1.pack()

btn_1 = tk.Button(frame1, text="에스프레소 ", command=lambda : add('에스프레소'), width = 16, height = 3)
btn_2 = tk.Button(frame1, text="아메리카노", command=lambda : add('아메리카노'), width = 16, height = 3)
btn_3 = tk.Button(frame1, text="카페라떼", command=lambda : add('카페라떼'), width = 16, height = 3)
btn_4 = tk.Button(frame1, text="카페모카", command=lambda : add('카페모카'), width = 16, height = 3)
btn_5 = tk.Button(frame1, text="바닐라라떼", command=lambda : add('바닐라라떼'), width = 16, height = 3)
btn_6 = tk.Button(frame1, text="더치라떼", command=lambda : add('더치라떼'), width = 16, height = 3)
btn_7 = tk.Button(frame1, text="주문 완료", command = btn_exit, width = 10, height = 2)

btn_1.grid(row = 0, column = 0, padx = 10, pady = 10)
btn_2.grid(row = 0, column = 1, padx = 10, pady = 10)
btn_3.grid(row = 0, column = 2, padx = 10, pady = 10)
btn_4.grid(row = 2, column = 0, padx = 10, pady = 10)
btn_5.grid(row = 2, column = 1, padx = 10, pady = 10)
btn_6.grid(row = 2, column = 2, padx = 10, pady = 10)
btn_7.grid(row = 4, column = 1, padx = 10, pady = 10)

label4 = tk.Label(frame1, text = "2,000원", width = 16, height = 1).grid(row = 1, column=0)
label5 = tk.Label(frame1, text = "2,500원", width = 16, height = 1).grid(row = 1, column=1)
label6 = tk.Label(frame1, text = "4,500원", width = 16, height = 1).grid(row = 1, column=2)
label7 = tk.Label(frame1, text = "4,500원", width = 16, height = 1).grid(row = 3, column=0)
label8 = tk.Label(frame1, text = "4,500원", width = 16, height = 1).grid(row = 3, column=1)
label9 = tk.Label(frame1, text = "4,500원", width = 16, height = 1).grid(row = 3, column=2)

frame2 = tk.Frame(window)
frame2.pack()

label2 = tk.Label(frame2, text = "이름", width = 10, height = 2).grid(row = 0, column=0)
label3 = tk.Label(frame2, text = "휴대폰번호", width = 10, height = 2).grid(row = 1, column=0)

entry1 = tk.Entry(frame2)
entry2 = tk.Entry(frame2)
entry1.grid(row=0, column = 1)
entry2.grid(row=1, column=1)

label1 = tk.Label(window, text = "금액: 0원", width = 100, height = 2, fg = "blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack(padx = 10, pady = 10)

window.mainloop()
