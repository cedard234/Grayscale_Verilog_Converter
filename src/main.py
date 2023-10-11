# convert a single grayscale image to verilog format

import sys
import os
import numpy as np
import cv2

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 grayscale_convert_single.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print("Error: image_path is not a file")
        sys.exit(1)

    # read image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: failed to read image")
        sys.exit(1)

    # convert to 8-bit unsigned integer
    img = img.astype(np.uint8)
        
    image_path = os.path.basename(image_path)
    image_name = os.path.splitext(image_path)[0]
    height, width = img.shape
    with open("build/"+image_name+".sv", 'w') as f:
        f.write("module image"+image_name+"(output reg [7:0] pixel ["+  str(height-1) + ":0][" + str(width-1) +  ":0])\n")
        # image size
        f.write("// module instance for image:  " + image_path + "\n")
        for (i,j) in np.ndindex(img.shape):
            # write into .v file
            f.write("    assign pixel["+str(i)+"]["+str(j)+"] = 8'h{:02x};\n".format(img[i,j]))
        f.write("endmodule\n")
    f.close()
    print("Image " + str(image_path) +  " converted to verilog format")


if __name__ == '__main__':
    main()

