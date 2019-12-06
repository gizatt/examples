import os

content_file = "./images/content-images/kara.png"
model_file = "saved_models/mosaic.pth"
output_file = "out.png"

os.system("python neural_style/neural_style.py eval --content-image %s "
          "--model %s --output-image %s --cuda 1" % (
              content_file, model_file, output_file))
