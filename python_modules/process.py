import cv2
import numpy as np

def reversible_color_transform(image: np.ndarray) -> np.ndarray:
    """
    My implementation of the reversible color transform, described in the Jpeg 2000
    Simply taking RGB space and converting it to YCoCg space.     
    Sources:  
    - https://en.wikipedia.org/wiki/YCoCg
    """

    R, G, B = np.split(image, 3, axis=-1)
    Co = R - B  # Difference between R and B channels
    tmp = B + Co/2  # B + (R-B)/2 = (R+B)/2
    Cg = G - tmp  # G - (R+B)/2
    Y = tmp + Cg/2  # (R+B)/2 + (G-(R+B)/2)/2 = (R + 2G + B)/4

    # debug
    print(Y.shape)
    print(Co.shape)
    print(Cg.shape)
   
    return np.concatenate([Y, Co, Cg], axis=-1)


