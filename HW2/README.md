# Object detection

clone the yolo repo
```git clone https://github.com/AlexeyAB/darknet.git```

download the number.data file, digit.cfg file and weights in [here](https://drive.google.com/drive/folders/1tJ12o1Q7DQZnvXuE8Gmc835qIs6zmHTK?usp=sharing)
and put above files in darknet folder

run on multiple imgaes and get json file
```./darknet detector test voc.names digit.cfg digit_last.weights -dont_show -out res.json < [path of .txt containing images]```

run on single images and see results
```./darknet detecotr test voc.names digit.cfg digit_last.weights -dont_show [path to your image]```
