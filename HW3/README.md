# Instance Segmentation

I use [yolact](https://github.com/dbolya/yolact) to complete this assignment.

## Environment setup
clone the repo <br/>
```git clone https://github.com/dbolya/yolact.git```

install dependencies
```
pip install cython
pip install opencv-python pillow pycocotools matplotlib
```

Use YOLACT++ [Optional]
```
cd external/DCNv2
python setup.py build develop
```

## Edit ./data/config.py (or you can just replace the config.py with my config.py 
add myDataset_test under the end of **DATASETS** part <br/>
```
myDataset_test = dataset_base.copy({
  'name': '<your desired name>',
  'valid_info': '<path to json that annotates testing set>',
  'valid_images': '<path to testing set>',
  'class_names': PASCAL_CLASSES,
  'label_map': None
})
```

add test_config under the end of **YOLACT v1.0 CONFIGS** part <br/>
```
myDataset_test = dataset_base.copy({
  'name': '<your desired name>',
  'dataset': myDataset_test,
  'num_classes': 21,
  'max_size': 550,      # recommended by official github
})
```

## Prepare weight
put [my pretrained weight](https://drive.google.com/file/d/1Zr0WM4Lwwv2jkYmKirL_sp5wZ31nJYiV/view?usp=sharing) in ./weights/ folder


## Evaluate the model
evaluate my model <br/>
```
python3 eval.py --trained_model=weights/<your weight.pth> --config=test_config --output_coco_json --dataset=myDataset_test
```

the above command will generate 2 .json file in ./results/ folder, and the **mask_detections.json** is what we needed


## Citation

```
@article{yolact-plus-tpami2020,
  author  = {Daniel Bolya and Chong Zhou and Fanyi Xiao and Yong Jae Lee},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title   = {YOLACT++: Better Real-time Instance Segmentation}, 
  year    = {2020},
}
```
