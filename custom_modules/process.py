import cv2
import numpy as np

def luminance(image: np.ndarray) -> np.ndarray:
    """
    Calculate the luminance of an image.
    """
    return 0.2126*image[:, :, 0] + 0.7152*image[:, :, 1] + 0.0722*image[:, :, 2]


# def color_transform_RGB_YCbCr(image: np.ndarray) -> np.ndarray:
#     """
#     My implementation of the reversible color transform, described in the Jpeg 2000
#     Simply taking RGB space and converting it to YCoCg space.     
#     Sources:  
#     - https://en.wikipedia.org/wiki/YCbCr
#     - Note: Coefficents are from BT.709
#     """

#     coefficients = np.array([
#         [0.2126, 0.7152, 0.0722],
#         [-0.1146, -0.3854, 0.5],
#         [0.5, -0.4542, -0.0458] 
#     ])

#     image_float = image.astype(np.float64)
#     YCC = np.zeros_like(image_float)
    
#     for i in range(3):  # For each output channel
#         for j in range(3):  # For each input channel
#             YCC[:, :, i] += coefficients[i, j] * image_float[:, :, j]
    
#     YCC = np.clip(YCC, 0, 255).astype(np.uint8)
#     return YCC


