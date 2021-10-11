import time
import numpy as np


def convert_to_grayscale(image):
    """Converts an image to grayscaleusing a numpy implementation

        Args:
            image (Array): an array representation of the image that is to be converted
        Returns:
            Array: an array representation of the image in grayscale
    """

    (height, width) = image.shape[:2]
    grayscale_image = np.empty((height, width))
    grayscale_image[0:height, 0:width] = \
    np.sum((0.07, 0.72, 0.21)*image[0:height, 0:width], axis = 2)
    return grayscale_image


def calculate_runtime(image, experiment_repeats):
    """Calculates the average runtime of the time used to convert an image to grayscale
       The result are being printed to the terminal

        Args:
            image (Array): an array representation of the image that is to be converted
            experiment_repeats (int): the number of times to calculate the runtime
    """

    sum_runtime = 0

    for i in range(experiment_repeats):
        start_time = time.time()
        convert_to_grayscale(image)
        end_time = time.time()
        runtime = end_time - start_time
        sum_runtime += runtime

    average_runtime = sum_runtime/experiment_repeats
    print("\nAverage runtime over {} runs: {:.4} s\n".format(experiment_repeats, average_runtime))
