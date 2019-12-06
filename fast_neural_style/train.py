import os

style_name = "oil_painterly"
dataset_dir = "~/data/coco_train_2017"
style_file = "./images/style-images/%s.jpg" % style_name
content_weight = 1E5
style_weight = 1E10
style_size = 512
model_dir = "saved_models/%s_%d_%d_%d/" % (style_name, content_weight, style_weight, style_size)
checkpoint_model_dir = "saved_models/%s_%d_%d_%d_checkpoints/" % (style_name, content_weight, style_weight, style_size)
os.system("mkdir -p %s" % model_dir)
os.system("mkdir -p %s" % checkpoint_model_dir)
os.system("python neural_style/neural_style.py train --dataset %s --style-image %s --save-model-dir %s "
          "--epochs 2 --cuda 1 --checkpoint-model-dir %s --content-weight %d --style-weight %d --style-size %d" % (
    dataset_dir, style_file, model_dir, checkpoint_model_dir, content_weight, style_weight, style_size))
