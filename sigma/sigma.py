import tkinter
import tkinter.font
import threading
window = tkinter.Tk()
window.title('sigma calculator')
window.geometry('400x500+100+100')

def Calculation():
    i=int(end_n.get())
    a1=nor_func.get()
    n1=int(start_n.get())
    if n1>i :
        warning_text.config(text='시작할 n 번째항이, 끝낼 n 번째항 보다 크면 안 됩니다!')
    else:
        warning_text.config(text='')
        def an(n):
            return eval(a1)
        list1=[]
        list2=[]
        sum_list=[]
        while n1 <= i :
            list1.append(an(n1))
            list2.append(n1)
            n1=n1+1
            sum_list.append(sum(list1))
        result.delete(0,'end')
        result.insert(0,sum(list1))
        warning_text.config(text=list1)
        
font=tkinter.font.Font(family="맑은 고딕", size=30, slant="italic")
image1=tkinter.PhotoImage(file="./img/sigma.png")
sigma=tkinter.Label(window,image=image1)
end_n=tkinter.Entry(window,width=10)
nor_func=tkinter.Entry(window,width=30)
varia_n=tkinter.Label(window,text='n=',font=font)
start_n=tkinter.Entry(window,width=10)
start=tkinter.Button(window,width=20,text='=',command=Calculation)
result=tkinter.Entry(window)
result_text=tkinter.Label(window,text='결과:')
warning_text=tkinter.Label(window,text='')

sigma.place(x=0,y=30)
end_n.place(x=23,y=5)
nor_func.place(x=132,y=100)
varia_n.place(x=0,y=190)
start_n.place(x=60,y=213)
start.place(x=250,y=240)
result_text.place(x=80,y=300)
result.place(x=120,y=300)
warning_text.place(x=50,y=350)

window.mainloop()