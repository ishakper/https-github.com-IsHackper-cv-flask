from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000

IMAGE_FOLDER = os.path.join(os.getcwd(), 'image')

@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)

@app.route('/api/stats')
def get_stats():
    return {
        'projects': 5,
        'experience_years': 2,
        'github_repos': 12,
        'certifications': 3
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False, use_reloader=False)
