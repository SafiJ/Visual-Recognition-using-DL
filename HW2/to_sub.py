import json
import cv2

all_info = []
with open('darknet/res.json') as fp:
    data = json.load(fp)
    for info in data:
	    img = cv2.imread(info['filename'])
	    H, W, _ = img.shape
	    bbox = []
	    score = []
	    label = []
	    for idx in range(len(info['objects'])):
		    cx = info['objects'][idx]['relative_coordinates']['center_x']
		    cy = info['objects'][idx]['relative_coordinates']['center_y'] 
		    w = info['objects'][idx]['relative_coordinates']['width']
		    h = info['objects'][idx]['relative_coordinates']['height']
		    conf = info['objects'][idx]['confidence']
		    y1 = cy - h/2
		    x1 = cx - h/2
		    y2 = cy + h/2
		    x2 = cx + h/2
		    _bbox = [y1*H, x1*W, y2*H, x2*W]
		    bbox.append(_bbox)
		    score.append(conf)
		    _label = info['objects'][idx]['class_id']
		    if _label == 0:
			    label.append(10)
		    else:
		        label.append(_label)
	    door = {'bbox':bbox, 'score':score, 'label':label}
	    all_info.append(door)
	
    with open('result.json', 'w') as fw:
	    json.dump(all_info, fw)
