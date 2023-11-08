import tkinter

window=tkinter.Tk()
window.title("VÜCUT KİTLE İNDEKSİ HESAPLA")
window.geometry("400x500")
window.config(padx=30,pady=50)

my_weigth=tkinter.Label(text="Lütfen Kilonuzu Giriniz()kg !",font=("Arial",10,"bold"))
my_weigth.pack()
my_weigthEntry=tkinter.Entry(font=("Arial",15,"bold"))
my_weigthEntry.pack()
my_height=tkinter.Label(text="Lütfen Boyunuzu Gİriniz(cm)!",font=("Arial",10,"bold"))
my_height.pack()
my_heightEntry=tkinter.Entry(font=("Arial",15,"bold"))
my_heightEntry.pack()

my_result=tkinter.Label()
my_emomji=tkinter.Label()
def Result():
    try:
        a=float(my_weigthEntry.get())
        b=float(my_heightEntry.get())
        bmi=a/(b/100)**2
        print(bmi)
        if bmi<=18.5:
            my_result.config(text="İdeal kilonun \naltında(ZAYIF)",bg="white",fg="black",font=("Arial",20,"bold"))
            my_result.pack()
            my_emomji.config(text="\U0001F44E", font=("Arial", 90, "bold"))
            my_emomji.pack()
        elif bmi>18.5 and bmi<25:
            my_result.config(text="İdeal kiloda(NORMAL)",bg="white",fg="green",font=("Arial",20,"bold"))
            my_result.pack()
            my_emomji.config(text="\U0001F44D \U0001F609\U0001F60E",font=("Arial",50,"bold"),bg="yellow")
            my_emomji.pack()
        elif bmi>=25 and bmi<30:
            my_result.config(text="İdeal kilonun üstünde(KİLOLU)",bg="white",fg="#f58442",font=("Arial",15,"bold"))
            my_result.pack()
            my_emomji.config(text="\U0001F610\U0001F92B",bg="yellow", font=("Arial", 50, "bold"))
            my_emomji.pack()
        elif bmi>=30 and bmi<35:
            my_result.config(text="İdeal kilonun \nçok üstünde (OBEZ)",bg="white",fg="red",font=("Arial",15,"bold"))
            my_result.pack()
            my_emomji.config(text="😥 ", font=("Arial", 50, "bold"))
            my_emomji.pack()
        elif bmi>=35:
            my_result.config(text="İdeal kilonun \naşırı üstünde (MORBİD OBEZ)",bg="white",fg="red",font=("Arial",15,"bold"))
            my_result.pack()
            my_emomji.config(text="\U0001F631", font=("Arial", 30, "bold"))
            my_emomji.pack()

    except ValueError:
        my_result.config(text="Lütfen Geçerli Kilo ve Boy \nDeğeri Giriniz!!!", fg="red", font=("Arial",15, "bold"))
        my_result.pack()


result=tkinter.Button(text="HESAPLA",command=Result ,font=("Arial",20,"bold"))
result.pack()





window.mainloop()


