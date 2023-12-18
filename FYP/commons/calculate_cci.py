import csv

def calculate_cci(consumer_sentiment, unemployment_rate, consumer_spending):
    # print('checking here')
    # Normalize the values (between 0 and 100)
    normalized_consumer_sentiment = consumer_sentiment / 100
    normalized_unemployment_rate = (10 - unemployment_rate) / 10  # Inverted, higher value is better.
    normalized_consumer_spending = consumer_spending / 100

    # Calculate the CCI as the average of the three factors
    cci = (normalized_consumer_sentiment + normalized_unemployment_rate + normalized_consumer_spending) / 3

    # Scale the CCI to be in the range of 0 to 100
    cci = min(100, max(0, cci * 100))

    return cci

def fileupload(file):
    if file:
        filename = file.filename
        if filename.endswith('.csv'):
            # Handle CSV file
            data = []
            try:
                csv_data = file.read().decode('utf-8').splitlines()
                csv_reader = csv.reader(csv_data)
                for row in csv_reader:
                    data.append(row)
            except Exception as e:
                return f"Error reading CSV file: {str(e)}"

            return {'key':'csv','data':data}

        elif filename.endswith('.txt'):
            # Handle text file
            text_data = file.read().decode('utf-8')
            return {'type':'text','data':text_data}

    else:
        return "Unsupported file format. Please upload a CSV or text file."