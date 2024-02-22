def predict(data):
    """
        Incoming data should be a dictionary like:
        data = {
                    'scanData'  : np.array                        # np.array of the raw scan data (Z channel)
                    'scanSize'  : (w,h)                           # Tuple containing the width and height of the scan frame (m)
                    'modelName' : "<Name of trained model>"       # Name of your previously trained model to run this image through. "" means the default model
                }
    """
    image = data['scanData']

    # Code to call model <modelName> and get prediction for image

    prediction = 7/10
    error = None

    return prediction, error

def train(data):
    """
        Incoming data should be a dictionary like:
        data = {
                    'scanData'  : [np.array, ...]                 # List of np.array of the raw scan data (Z channel)
                    'scanSize'  : [(w,h), ...]                    # List of tuples containing the width and height of each scan frame (m)
                    'modelName' : "<Name of trained model>"       # Name of your new model. If a model with the same name exists, it will be overwritten.
                }
    """
    images = data['scanData']

    # Code to synthesise data from good images
    # Code to train model and save as <modelName>

    success = True

    return success