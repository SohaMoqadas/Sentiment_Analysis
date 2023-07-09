
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfile

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfile


import os
import pandas as pd 
import re 
from textblob import TextBlob
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
# import spacy
from nltk.corpus import sentiwordnet as swn
from IPython.display import clear_output
# import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import googletrans
from googletrans import Translator
# from wordcloud import WordCloud
# import plotly

import ssl
from nltk.corpus import wordnet as wn  

class PAGE2:
    
    
    def __init__(self):
       root=tk.Tk()
       root.geometry("1200x660")
       root.title("CCI")
       root.iconbitmap(r"C:\Users\SUN IT\OneDrive\Documents\interface of fyp")
    
       
       def toggle_menu():
           
           def collapse_toggle_menu():
               toggle_menu_fm.destroy()
               toggle_btn.config(text='☰')
               toggle_btn.config(command=toggle_menu)
              
           def nextPage():
               root.destroy()
               import page1
           def nextPage3():
               root.destroy()
               import page3    
           toggle_menu_fm=tk.Frame(root,bg='#202c61',highlightbackground='black',highlightthickness=1)
           
           home_btn=tk.Button(toggle_menu_fm,text="🏠 HOME",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage)
           home_btn.place(x=20,y=20)
           cci_btn=tk.Button(toggle_menu_fm,text="📊 CCI",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white')
           cci_btn.place(x=20,y=80)
           about_btn=tk.Button(toggle_menu_fm,text="☎ ABOUT US",font=('Arial Bold',15),bd=0,bg='#202c61',fg='white',activebackground='#202c61',activeforeground='white',command=nextPage3)
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
       
       
       
       title_lb=tk.Label(head_frame,text="SENTIMEMNT ANALYSIS BASED CONSUMER CONFIDENCE INDEX COMPUTATION OF PURCHASING BEHAVIOUR", bg='#202c61',fg='white',font=('Arial Bold',12))
       title_lb.place(x=140,y=14)
       
     
       
  
      
       
   
       
       button_select=tk.Button(root,text="⋮", command=self.openfile,font=("Arial Bold",16),bg="#202c61",fg="white",bd=1)
       button_select.place(x=360,y=150)
       
       label_select = tk.Label(root,text="Select DataSet",font=("Arial bold",16),bg="#202c61",fg="white")
       label_select.pack(side=tk.LEFT)
       label_select.place(x=15,y=100)
       
       # button_select1=tk.Button(root,text="GO ",command=self.senti, font=("Arial Bold",16),bg="skyblue",fg="black",bd=1)
       # button_select1.place(x=430,y=150,width=130)
       
       self.textbox_select = tk.Entry(root,bd=3,width=22,font="Arial 20")
       self.textbox_select.place(x=15,y=150)
       
       label_dropdown = tk.Label(root,text='Lingual Processing',font=("Arial bold",16),bg="#202c61",fg="white")  
       label_dropdown.place(x=15,y=200)
       

       
       
       self.options = tk.StringVar(root)
       self.options.set("Select Task")
       self.dropdown =tk.OptionMenu(root,self.options, "Normalization","Translation", "Text Correction", "Lemmatization","POS Tagging","Sentiment score",command = self.dropd)
       self.dropdown.place(x=12,y=240) 
       self.dropdown.config(width =47,bg="#202c61",fg="white")
       
       
       radio_frame=tk.Frame(root, bg='#202c61',
                           highlightbackground='white',highlightthickness=1,height=100,width=350)  
       radio_frame.place(x=650,y=130)
       # label_radio = tk.Label(root,text='Subjectivity Classification',font=("Arial bold",16) ,bg='skyblue')  
       # label_radio.place(x=20,y=445) 
       self.r=tk.IntVar()
       self.Radio=tk.Radiobutton(root,text="Commulative",variable=self.r,value=1,command=self.rem,width=20).place(x=665,y=155)
       self.Radio1=tk.Radiobutton(root,text="Monthly  :",variable=self.r,value=2,command=self.select,width=20).place(x=665,y=175)
       
       button_date_sub=tk.Button(root,text="GET",command=self.report,font=("Arial Bold",12),bg="#202c61",fg="white",bd=1) 
       button_date_sub.place(x=880,y=190)
       
       label_result = tk.Label(root,text='Subjectivity Classification',font=("Arial bold",16),bg="#202c61",fg="white" )  
       label_result.place(x=650,y=90) 
       
       # textbox_type = tk.Text(root,font="Arial 16")
       # textbox_type.place(x=600,y=130,width=45,height=50)
       self.f3 = tk.Frame(root, bg= "#202c61", highlightbackground='white', highlightthickness=7)
       self.f3.place(height = 300, width=1055, x =15, y=300)
       
       self.L2 = tk.Label(self.f3, bg="white",  highlightcolor="white")
       self.scroll_x = tk.Scrollbar(self.L2,orient=HORIZONTAL )
       self.scroll_y = tk.Scrollbar(self.L2, orient=VERTICAL)
       s = ttk.Style()
       s.theme_use('clam')
       s.map("Custom.Treeview", background=[("selected", "green")])
       s.configure('Treeview')
       self.dataview = ttk.Treeview(self.L2,
                                         columns=("Date", "Data", "Translated", "Lemmatization", "Pos", "Sentiment Score","Subjectivity"),
                                         height=27, xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
       self.scroll_x.pack(side=BOTTOM, fill=X)
       self.scroll_y.pack(side=RIGHT, fill=Y)
       self.scroll_x.config(command=self.dataview.xview)
       self.scroll_y.config(command=self.dataview.yview)
       self.dataview.heading("Date", text="Date")
       self.dataview.heading("Data", text=" Data")
       self.dataview.heading("Translated", text="Translated")
       self.dataview.heading("Lemmatization", text="Lemmatization")
       self.dataview.heading("Pos", text="P.O.S")
       self.dataview.heading("Sentiment Score", text="Sentiment Score")
       self.dataview.heading("Subjectivity", text="Subjectivity")
       self.dataview["show"] = "headings"
       self.dataview.column("Date", )
       self.dataview.column("Data",width=600  )
       self.dataview.column("Translated",width=600 )
       self.dataview.column("Lemmatization",width=600 )
       self.dataview.column("Pos",width=600)
       self.dataview.column("Sentiment Score",width=200)
       self.dataview.column("Subjectivity",width=200 )
       self.dataview.place(height=265, width=1023, x=0, y=0)
        
      
       self.L2.place(height=286, width=1040, x=0, y=0)
        
        
       
       head_frame.pack(side=tk.TOP,fill=tk.X)
       head_frame.pack_propagate(False)
       head_frame.configure(height=70)
       bottom_frame=tk.Frame(root, bg='#202c61',fg='white',
                           highlightbackground='white',highlightthickness=1)
       bottom_frame.pack(side=tk.BOTTOM,fill=tk.X)
       bottom_frame.pack_propagate(False)
       bottom_frame.configure(height=30)
       root.mainloop()
       
       
    def dropd(self, options):
        print("function called")
        if(self.options.get()=="Normalization"):
            self.preprocess_data(self.data_file,'Data')
            print( self.data_file['Data'].head(4))
            
        elif(self.options.get()=="Translation"):
        
            self.translate(self.data_file,'Data')
            print( self.data_file['Translated'].head(4))
        elif(self.options.get()=="Text Correction"):
            self.textcorrect(self.data_file,'Translated')
            print( self.data_file['Translated'].head(4))
        elif(self.options.get()=="Lemmatization"):
             self.lemma(self.data_file,'Translated')
             print( self.data_file.head(4))   
        elif(self.options.get()=="POS Tagging"):
          
             self.pos(self.data_file,'After_lemmatization')
        # print(self.textbox_select.get())
        # self.data_file.to_excel (self.textbox_select.get())
        elif(self.options.get()=="Sentiment score"):
          
             self.sentiment()
        self.data_file.to_excel ("tweet.xlsx",index=False)
    def prnt(self):
        print("function called")
    

        
        
        

    def openfile(self):
        file=fd.askopenfile(mode="r",filetypes=[('Excel Files','*.xlsx')])
        if file:
            filepath=os.path.abspath(file.name)
            self.data_file=pd.read_excel(filepath,index_col=False)
            self.textbox_select.insert(tk.END, filepath)
            for index, row in self.data_file.iterrows():
                 
                 self.dataview.insert("", tk.END, values = [row['Date'], row['Data'],"  ", "   ","   ", "  ","  "])
                
      
       
       
       
       
       # print(data_file.head())
    def senti(self):
        self.preprocess_data(self.data_file,'Data')
        self.translate(self.data_file,'Data')
        
        # self.textcorrect(self.data_file,'Translated')
        self.lemma(self.data_file,'Translated')
        self.pos(self.data_file,'After_lemmatization')
        self.sentiment()
        self.data_file.to_excel ("tweet.xlsx",index=False)
        
    def preprocess_data(self,data,name):
        
        # Proprocessing the data
        data[name]=data[name].str.lower()
        # Code to remove the Hashtags from the text
        data[name]=data[name].apply(lambda x:re.sub(r'\B#\S+','',str(x)))

      
        # Code to remove the links from the text
        data[name]=data[name].apply(lambda x:re.sub(r"http\S+", "", str(x)))
        data[name]=data[name].apply(lambda x:re.sub('rt @\w+:', "", str(x)))
        data[name]=data[name].apply(lambda x:re.sub('\S*@\S*\s?', "", str(x)))
        
        # Remove the twitter handlers
        data[name]=data[name].apply(lambda x:re.sub('@[A-Za-z0-9_]+','',str(x)))
        # Code to remove the Special characters from the text 
        data[name]=data[name].apply(lambda x:' '.join(re.findall(r'\w+', str(x))))
        # Code to substitute the multiple spaces with single spaces
        data[name]=data[name].apply(lambda x:re.sub(r'\s+', ' ', x, flags=re.I))
        # Code to remove all the single characters in the text
        data[name]=data[name].apply(lambda x:re.sub(r'\s+[a-zA-Z]\s+', '', str(x)))
        for item in self.AttendanceReportTable.get_children():
            self.AttendanceReportTable.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.AttendanceReportTable.insert("", tk.END, values = [row['Date'], row['Data'], "  ", "   ","   ", "  "," "])
        
    def translate(self,data,name):
        
       
        source_text = data[name]
        translated_text = []




        # translation object
        translator = Translator() 

        for i in source_text:
            temp = translator.translate(str(i)).text
            translated_text.append(temp)
        data['Translated']=translated_text
        # data_file['Data']=data_file['Data'].apply(lambda txt: ''.join(py_t.translate(str(txt), "en")["translation"]))    
        for item in self.dataview.get_children():
            self.dataview.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.dataview.insert("", tk.END, values = [row['Date'], row['Data'], row['Translated'], "   ","   ", "  "," "])
    def textcorrect(self,data,name):
        data[name]=data[name].apply(lambda txt: ''.join(TextBlob(str(txt)).correct()))
        for item in self.dataview.get_children():
            self.dataview.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.dataview.insert("", tk.END, values = [row['Date'], row['Data'], row['Translated'], "  ","  ", "  ","  "])
        
        
    def lemma(self,dataa,name):
        data=dataa
        Edited = data[name].copy()
        data['without_stopwords'] = Edited
    
        def rem_stopwords_tokenize(data,name):
              
            def getting(sen):
                example_sent = sen
                
                filtered_sentence = [] 

                stop_words = set(stopwords.words('english')) 

                word_tokens = word_tokenize(example_sent) 
                
                filtered_sentence = [w for w in word_tokens if not w in stop_words] 
                
                return filtered_sentence
            # Using "getting(sen)" function to append edited sentence to data
            x=[]
            for i in data[name].values:
                x.append(getting(i))
            data[name]=x



        lemmatizer = WordNetLemmatizer()
        def Lemmatization(data,name):
            def getting2(sen):
                
                example = sen
                output_sentence =[]
                word_tokens2 = word_tokenize(example)
                lemmatized_output = [lemmatizer.lemmatize(w) for w in word_tokens2]
                
                # Remove characters which have length less than 2  
                without_single_chr = [word for word in lemmatized_output if len(word) > 2]
                # Remove numbers
                cleaned_data_title = [word for word in without_single_chr if not word.isnumeric()]
                
                return cleaned_data_title
            # Using "getting2(sen)" function to append edited sentence to data
            x=[]
            for i in data[name].values:
                x.append(getting2(i))
            data[name]=x
            



        def make_sentences(data,name):
            data[name]=data[name].apply(lambda x:' '.join([i+' ' for i in x]))
            # Removing double spaces if created
            data[name]=data[name].apply(lambda x:re.sub(r'\s+', ' ', x, flags=re.I))
            
            
        rem_stopwords_tokenize(data,'without_stopwords')
        make_sentences(data,'without_stopwords')
        final_Edit = data['without_stopwords'].copy()
        data["After_lemmatization"] = final_Edit
        Lemmatization(data,'After_lemmatization')
        # Converting all the texts back to sentences
        make_sentences(data,'After_lemmatization')
        for item in self.dataview.get_children():
            self.dataview.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.dataview.insert("", tk.END, values = [row['Date'], row['Data'], row['Translated'], row['After_lemmatization']," ", " "," "])
    def pos(self,data,name):
        
        
        
        pos=neg=obj=count=0

        postagging = []

        for review in data[name]:
            list = word_tokenize(review)
            postagging.append(nltk.pos_tag(list))

        data['pos_tags'] = postagging

        def penn_to_wn(tag):
            if tag.startswith('J'):
                return wn.ADJ
            elif tag.startswith('N'):
                return wn.NOUN
            elif tag.startswith('R'):
                return wn.ADV
            elif tag.startswith('V'):
                return wn.VERB
            return None
        for item in self.dataview.get_children():
            self.dataview.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.dataview.insert("", tk.END, values = [row['Date'], row['Data'], row['Translated'], row['After_lemmatization'], row['pos_tags'], " "," "])
    def sentiment(self):
        pos=neg=obj=count=0
        def penn_to_wn(tag):
            if tag.startswith('J'):
                return wn.ADJ
            elif tag.startswith('N'):
                return wn.NOUN
            elif tag.startswith('R'):
                return wn.ADV
            elif tag.startswith('V'):
                return wn.VERB
            return None

        
        data=self.data_file
        def get_sentiment(word,tag):
           
            wn_tag = penn_to_wn(tag)
           
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                return []
 
            #Lemmatization
            lemmatizer = WordNetLemmatizer()
            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                return []
 
            #Synset is a special kind of a simple interface that is present in NLTK to look up words in WordNet. 
            #Synset instances are the groupings of synonymous words that express the same concept. 
            #Some of the words have only one Synset and some have several.
            synsets = wn.synsets(word, pos=wn_tag)
            if not synsets:
                return []
 
            # Take the first sense, the most common
            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())
 
            return [synset.name(), swn_synset.pos_score(),swn_synset.neg_score(),swn_synset.obj_score()]
 
            pos=neg=obj=count=0
            
          
           
         
           
         
           
         
           
        senti_score = []
 
        for pos_val in data['pos_tags']:
            senti_val = [get_sentiment(x,y) for (x,y) in pos_val]
            for score in senti_val:
                try:
                    pos = pos + score[1]  #positive score is stored at 2nd position
                    neg = neg + score[2]  #negative score is stored at 3rd position
                except:
                    continue
            if pos-neg >1:
                senti_score.append(1)
            elif pos-neg <-1:
                senti_score.append(-1)
                
            else:
                senti_score.append(pos - neg)
                
            pos=neg=0    
       
        data['senti_score'] = senti_score
       
            
            




        overall=[]
        for i in range(len(data)):
            if data['senti_score'][i]>= 0.5:
                overall.append('Strongly_Positive')
            elif (data['senti_score'][i]>= 0.05 and data['senti_score'][i]< 0.5):
                overall.append('Weakly_positive')
            elif (data['senti_score'][i]<= -0.05 and data['senti_score'][i]> -0.5):
                overall.append('Weakly_Negative')
            elif data['senti_score'][i]<= -0.5:
                overall.append('Strongly_Negative')
            else:
                overall.append('Neutral')
        data['Score']=overall
        
        
        # data.to_excel (self.textbox_select.get())
        
           
           #tk.Text(self.root,font=("Arial",12),height=1.5,width=20).place(x=200,y=520)
        for item in self.dataview.get_children():
            
            self.dataview.delete(item)
        for index, row in self.data_file.iterrows():
             
             self.dataview.insert("", tk.END, values = [row['Date'], row['Data'], row['Translated'], row['After_lemmatization'], row['pos_tags'], row['senti_score'],row['Score']])
             # print(row['Date'], row['Data'], row['Translated'], row['After_lemmatization'], row['pos_tags'],row['senti_score'],row['Score'])
    def subjectivity(self,data):
        
        
        index_names = data[data['Score'] == 'Neutral'].index
        data.drop(index_names, inplace = True)
        # data= data.reset_index()
        data.to_excel ("tweet.xlsx",index=False)
    def average(self,data,name):
        s_pos_avg = (data['Score']=='Strongly_Positive').sum()
        w_pos_avg = (data['Score']=='Weakly_positive').sum()
        s_neg_avg = (data['Score']=='Strongly_Negative').sum()
        w_neg_avg = (data['Score']=='Weakly_Negative').sum()
        #neu_avg = (data['Score']=='Neutral').sum()
        total = data['Score'].count()
        print("Strongly_positive score",s_pos_avg)


        s_pos_average= (s_pos_avg/total)*100
        w_pos_average= (w_pos_avg/total)*100
        s_neg_average= (s_neg_avg/total)*100
        w_neg_average= (w_neg_avg/total)*100
        #neu_average= (neu_avg/total)*100
     
        
        df = pd.DataFrame({'Duration': name,'Strongly_pos': [s_pos_avg],'Weekly_pos': [w_pos_avg],
                            'strongly_neg': [s_neg_avg],'weakly_neg': [w_neg_avg], 'total': [total], 's_positive_average': [s_pos_average], 'w_positive_average': [w_pos_average],
                            's_negative_average': [s_neg_average], 'w_negative_average': [w_neg_average]})

        table=df.to_csv('average.csv',mode='a',index=False,header=False)
        
    def filterdata(self,data,name):
        mon=int(self.test.get())
        print(data[name].head(4))
        # data[name] = data[name].str.replace(' Pakistan Standard Time', '')
        data[name] = pd.to_datetime(data[name],yearfirst=True ).dt.date
        data[name]=pd.to_datetime(data[name])
        data=data.set_index(data[name])
        data=data[data.index.month.isin([mon])]
        file=r"Month"+str(mon)+".xlsx"
        self.path="Month"+str(mon)
        data=data.to_excel (file,index=False) 
        
        
        
        
    def report(self):
        print(self.r.get())
        if self.r.get()==1:
            #self.subjectivity(self.data_file)
            self.average(self.data_file,'Overall')
        else:
            #self.subjectivity(self.data_file)
            self.filterdata(self.data_file,'Date')
            self.average(self.data_file,self.path)

        # self.average(self.data_file)   
    def rem(self):
        if self.check==True:
            self.test.delete(0, 'end')
            self.test.place_forget()
     
    def select(self):
        def click(*args):
            self.test.delete(0, 'end')
  
        # call function when we leave entry box
        def leave(*args):
            # self.textbox_type.delete(0,'end')
            self.mon=self.test.get()
            # test.insert(0, 'Enter Month:- ')
           
        
        date=tk.IntVar()
        self.test= tk.Entry(font="Arial 15",width=13,textvariable=date)
        self.test.insert(0, "Enter Month:")
        self.test.place(x=835,y=155)
        self.test.bind("<Button-1>", click)
        self.test.bind("<Leave>", leave) 
        self.check=True
  
       
        
     
PAGE2()       
      