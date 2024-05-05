from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "3fb8d956837645f0bcd70e14e2d61d97"
publish_iteration_name = "Iteration3"
projectId = "8f518040-5867-4843-8f82-08f7cd745422"
ENDPOINT="https://customwebcasts-prediction.cognitiveservices.azure.com/"
