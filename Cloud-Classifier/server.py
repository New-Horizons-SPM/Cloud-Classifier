from flask import Flask, request
import classifier

app = Flask(__name__)
   
@app.route('/test')
def test():
    return "hello"

@app.route('/predict', methods=['POST'])
def predict():
    """
        Incoming data should be a dictionary like:
        data = {
                    'scanData'  : np.array                          # np.array of the raw scan data (Z channel)
                    'scanSize'  : (w,h)                             # Tuple containing the width and height of the scan frame (m)
                    'modelName' : "<Name of trained model>"         # Name of your previously trained model to run this image through. "" means the default model
                }
    """
    data = request.json
    prediction, error = classifier.predict(data)                    # Returns prediction and error message if there was one. If no errors, error = None

    return {"prediction": prediction,
            "error"     : error}, 200

@app.route('/train_model', methods=['POST'])
def trainModel():
    """
        Incoming data should be a dictionary like:
        data = {
                    'scanData'  : [np.array, ...]                   # List of np.array of the raw scan data (Z channel)
                    'scanSize'  : [(w,h), ...]                      # List of tuples containing the width and height of each scan frame (m)
                    'modelName' : "<Name of trained model>"         # Name of your new model. If a model with the same name exists, it will be overwritten.
                }
    """
    data    = request.json
    success = classifier.train(data)                                # If successful, error = None, otherwise error is a string

    return {"success": success}, 200

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=3000, debug=True)                 # Listen on localhost:3000