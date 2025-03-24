import cv2
import numpy as np

def load_image(path: str) -> np.ndarray:
    """
    Loads an image from path using OpenCV.
    Returns: numpy.ndarray with dtype uint8 and shape (height, width, channels)
    """
    return cv2.imread(path)  # Returns numpy.ndarray (uint8)

def save_image(path: str, image: np.ndarray): 
    """
    Saves an image using OpenCV.
    Args:
        path: str, path to save image to
        image: numpy.ndarray with dtype uint8 and shape (height, width, channels)
    """
    cv2.imwrite(path, image)  # Expects numpy.ndarray (uint8)


def show_image(image: np.ndarray): 
    """
    Displays an image using OpenCV.
    """
    # map min and max values to 0 and 255
    image = (image - np.min(image)) / (np.max(image) - np.min(image)) * 255
    image = image.astype(np.uint8)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
