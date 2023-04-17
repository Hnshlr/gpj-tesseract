# DEFAULT IMPORTS:
import os  # OS
# FLASK IMPORTS:
from flask import Flask, render_template, request, flash  # FLASK
from werkzeug.utils import secure_filename
# MODELS=
from src.Models.Graph import Graph  # GRAPH
from src.Models.NXGraph import NXGraph  # NXGRAPH
# CONTROLLERS=
from src.Controllers.GraphController import *  # GRAPH CONTROLLER
from src.Controllers.NXGraphController import *  # NXGRAPH CONTROLLER

# PATHS=
input_dir = "static/input/"
output_dir = "static/output/"
os.mkdir(output_dir) and print("Can't find output directory. Creating one now.") \
    if not os.path.isdir(output_dir) else print("Found existing output directory.")
upload_dir = 'static/input/uploads'
allowed_extensions = {'csv', 'xlsx', 'tsv', 'ods'}

# TEMP: PRELOAD GRAPH/NXGRAPH OBJECTS CONSTRUCTION -> SAVE TO PICKLE:
Graph(filepath=input_dir + "chinese.csv", output_dir=output_dir, save_csvs=True, save_pickle=True)
Graph(filepath=input_dir + "indian.csv", output_dir=output_dir, save_csvs=True, save_pickle=True)

# FLASK APP:
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_dir

# BLUEPRINTS/CONTROLLERS:
app.register_blueprint(nxgraph_bp)


# INDEX ROUTE:
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("base.html")


# UPLOAD ROUTE:
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@app.route('/choice', methods=['GET', 'POST'])
def choose_dataset():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template("dataset/upload_not_valid.html")
        file = request.files['file']
        # If the user does not select a file, the page is refreshed.
        if file.filename == '':
            return render_template("dataset/upload_not_valid.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("dataset/upload_done.html")
    return render_template("dataset/dataset_selection.html")


# MAIN:
def main():
    # START THE APP:
    app.run(debug=True)


if __name__ == '__main__':
    main()
