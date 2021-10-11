import instapy.filters.grayscale.python_color2gray as py_g
import instapy.filters.grayscale.numpy_color2gray as np_g
import instapy.filters.grayscale.numba_color2gray as nu_g
import instapy.filters.sepia.python_color2sepia as py_s
import instapy.filters.sepia.numpy_color2sepia as np_s
import instapy.filters.sepia.numba_color2sepia as nu_s


def runtime(color, implementation, image):
    """Calculates the average runtime of the time used to convert an image
       The result are being printed to the terminal

        Args:
            color (String): a value that tells if the image is converted to grayscale or sepia
            implementation (String): a value that tells which implementation to use
            image (Array): an array representation of the image that is to be converted
    """
    if color == "gray":
        if implementation == "python":
            py_g.calculate_runtime(image, 3)
        elif implementation == "numpy":
            np_g.calculate_runtime(image, 3)
        elif implementation == "numba":
            nu_g.calculate_runtime(image, 3)
    elif color == "sepia":
        if implementation == "python":
            py_s.calculate_runtime(image, 3)
        elif implementation == "numpy":
            np_s.calculate_runtime(image, 3)
        elif implementation == "numba":
            nu_s.calculate_runtime(image, 3)
