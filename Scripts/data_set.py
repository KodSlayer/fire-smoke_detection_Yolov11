#This is the Script to unzip the folder from the drive 
# after connecting to google colab
# Make sure to update the path accordingly

from google.colab import drive
drive.mount('/content/drive')

import zipfile
zip_path = '/content/drive/MyDrive/Fire-Smoke-Detection-Yolov11-2.zip'  # adjust if needed
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('/content/')

print("✅ Dataset ready!")
