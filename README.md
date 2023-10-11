# Grayscale Verilog Converter

## Introduction
This is a python-based utility to convert a grayscale image into verilog code.
I got the idea to develop this little project because generating verilog code for grayscale image can be very tedious. I have done it throughout another project [AcceleNetor. Check it out](https://github.com/cedard234/AcceLeNetor/tree/master) if you are interested in FPGA based neural network accelerator.

## Dependencies
- Python 3.6 or above
- numpy
- opencv-python
These dependencies have been listed in requirements.txt file.

## How to use?
1. Clone this repository
2. Run ```make requirements``` to install dependencies.
3. Run ```make test``` to test whether the test images have been successfully converted into verilog code or not.
> The test images are stored in ```test/``` directory. They are originally from [this repository](https://github.com/ZFTurbo/Verilog-Generator-of-Neural-Net-Digit-Detector-for-FPGA). Thanks all the contributors for providing these images.

4. Building images
    1. If you want to make a single image, run ```make image image=<path_to_image>```. The result will be stored in ```build``` directory.
    2. If you want to run a batch of images, run ```make folder folder=<folder>```. The result will also be stored in ```build``` directory.
5. If you want to clean the build directory, run ```make clean```.
6. You can also run ```make``` if you want to see help message.

## Contact
If you have any questions, please feel free to contact me at ```wangdi1310@gmail.com```.