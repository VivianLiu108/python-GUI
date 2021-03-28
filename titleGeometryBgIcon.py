from tkinter import *   #引入tkinter

print(TkVersion)        #8.6 (tkinter版本)
root = Tk()             #建立一個叫root的新視窗
root.title("practice")       #視窗標題
root.geometry("300x160+400+200")     #視窗大小 "X x Y" 距離螢幕左上角(400, 200)
# w = 300                                        # screenWidth = root.winfo_screenwidth()   螢幕寬度
# h = 160                                        # screenHeight = root.winfo_screenheight() 螢幕高度
# x = 400                                        # w = 300 視窗寬
# y = 200                                        # h = 160 視窗高
# root.geometry("%dx%d+%d+%d" % (w, h, x, y))    # root.geometry("{}x{}+{}+{}".format(w, h, (screenWidth - w)//2, (screenHeight - h)//2))
# // 為向下取整除
root.configure(bg="#880088") #視窗背景顏色 "#RGB" 也可直接用"yellow", "blue", ...
root.iconbitmap("logo.ico")  #左上角的icon(圖標)

root.mainloop()         #進入等待處理物件狀態
