import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
class PAGE1:
    
    
    def __init__(self):
       root=tk.Tk()
       root.geometry("1200x660")
       root.title("HOME")
       photo = PhotoImage(file="g.png")
       photo_label = Label(image=photo,height=64,width=64)
       photo_label.place(x=100,y=15)
       root.iconbitmap(r"C:\Users\SUN IT\OneDrive\Documents\FINAL YEAR PROJECT\interface of fyp")
    
       
       def toggle_menu():
           
           def collapse_toggle_menu():
               toggle_menu_fm.destroy()
               toggle_btn.config(text='☰')
               toggle_btn.config(command=toggle_menu)
           def nextPage():
                root.destroy()
                import page2     
           def nextPage3():
               root.destroy()
               import page3    
           toggle_menu_fm=tk.Frame(root,bg='#202c61',highlightbackground='white',highlightthickness=1)
           
           home_btn=tk.Button(toggle_menu_fm,text="🏠 HOME",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white')
           home_btn.place(x=20,y=20)
           cci_btn=tk.Button(toggle_menu_fm,text="📊 CCI",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage)
           cci_btn.place(x=20,y=80)
           about_btn=tk.Button(toggle_menu_fm,text="☎ ABOUT US",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage3)
           about_btn.place(x=20,y=140)
           
           #window_height=root.winfo_height() 
           toggle_menu_fm.place(x=0,y=70,height=511,width=200)
           toggle_btn.config(text='X',font=('Arial Bold',20))
           toggle_btn.config(command=collapse_toggle_menu)
       head_frame=tk.Frame(root, bg='#202c61',
                           highlightbackground='black',highlightthickness=1)
       
       
       
       
       photo = PhotoImage(file="g.png")
       varun_label = Label(head_frame,image=photo,height=64,width=64)
       varun_label.place(x=53,y=0)


       toggle_btn=tk.Button(head_frame,text='☰',bg='#202c61',fg='white',font=('Arial  Bold',20),bd=0,command=toggle_menu)
       toggle_btn.pack(side=tk.LEFT)
       
       title_lb=tk.Label(head_frame,text="SENTIMEMNT ANALYSIS BASED CONSUMER CONFIDENCE INDEX COMPUTATION OF PURCHASING BEHAVIOUR", bg='#202c61',fg='white',font=('Arial Bold',13))
       title_lb.place(x=140,y=16)
       
       
       body_frame=Frame(root,bg="white",highlightbackground="black", highlightthickness=3).place(x=50,y=90,height=100,width=650)
       label_1 = tk.Label(body_frame,height=2,text="NATURAL LANGUAGE PROCESSING:",font=('Arial bold',10),bg='white',fg='black')
       label_1.place(x=60,y=95)
       label_2 = tk.Label(body_frame,height=3,text="Natural language processing (NLP) is the ability of a computer program to understand human language\n as it is spoken and written -- referred to as natural language.It is a component of artificial intelligence (AI).",font=('Arial ',10),bg='white',fg='black')
       label_2.place(x=60,y=120)
       
       
       
      
       
       
       body_frame_1=Frame(root,bg="white",highlightbackground="blue", highlightthickness=3).place(x=320,y=230,height=100,width=650)
       label_3 = tk.Label(body_frame_1,height=2,text="CONSUMER'S CONFIDENCE INDEX:",font=('Arial bold',10),bg='white',fg='black')
       label_3.place(x=325,y=235)
       label_4 = tk.Label(body_frame_1,height=3,text="The Consumer Confidence Index (CCI) is a survey, administered by The Conference Board, that\n measures how optimistic or pessimistic consumers are regarding their expected financial situation. ",font=('Arial ',10),bg='white',fg='black')
       label_4.place(x=325,y=260)
       
       
       
       body_frame_2=Frame(root,bg="white",highlightbackground="green", highlightthickness=3).place(x=50,y=390,height=100,width=650)
       label_5= tk.Label( body_frame_2,height=2,text="MACHINE LEARNING:",font=('Arial bold',10),bg='white',fg='black')
       label_5.place(x=55,y=400)
       label_6 = tk.Label( body_frame_2,height=3,text="Machine learning (ML) is a discipline of artificial intelligence (AI) that provides machines with the ability \nto automatically learn from data and past experiences while identifying patterns to make predictions\n with minimal human intervention.",font=('Arial ',10),bg='white',fg='black')
       label_6.place(x=65,y=430)
       
       
       
       
      
       
       head_frame.pack(side=tk.TOP,fill=tk.X)
       head_frame.pack_propagate(False)
       head_frame.configure(height=70)
       bottom_frame=tk.Frame(root, bg='#202c61',
                           highlightbackground='black',highlightthickness=1)
       #label_7 = tk.Label( body_frame_2,height=3,text="Contact Us: umer777375@gmail.com",font=('Arial Bold',10),bg='skyblue',fg='black')
       #label_7.place(x=60,y=590)
       
       #label_8 = tk.Label( body_frame_2,height=3,text="Contact Us: umer777375@gmail.com",font=('Arial Bold',10),bg='skyblue',fg='black')
       #label_8.place(x=60,y=590)
       bottom_frame.pack(side=tk.BOTTOM,fill=tk.X)
       bottom_frame.pack_propagate(False)
       bottom_frame.configure(height=70)
       root.mainloop()
       
   
PAGE1()       
      