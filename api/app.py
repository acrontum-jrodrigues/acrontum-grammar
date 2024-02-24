from flask import Flask, request
from transformers import AutoTokenizer, T5ForConditionalGeneration
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")

@app.route('/grammar', methods=['POST'])
def correct():
    input_text = request.json['text']
    # Tell the model to fix the grammar by adding "Fix the grammar: " at the beginning of the input text
    input_text = "Fix the grammar: " + input_text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {'edited_text': edited_text}

if __name__ == '__main__':
    app.run()
