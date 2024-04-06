from flask import Flask, render_template, url_for
app =  Flask(__name__)

posts = [
    {
        'author' : 'Steve Das',
        'title' : 'Testing Flask',
        'content' : 'First post content',
        'date_posted' : '6th March 2024'
    },
    {
        'author' : 'Amy Das',
        'title' : 'Testing Flask',
        'content' : 'Second post content',
        'date_posted' : '7th March 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)