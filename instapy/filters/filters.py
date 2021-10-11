import cv2
import instapy.filters.grayscale.python_color2gray as py_g
import instapy.filters.grayscale.numpy_color2gray as np_g
import instapy.filters.grayscale.numba_color2gray as nu_g
import instapy.filters.sepia.python_color2sepia as py_s
import instapy.filters.sepia.numpy_color2sepia as np_s
import instapy.filters.sepia.numba_color2sepia as nu_s


def grayscale_image(implementation, input_filename, output_filename=None):
    """Converts an image to grayscale

        Args:
            implementation (String): the implementation to be used
            input_filename (String): the filename of the image to be converted
            output_filename (String): the new filename of the converted image
                                      if it is to be saved
        Returns:
            Array: an array representation of the image in grayscale
    """

    image = cv2.imread(input_filename)
    if implementation == "py":
        image = py_g.convert_to_grayscale(image)
    elif implementation == "np":
        image = np_g.convert_to_grayscale(image)
    elif implementation == "nu":
        image = nu_g.convert_to_grayscale(image)
    image = image.astype("uint8")
    if output_filename != None:
        cv2.imwrite(output_filename, image)
    return image


def sepia_image(implementation, input_filename, output_filename=None):
    """Converts an image to sepia

        Args:
            implementation (String): the implementation to be used
            input_filename (String): the filename of the image to be converted
            output_filename (String): the new filename of the converted image
                                      if it is to be saved
        Returns:
            Array: an array representation of the image in sepia
    """

    image = cv2.imread(input_filename)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if implementation == "py":
        image = py_s.convert_to_sepia(image)
    elif implementation == "np":
        image = np_s.convert_to_sepia(image)
    elif implementation == "nu":
        image = nu_s.convert_to_sepia(image)
    image = image.astype("uint8")
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if output_filename != None:
        cv2.imwrite(output_filename, image)
    return image
