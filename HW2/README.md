# Object detection

clone the yolo repo<br/>
```git clone https://github.com/AlexeyAB/darknet.git```

change the make file to enable GPU<br/>
```
GPU=1
CUDNN=1
CUDNN_HALF=0
OPENCV=1
```

make darknet<br/>
```make```

download the number.data file, digit.cfg file and weights [here](https://drive.google.com/drive/folders/1tJ12o1Q7DQZnvXuE8Gmc835qIs6zmHTK?usp=sharing)
and put above files in darknet folder

run on multiple imgaes and get json file<br/>
```./darknet detector test voc.names digit.cfg digit_last.weights -dont_show -out res.json < [path of .txt containing images]```

run on single images and see results<br/>
```./darknet detecotr test voc.names digit.cfg digit_last.weights -dont_show [path to your image]```
