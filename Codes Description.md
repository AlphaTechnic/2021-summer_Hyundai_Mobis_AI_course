# Goals

- 자동차 여부 인식 시스템 구현 (Object Detection)

# Codes and Algorithms

## `train_ssd.py`

```python
if __name__ == '__main__':
    timer = Timer()

    logging.info(args)
	..
    train_transform = TrainAugmentation(config.image_size, config.image_mean, config.image_std)
    target_transform = MatchPrior(config.priors, config.center_variance,
                                  config.size_variance, 0.5)

    test_transform = TestTransform(config.image_size, config.image_mean, config.image_std)

    logging.info("Prepare training datasets.")
	..
    logging.info("Build network.")
	..


    logging.info(f"Start training from epoch {last_epoch + 1}.")
    for epoch in range(last_epoch + 1, args.num_epochs):
        scheduler.step()
        train(train_loader, net, criterion, optimizer,
              device=DEVICE, debug_steps=args.debug_steps, epoch=epoch)
        
		..
```

- `train` 함수 : 설정한 net(default : SSD-mobilenet-v1)로 학습한다.





## `onnx_export.py`

```python
#
# converts a saved PyTorch model to ONNX format
# 
import os
import argparse

import torch
import torchvision.models as models


# parse command line
..

# format input model path
..

# set the device
..

# load the model checkpoint
..

# create the model architecture
print('using model:  ' + arch)
print('num classes:  ' + str(num_classes))

model = models.segmentation.__dict__[arch](num_classes=num_classes,
                                           aux_loss=None,
                                           pretrained=False,
                                           export_onnx=True)
																 
# load the model weights
..

# create example image data
..

# format output model path
if not opt.output:
   opt.output = arch + '.onnx'

if opt.model_dir and opt.output.find('/') == -1 and opt.output.find('\\') == -1:
   opt.output = os.path.join(opt.model_dir, opt.output)

# export the model
input_names = [ "input_0" ]
output_names = [ "output_0" ]

print('exporting model to ONNX...')
torch.onnx.export(model, input, opt.output, verbose=True, input_names=input_names, output_names=output_names)
print('model exported to:  {:s}'.format(opt.output))
```

- converts a saved PyTorch model to ONNX format
- PyTorch로 생성된 모델을 ONNX 포맷으로 바꾸게 되면 TensorRT에 적용할 수 있다.
- TensorRT는 학습된 딥러닝 모델을 최적화하여 NVIDIA GPU 상에서의 추론 속도를 수배 ~ 수십배 까지 향상시켜 딥러닝 서비스를 개선하는데 도움을 줄 수 있는 모델 최적화 엔진이다.



## `detectnet.py`

```python
import jetson.inference
import jetson.utils

import argparse
import sys

# parse the command line
..

# load the object detection network
..

# create video sources & outputs
..

# process frames until the user exits
while True:
	# capture the next image
	img = input.Capture()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, overlay=opt.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))

	for detection in detections:
		print(detection)

	# render the image
	..

	# update the title bar
	..

	# print out performance info
	..

	# exit on input/output EOS
	..
```

![train_ssd](C:\Users\juho3\Desktop\2021-summer_Hyundai_Mobis_AI_course\img\train_ssd.jpg)

- capture the next image
- detect objects in the image (with overlay)


