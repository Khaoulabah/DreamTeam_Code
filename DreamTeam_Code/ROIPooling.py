import ImageList
import ImageDetails


"""
    This class classifies framed items, into objects using the user provided database. 
"""
class ROIPooling:
    list = ImageList()
    imageDetails = ImageDetails()
    
    """
    Classify item types of image details.
    
    @param img: Image item retrieved from R-CNN class 
    """
    def ClassifyItemType(img):
        return img

    """
    Frame objects on images
    
    @param item: Image item retrieved from R-CNN class 
    """
    def FrameImage(item):
        pass
