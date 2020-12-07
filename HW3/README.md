# Instance Segmentation

I use [yolact](https://github.com/dbolya/yolact) to complete this assignment.

First, clone the repo
```https://github.com/dbolya/yolact.git```

Use YOLACT++ [Optional]
```
cd external/DCNv2
python setup.py build develop
```

add myDataset_test under the end of ```**DATASETS**``` part <br/>
```
myDataset_test = dataset_base.copy({
  'name': '<your desired name>',
  'valid_info': '<path to json that annotates testing set>',
  'valid_images': '<path to testing set>',
  'class_names': PASCAL_CLASSES,
  'label_map': None
})
```

add test_config under the end of ```**YOLACT v1.0 CONFIGS**``` part <br/>
```
myDataset_test = dataset_base.copy({
  'name': '<your desired name>',
  'dataset': myDataset_test,
  'num_classes': 21,
  'max_size': 550,      # recommended by official github
})
```

put [my pretrained weight](https://drive.google.com/file/d/1DMFNCl4P3ScrsMydrCowt03d1rQPUnlH/view?usp=sharing) in ./weights/ folder

evaluate my model <br/>
```
python3 eval.py --trained_model=weights/yolact_plus_resnet50_myDataset_1375_57786_interrupt.pth --config=test_config --output_coco_json --dataset=myDataset_test
```

the above command will generate 2 .json file in ./results/ folder, and the **mask_detections.json** is what we needed
