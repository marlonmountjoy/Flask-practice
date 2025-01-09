from flask import Flask, render_template, request
# Import Flask class, render_template is for rendering the HTML,
# request is to handle form data
import html  # Import the html module for sanitization

app = Flask(__name__) # Create Flask instance

# Home route that is triggered when the user accesses the root URL
@app.route('/')
def home():
    return render_template('index.html') # Render and return the index template

# Submit route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the user input from the form
    user_input = request.form['user_input']

    # Sanitize the input to escape potentially harmful HTML characters
    # This is a second layer of sanitization after Jinja2's autoescaping
    sanitized_input = html.escape(user_input)

    # Pass the sanitized input to the result template
    return render_template('result.html', user_input=sanitized_input)


if __name__ == '__main__':
    app.run(debug=True)


