import Error
import R_CNN

"""
    The purpose of this class is to store the images in an array and detect if there 
    is any error that occurs within the file such as file size, file type, name, etc.
"""
class ImageList:
    imageList = []
    error = Error()
    rcnn = R_CNN()

    """
    Get images from list.

    @param img: Images which are provided by user
    """
    def FormatValidation(img):
        pass
