from flask import Flask, render_template, request
import tensorflow as tf
from transformers import BertTokenizer
import numpy as np
from random import randrange


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        processed_output = process_text(user_input)
        return processed_output
    return render_template('index.html')


def process_text(text):
    # Add your text processing logic here
    # processed_text = predict(text)
    processed_text = predict(text)
    return processed_text

def predict(input_text):
    # model = tf.keras.models.load_model('src\clinical_notes_model')
    # tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',do_lower_case=True)
    # token = tokenizer.encode_plus(
    #     input_text,
    #     max_length=512,
    #     truncation=True,
    #     padding='max_length',
    #     add_special_tokens=True,
    #     return_tensors='tf'
    # )
    # tokenized_text = {'input_ids': tf.cast(token.input_ids, tf.float64), 'attention_mask': tf.cast(token.attention_mask, tf.float64)}
    Categories = ['Neurology','Urology','Radiology','Orthopedic','Gastroenterology']
    # probs = model.predict(tokenized_text)[0]
    # return Categories[np.argmax(probs)]
    return Categories[randrange(5)]

def extract_names(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    names = []

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            names.append(entity.text)

    return names

def extract_age(text):
    pattern = r"\b(\d{1,2})\b"  # Matches 1 or 2 digits as a word boundary
    match = re.search(pattern, text)
    if match:
        age = int(match.group(0))
        return age
    else:
        return "no ages found"

if __name__ == '__main__':
    app.run(debug=True)