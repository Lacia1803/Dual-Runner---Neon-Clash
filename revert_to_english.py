import zipfile
import os
import shutil

zip_path = r'c:\Users\Lacia\Downloads\Agate-Game-Project-master.zip'
base_in_zip = 'Agate-Game-Project-master/'

with zipfile.ZipFile(zip_path, 'r') as z:
    for info in z.infolist():
        if info.filename.endswith(('.unity', '.prefab', '.asset', '.mat')):
            if info.filename.startswith(base_in_zip):
                target_path = info.filename[len(base_in_zip):]
                if not target_path:
                    continue
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                with z.open(info) as src, open(target_path, 'wb') as dst:
                    shutil.copyfileobj(src, dst)

print("Restored all assets to original English state.")
