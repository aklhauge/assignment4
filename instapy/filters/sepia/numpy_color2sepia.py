import time
import numpy as np


def convert_to_sepia(image):
    """Converts an image to sepia using a numpy implementation

        Args:
            image (Array): an array representation of the image that is to be converted
        Returns:
            Array: an array representation of the image in sepia
    """

    sepia_matrix = [[0.393, 0.769, 0.189],
                [ 0.349 , 0.686 , 0.168],
                [ 0.272 , 0.534 , 0.131]]
    sepia_array = np.array(sepia_matrix)

    sepia_image = image
    sepia_image = np.dot(sepia_image, sepia_array.T)
    sepia_image = np.minimum(sepia_image, 255)
    return sepia_image


def calculate_runtime(image, experiment_repeats):
    """Calculates the average runtime of the time used to convert an image to sepia
       The result are being printed to the terminal

        Args:
            image (Array): an array representation of the image that is to be converted
            experiment_repeats (int): the number of times to calculate the runtime
    """

    sum_runtime = 0

    for i in range(experiment_repeats):
        start_time = time.time()
        convert_to_sepia(image)
        end_time = time.time()
        runtime = end_time - start_time
        sum_runtime += runtime

    average_runtime = sum_runtime/experiment_repeats
    print("\nAverage runtime over {} runs: {:.4} s\n".format(experiment_repeats, average_runtime))
