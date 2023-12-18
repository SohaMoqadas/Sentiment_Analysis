# import tkinter as tk
from flask import Flask, render_template , redirect , url_for , request , session , send_file , Response
from commons.calculate_cci import calculate_cci
import csv
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from textblob import TextBlob
# from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'abc123122dfdgereb4343'
from os import path, walk
import os
import io

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = 'static'

extra_dirs = ['templates']  # Modify this as needed
extra_files = extra_dirs[:]

for extra_dir in extra_dirs:
    for dirname, _, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)

@app.route('/')
def index():
    return render_template('page1.html')

def get_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def calculate_sentiment_score(SP, WP, WN, SN):
    return SP + (0.50 * WP) - (0.50 * WN) - SN

# Update the get_sentiment_category function to handle non-numeric input
def sentiment_category(score):
    # Convert the score to float
    score_float = float(score)

    # Now categorize based on the numeric score
    if score_float > 0.5:
        return "Strong Positive"
    elif score_float > 0.0:
        return "Weak Positive"
    elif score_float == 0.0:
        return "Neutral"
    elif score_float >= -0.5:
        return "Weak Negative"
    else:
        return "Strong Negative"

# Update the calculate_cci function to include sentiment score calculation

def calculate_cci(df):
    analyzer = SentimentIntensityAnalyzer()

    # Apply sentiment analysis to each row in the DataFrame
    df['SentimentScore'] = df['Noise Cleared'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Categorize sentiment scores
    df['SentimentCategory'] = df['SentimentScore'].apply(sentiment_category)

    # Calculate sentiment score for each parameter
    df['SP'] = df['SentimentScore'] * (df['SentimentCategory'] == 'Strong Positive')
    df['WP'] = df['SentimentScore'] * (df['SentimentCategory'] == 'Weak Positive')
    df['WN'] = df['SentimentScore'] * (df['SentimentCategory'] == 'Weak Negative')
    df['SN'] = df['SentimentScore'] * (df['SentimentCategory'] == 'Strong Negative')

    # Calculate overall sentiment score for each row
    df['OverallSentimentScore'] = df.apply(lambda row: calculate_sentiment_score(row['SP'], row['WP'], row['WN'], row['SN']), axis=1)

    return df['OverallSentimentScore']
    
def getFilesNames():
    path = os.getcwd()+"/static/purchasing behaviour"
    list_of_files = {}

    for filename in os.listdir(path):
        if not filename.startswith("~"):
            list_of_files[filename] = filename

    return list_of_files

def remove_noise(text):
    # Remove user mentions, hashtags, and URLs
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # Remove mentions
    text = re.sub(r'#', '', text)  # Remove hashtags
    text = re.sub(r'https?://[A-Za-z0-9./]+', '', text)  # Remove URLs

    text = re.sub(r'😊', '', text)
    
    # Replace contractions with expanded forms
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "can not", text)
    
    # Remove non-alphanumeric characters
    text = re.sub(r'[^A-Za-z0-9]', ' ', text)
    
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize the text
    words = word_tokenize(text)
    
    # Join the tokenized words into a clean text
    clean_text = ' '.join(words)
    return clean_text

def clean_text(text):
    return text
    # Remove double quotes from text
    # cleaned_text = re.sub('"', '', text)
    # return cleaned_text


def get_file_type(file_content):
    # Use magic to determine the file type
    dot = file_content.find('.')
    file_type = file_content['filename'][dot:]
    return file_type

def subjectivity(text):
    analysis = TextBlob(text)
    return analysis.sentiment.subjectivity

