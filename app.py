from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return ''  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length'))
        use_uppercase = 'use_uppercase' in request.form
        use_lowercase = 'use_lowercase' in request.form
        use_numbers = 'use_numbers' in request.form
        use_symbols = 'use_symbols' in request.form

        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
