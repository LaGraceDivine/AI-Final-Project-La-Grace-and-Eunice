# app.py
from flask import Flask, request, render_template, send_file
from tensorflow.keras.models import load_model
import numpy as np
import io
from PIL import Image
import os
import base64

app = Flask(__name__)

# Load the pre-trained GAN generator model
generator = load_model("//Users//divineigirubuntu//Downloads//my_model.h5")
latent_dim = 100  # Make sure this matches the latent_dim used in training

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get the number of images to generate and the desired size
    num_images = int(request.form['num_images'])
    img_size = int(request.form['img_size'])

    # Generate images
    noise = np.random.normal(0, 1, (num_images, latent_dim))
    gen_images = generator.predict(noise)
    gen_images = 0.5 * gen_images + 0.5  # Rescale to [0, 1]

    # Process and save the generated images
    image_urls = []
    for i, gen_image in enumerate(gen_images):
        gen_image = (gen_image * 255).astype(np.uint8)
        gen_image = gen_image.squeeze()
        pil_img = Image.fromarray(gen_image).resize((img_size, img_size))

        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        pil_img.save(img_io, 'PNG')
        img_io.seek(0)

        # Convert image to base64 string for HTML display
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        image_urls.append(f"data:image/png;base64,{img_base64}")

    return render_template('index.html', images=image_urls)

if __name__ == '__main__':
    app.run(debug=True)

 