def sentiment_score(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    label = ''
    if score > 0 :
        label = 'Positive'
    elif score < 0 :
        label = 'Negative'
    else:
        label = 'Neutral'
    return label          

@app.route('/page2' , methods= ['POST','GET'])
def page1():
    user_input = ''
    norm = False
    if request.method == 'POST':
        data_select = request.form['dataset']
        file = request.files['uploadfile']
        stored = {'indicators':'nothing','data':''}   
        if data_select:
            excel_path = "static/purchasing behaviour/" + request.form['dataset']        
            df = pd.read_excel(excel_path)
            stored['data'] = excel_path
            stored['indicators'] = 'path'
        # elif request.form['perform_norm']:
        elif file :
            df = pd.read_excel(file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            sanitized_filename = file.filename.replace(' ', '_')
            filename = f"{timestamp}_{sanitized_filename}"
            # filename = f"{timestamp}_{file.filename}"
            # Specify the path where you want to save the file
            upload_path = os.path.join("static/uploads", filename)
            # print(upload_path)
            # Save the file with the generated path
            file.save(upload_path)
            stored['data'] = upload_path
            stored['indicators'] = 'path'
        session['uploaded_data'] = stored  
        selected = ['Translated', 'Sentiment Label' , 'Cci']
        df['Noise Cleared'] = df['Translated'].apply(remove_noise)
        df['Tokens'] = df['Noise Cleared'].apply(word_tokenize)
        df['Sentiment Label'] = df['Noise Cleared'].apply(sentiment_score)
        df['Cci'] = calculate_cci(df)
        df = df[selected]
        # data = df.to_html()
        # data = calculate_cci(df)
        norm = True
        return render_template('output.html', data = df.to_html(), norm=norm  )
    return render_template('page2.html', filenames = getFilesNames())

@app.route('/page3')
def page2():
    return render_template('page3.html')

@app.route('/page4' , methods = ['POST', 'GET'])
@app.route('/page4/<extracted>')
def page3(extracted = False):
    user_input = ''
    print('user insput',extracted)
    if request.method == 'POST':
        # if 'text-extract' in request.form:
            # check = request.form['text-extract']/
        stored = {'indicators':'nothing','data':''}    
        user_input = request.form['field2'] 
        if user_input:
            df = pd.DataFrame({'Translated': [user_input]}) 
            stored['data'] = user_input
            stored['indicators'] = 'input' 
            session['uploaded_data'] = stored  
        else:
            content = session.get('uploaded_data', 'Default Processed Data')
            if content['indicators'] == 'input':
                df = pd.DataFrame({'Translated': [content['data']]})             
            else:          
                df = pd.read_excel(content['data'])  
        selected = ['Translated']
        if 'noise_removal' in request.form and request.form['noise_removal'] == 'on':
            df['Noise Cleared'] = df['Translated'].apply(remove_noise)
            selected.append('Noise Cleared')

        # Tokenization
        if 'Noise Cleared' in selected :
            df['Tokens'] = df['Noise Cleared'].apply(word_tokenize)
        else :     
            df['Tokens'] = df['Translated'].apply(word_tokenize)

        if 'tokenization' in request.form and request.form['tokenization'] == 'on':
            selected.append('Tokens')

        if 'pos_tagging' in request.form and request.form['pos_tagging'] == 'on':
            #  Part-of-Speech Tagging
            df['POS Tags'] = df['Tokens'].apply(pos_tag)
            selected.append('POS Tags')

        if 'stemming' in request.form and request.form['stemming'] == 'on':
            # Stemming
            stemmer = PorterStemmer()
            df['Stemming'] = df['Tokens'].apply(lambda tokens: [stemmer.stem(token) for token in tokens])
            selected.append('Stemming')

        if 'lematization' in request.form and request.form['lematization'] == 'on':
            # Lemmatization
            lemmatizer = WordNetLemmatizer()
            df['Lematization'] = df['Tokens'].apply(lambda tokens: [lemmatizer.lemmatize(token) for token in tokens])
            selected.append('Lematization')

        # if 'annotation' in request.form and request.form['annotation'] == 'on':
        #     # Annotation (Replace this with your annotation logic)
        #     df['annotated_tokens'] = df['tokens'].apply(lambda tokens: ['annotate_' + token for token in tokens])
        #     selected.append('annotated_tokens')

        if 'subjectivity' in request.form and request.form['subjectivity'] == 'on':
            # Annotation (Replace this with your annotation logic)
            df['Subjectivity Score'] = df['Noise Cleared'].apply(subjectivity)
            selected.append('Subjectivity Score')

        if 'sentiment_score' in request.form and request.form['sentiment_score'] == 'on':
            df['Sentiment Label'] = df['Noise Cleared'].apply(sentiment_score)
            selected.append('Sentiment Label') 

        # consumer_sentiment = 75  # On a scale of 0 to 100
        # unemployment_rate = 5  # In percentage
        # consumer_spending = 80  # In percentage of GDP
        # cci = calculate_cci(consumer_sentiment , unemployment_rate , consumer_spending)
        df = df[selected]
        return render_template('output.html',data = df.to_html())
    if extracted:
        extracted = 'True' 
    else: 
        extracted = 'False'  
    return render_template('inputFilePage.html', extracted = extracted)    

@app.route('/page5', methods = ['POST', 'GET'])
def page4():
    content = session.get('uploaded_data', 'Default Processed Data')
    if content['indicators'] == 'input':
        df = pd.DataFrame({'Translated': [content['data']]})             
    else:          
        df = pd.read_excel(content['data'])
    if request.method == 'POST':
        selected = ['Translated', 'Noise Cleared' ,'Tokens' , 'POS Tags' , 'Stemming' , 'Lematization' ]
        df['Noise Cleared'] = df['Translated'].apply(remove_noise)
        df['Tokens'] = df['Noise Cleared'].apply(word_tokenize)
        #  Part-of-Speech Tagging
        df['POS Tags'] = df['Tokens'].apply(pos_tag)
        # Stemming
        stemmer = PorterStemmer()
        df['Stemming'] = df['Tokens'].apply(lambda tokens: [stemmer.stem(token) for token in tokens])
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        df['Lematization'] = df['Tokens'].apply(lambda tokens: [lemmatizer.lemmatize(token) for token in tokens])
        # Annotation (Replace this with your annotation logic)
        # df['Annotated Tokens'] = df['Tokens'].apply(lambda tokens: ['annotate_' + token for token in tokens])
        # Annotation (Replace this with your annotation logic)
        if 'print' in request.form and request.form['print'] == 'subjective':
            df['Subjectivity Score'] = df['Noise Cleared'].apply(subjectivity)
            selected.append('Subjectivity Score')
        elif 'print' in request.form and request.form['print'] == 'sentiment':  
            df['Sentiment Label'] = df['Noise Cleared'].apply(sentiment_score)
            selected.append('Sentiment Label')
        elif 'print' in request.form and request.form['print'] == 'cci_comp':  
            df['Cci'] = calculate_cci(df)
            selected.append('Cci')   
        df = df[selected]
        # return render_template('output.html',data = df.to_html())
        csv_data = df.to_csv(index=False)
        # return render_template('output.html',data=df.to_html())
        return Response(
            csv_data,
            mimetype="text/csv",
            headers={"Content-disposition": "attachment; filename=print.csv"}
        )
    
        # response = send_file(df.to_csv('print.csv', index=False), as_attachment=True, download_name='data.csv', mimetype='text/csv')
        return response
    return render_template('page4.html')

@app.route('/page6', methods= ['POST','GET'])
def page5():
    filenames = getFilesNames()
    if request.method == 'POST':
        file = request.files['uploadfile']
        user_input = request.form['field2'] 
        stored = {'indicators':'nothing','data':''}
        if user_input:
            # df = pd.DataFrame({'Translated': [user_input]})  
            stored['data'] = user_input
            stored['indicators'] = 'input'           
        elif file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            sanitized_filename = file.filename.replace(' ', '_')
            filename = f"{timestamp}_{sanitized_filename}"
            # filename = f"{timestamp}_{file.filename}"
            # Specify the path where you want to save the file
            upload_path = os.path.join("static/uploads", filename)
            # print(upload_path)
            # Save the file with the generated path
            file.save(upload_path)
            stored['data'] = upload_path
            stored['indicators'] = 'path'
            # df = pd.read_excel(file)
            # df = df.head(100)
        else:
            excel_path = "static/purchasing behaviour/" + request.form['dataset']
            stored['data'] = excel_path
            stored['indicators'] = 'path'          
            # df = pd.read_excel(excel_path)

            
        session['uploaded_data'] = stored       
        # print('hello')
        return redirect(url_for('page3', extracted=True))
            # return render_template('output.html',data = df.to_html())
    return render_template('page5.html',filenames = filenames)


if __name__ == '__main__':
    app.run(extra_files=extra_files , debug=True)
      