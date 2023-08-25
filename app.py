from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
db = SQLAlchemy(app)

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    size = db.Column(db.Integer)
    filepath = db.Column(db.String(255))

with app.app_context():
    db.create_all()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save the uploaded file to the uploads directory
    file_path = os.path.join('C:\\Users\\Abhinandan Gautam\\Desktop\\Rapidfort\\uploads', file.filename)
    file.save(file_path)
    
    # Store file information and reference in the database
    file_info = UploadedFile(filename=file.filename, size=os.path.getsize(file_path), filepath=file_path)
    db.session.add(file_info)
    db.session.commit()
    
    payload = { 'filename': file.filename,
                'size': os.path.getsize(file_path),
                'filepath': file_path
    }

    return render_template('uploads.html', data = payload)

@app.route('/files', methods=['GET'])
def get_uploaded_files():
    files = UploadedFile.query.all()
    file_list = [{'filename': file.filename, 'size': file.size, 'filepath': file.filepath} for file in files]
    return render_template('files.html', data = file_list)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(debug=True, port=port)