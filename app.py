from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    languages = LANGUAGES
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    dest_lang = data.get('dest_lang')
    if not text or not dest_lang:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        translation = translator.translate(text, dest=dest_lang)
        return jsonify({'translated_text': translation.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
