from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
	'''	Create a flask app which runs on the 5000 port
	Imports the PLM Script from the source folder
	'''
	logger.debug("Starting Flask Server")
	from src import *

	flaskAppInstance.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)