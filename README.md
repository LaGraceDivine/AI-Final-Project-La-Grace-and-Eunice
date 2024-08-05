# AI-Final-Project-La-Grace-and-Eunice: Fake Image Generator

# Project Overview

Our project is building a Generative Adversarial Network to generate fake images using Tensorflow and MNIST dataset.

Our project solves the issue of lacking tailored mathematical educational tools in kindergartehn school. Therefore, our model is used to generate fake images with digits to help kindergarten teachers to teach their students digis from 0 to 9.

# Steps Followed to Train the Model and  Deploy it for Use

We went through the following process from training the model to generating fake images:
1. Installing and importing all thenecessary libraries
2. Loading the training MNIST dataset.
3. Building and compling the discriminator using a binary cross-entropy loss and optimizer.
4. Building the generator model
5. Building GAN by combining the generator and the discriminator
6. Compile the GAN with binary cross-entropy loss and optimizer
7. Train the model for 2000 epochs with interval 100 and save the generator and discriminator models periodically
8. Generate images using the trained generator by inputting random noise and display generated images using matplotlib
9. Use visual inspection to generate and inspect the model performance to see the improvement in quality and adjusting the parameters accordingly.
10. Deploying the model using Flask through setting up flask environment by installing and defining it, load the trained generator model, creating a handle that accepts user image generation requests including number of images he/she wants and the size of those images in pixels, and use html to design the user interface.
11. Run the flask application

# Youtube link to the video showing how the fake image generator app works: 
https://youtu.be/tfzRQkyK9Bc
