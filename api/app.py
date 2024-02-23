from flask import Flask, request
from transformers import AutoTokenizer, T5ForConditionalGeneration

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")

@app.route('/correct', methods=['POST'])
def correct():
    input_text = request.json['text']
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {'edited_text': edited_text}

if __name__ == '__main__':
    app.run()
