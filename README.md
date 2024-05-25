
# Image Resizer using OpenCV

## Overview

This Python script resizes an image using the OpenCV library. It reads an image file, resizes it based on a scale percentage, and saves the resized image to a new file.

## Requirements

- Python 3.x
- OpenCV library (`pip install opencv-python`)

## Usage

1. Ensure you have an image file in the same directory as the script.
2. Run the script with the following command:

```bash
python resize_image.py
```

Replace `resize_image.py` with the name of your script if it's different.

3. The script will load the image specified in the `image_path` variable and resize it based on the `scale_percent`.
4. The resized image will be saved as "new_image.jpeg" in the same directory.

## Parameters

- `image_path`: Path to the input image file.
- `scale_percent`: Percentage by which the image will be scaled. Default is set to 50%.
- `output_file`: Path to save the resized image. Default is "new_image.jpeg" in the current directory.

## Example

```python
# Resize an image with default parameters
import cv2

image = cv2.imread("images.jpeg", cv2.IMREAD_UNCHANGED)
scale_percent = 50
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)
output = cv2.resize(image, (new_height, new_width))
cv2.imwrite("new_image.jpeg", output)
cv2.waitKey(0)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Notes

- Ensure the image file exists in the specified path before running the script.
- The script supports various image formats, including JPEG, PNG, and others, as long as they are supported by OpenCV.
```
