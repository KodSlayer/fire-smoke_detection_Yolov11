#Scrip to save the results back to your folder

import shutil

# Copy to your Google Drive instead
shutil.copytree(
    '/content/runs/detect/fire_smoke_yolo11',
    '/content/drive/MyDrive/fire_smoke_results'
)
print("✅ Saved to Google Drive!")
