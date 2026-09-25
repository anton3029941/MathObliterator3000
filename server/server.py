from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import solve

# confs and init
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(
    __name__, 
    template_folder='../website',
    static_folder='../website',
    static_url_path='/static'
)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# checking extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/solve', methods=['POST'])
def upload():
    # handling invalid inputs
    if 'image_file' not in request.files:
        return "No file part in the request", 400

    file = request.files['image_file']
    
    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        # saving the image on the server
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        solution = solve.process_and_solve(file_path)

        if os.path.exists(file_path):
            os.remove(file_path)

        return solution, 200
        
    return "File type not allowed", 400

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    app.run(debug=True)