import os

dataset_dir = "~/data/coco_train_2017"
style_file = "./images/style-images/oil_painterly.jpg"
model_dir = "saved_models/oil_painterly/"

os.system("mkdir -p %s" % model_dir)
os.system("python neural_style/neural_style.py train --dataset %s --style-image %s --save-model-dir %s "
          "--epochs 2 --cuda 1" % (dataset_dir, style_file, model_dir))
