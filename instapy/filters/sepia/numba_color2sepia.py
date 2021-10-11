import time
from numba import jit

@jit(nopython=True)
def convert_to_sepia(image):
    """Converts an image to sepia using a numba implementation

        Args:
            image (Array): an array representation of the image that is to be converted
        Returns:
            Array: an array representation of the image in sepia
    """

    (height, width) = image.shape[:2]
    sepia_matrix = [[0.393, 0.769, 0.189],
                [ 0.349 , 0.686 , 0.168],
                [ 0.272 , 0.534 , 0.131]]

    sepia_image = image
    max_value = 255
    for h in range(height):
        for w in range(width):
            (r, g, b) = sepia_image[h][w]

            red = int((r*sepia_matrix[0][0])+(g*sepia_matrix[0][1])+(b*sepia_matrix[0][2]))
            red = min(red, max_value)

            green = int((r*sepia_matrix[1][0])+(g*sepia_matrix[1][1])+(b*sepia_matrix[1][2]))
            green = min(green, max_value)

            blue = int((r*sepia_matrix[2][0])+(g*sepia_matrix[2][1])+(b*sepia_matrix[2][2]))
            blue = min(blue, max_value)

            sepia_image[h][w] = (red, green, blue)

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
