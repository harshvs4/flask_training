from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John Doe"
    return render_template('index.html',name=name)

@app.route('/about')
def about():
      title = "About Page"
      message = "This is about page"
      return render_template('about.html',title=title,message=message)

if __name__ == '__main__':
	app.run()