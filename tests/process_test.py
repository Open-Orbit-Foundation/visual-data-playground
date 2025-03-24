import yaml
import cv2
import numpy as np
from custom_modules.process import luminance
from custom_modules.io import show_image

def test_luminance():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)

    img = cv2.imread(config["test_img_path"])
    assert img is not None

    luminance_img = luminance(img)
    # map min and max values to 0 and 255
    luminance_img = (luminance_img - np.min(luminance_img)) / (np.max(luminance_img) - np.min(luminance_img)) * 255
    luminance_img = luminance_img.astype(np.uint8)
    show_image(luminance_img)


# def test_color_transform_RGB_YCoCg():
#     with open("config.yml", "r") as f:
#         config = yaml.safe_load(f)

#     img = cv2.imread(config["test_img_path"])
#     assert img is not None

#     ycc_opencv = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
#     ycc = color_transform_RGB_YCbCr(img)

#     assert ycc.dtype == np.uint8
#     assert ycc_opencv.dtype == np.uint8

#     # for i in range(ycc.shape[2]):
#     #     print(f"Channel {i}")
#     #     ycc_channel = ycc[:, :, i]
#     #     ycc_opencv_channel = ycc_opencv[:, :, i]
#     #     assert np.allclose(ycc_channel, ycc_opencv_channel)

#     show_image(np.concatenate([ycc, ycc_opencv], axis=0))

