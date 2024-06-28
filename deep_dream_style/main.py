from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_dream import run_deep_dream
import random
import base64
import io


app = Flask(__name__)
CORS(app)


@app.route('/stylize-image', methods=['POST'])
def stylize():
    image = request.files['content_image']
    level = request.form['level']
    random_number = ''.join(random.choice('0123456789') for _ in range(8))
    content_path = f'images/content-{random_number}.jpg'
    image.save(content_path)

    stylized_image = run_deep_dream(path=content_path, level=level, steps=100, step_size=0.05)

    image_bytes = io.BytesIO()
    stylized_image.save(image_bytes, format='JPEG')
    stylized_image.save(f'images/content-result-{random_number}.jpg')
    image_bytes.seek(0)
    encoded_img = base64.b64encode(image_bytes.read()).decode('utf-8')

    return jsonify({'stylized_image': encoded_img})

if __name__ == '__main__':
    app.run()