from flask import Flask, render_template, request

app = Flask(
    __name__, 
    template_folder='../website',
    static_folder='../website',
    static_url_path='/static'
)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/upload', methods=['POST'])
def upload():
    form = request.files['image_file']


if __name__ == "__main__":
    app.run(debug=True)