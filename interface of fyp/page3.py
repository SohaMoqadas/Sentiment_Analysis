

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

class PAGE3:
    
    
    def __init__(self):
       root=tk.Tk()
       root.geometry("1200x660")
       root.title("ABOUT US")
       root.iconbitmap(r"C:\Users\SUN IT\OneDrive\Documents\interface of fyp")
    

       def toggle_menu():
           
           def collapse_toggle_menu():
               toggle_menu_fm.destroy()
               toggle_btn.config(text='☰')
               toggle_btn.config(command=toggle_menu)
              
           def nextPage():
               root.destroy()
               import page1
           def nextPage1():
               root.destroy()
               import page2    
           toggle_menu_fm=tk.Frame(root,bg='#202c61',highlightbackground='white',highlightthickness=1)
           
           home_btn=tk.Button(toggle_menu_fm,text="🏠 HOME",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage)
           home_btn.place(x=20,y=20)
           cci_btn=tk.Button(toggle_menu_fm,text="📊 CCI",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage1)
           cci_btn.place(x=20,y=80)
           about_btn=tk.Button(toggle_menu_fm,text="☎ ABOUT US",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white')
           about_btn.place(x=20,y=140)
           
           #window_height=root.winfo_height() 
           toggle_menu_fm.place(x=0,y=70,height=511,width=200)
           toggle_btn.config(text='X',font=('Arial Bold',20))
           toggle_btn.config(command=collapse_toggle_menu)

       
       
       head_frame=tk.Frame(root, bg='#202c61',
                           highlightbackground='white',highlightthickness=1)
       
       photo = PhotoImage(file="g.png")
       photo_label = Label(head_frame,image=photo,height=64,width=64)
       photo_label.place(x=53,y=0)
       
       
       toggle_btn=tk.Button(head_frame,text='☰',bg='#202c61',fg='white',font=('Arial  Bold',20),bd=0,command=toggle_menu)
       toggle_btn.pack(side=tk.LEFT)
       

       title_lb=tk.Label(head_frame,text="SENTIMEMNT ANALYSIS BASED CONSUMER CONFIDENCE INDEX COMPUTATION OF PURCHASING BEHAVIOUR", bg='#202c61',fg='white',font=('Arial Bold',13))
       title_lb.place(x=140,y=14)
       
       label_mission = tk.Label(root,text="OUR MISSION",font=("Arial bold",16))
       label_mission.pack(side=tk.LEFT)
       label_mission.place(x=530,y=90)
       
       frame_mission=Frame(root,bg="#202c61",highlightbackground="white", highlightthickness=3).place(x=260,y=140,height=120,width=750)
       label_mission_data = tk.Label(frame_mission,height=4,text="Our mission is to perform cleaning, normalization of contextualized and country specific user generated contents\n from social media channels.Further this study aims to preprocess annotate the ectracted contents with subjective \nlabels via deep learning classifier. Subjectivity Classification will provide the Consumer's Confidence Index about\n the specific content.",font=('Arial bold',10),bg='#202c61',fg='white')
       label_mission_data.place(x=270,y=160)
       
       
    
       

       
       head_frame.pack(side=tk.TOP,fill=tk.X)
       head_frame.pack_propagate(False)
       head_frame.configure(height=70)
       bottom_frame=tk.Frame(root, bg='#202c61',
                           highlightbackground='white',highlightthickness=1)
       bottom_frame.pack(side=tk.BOTTOM,fill=tk.X)
       bottom_frame.pack_propagate(False)
       bottom_frame.configure(height=70)
       root.mainloop()
PAGE3()       
      