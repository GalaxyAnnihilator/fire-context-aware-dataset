# fire-context-aware-dataset
A dataset created for surveying/training Visual Language Models (VLM) to understand fire and its contextual environment. The dataset categorizes images into three classes: no fire, dangerous fire, and controlled fire.

## Dataset Structure

```
fire-context-aware-dataset/
├── original_dataset/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── labels.csv
```

## Labels Format

The `labels.csv` file contains three columns:
- `image_path`: Path to the image file
- `label`: Classification label (no fire/dangerous fire/controlled fire)
- `caption`: Detailed description of the image scene

Example:
```csv
image_path,label,caption
original_dataset/image1.jpg,no fire,"The image shows a cozy living room with a fireplace, a potted plant, a lamp, and a painting on the wall. The room appears to be well-lit and decorated."
original_dataset/image37.jpg,controlled fire,"The image shows a cozy dining room with a lit fireplace, wooden chairs around a table set for a meal, and a chandelier hanging from the ceiling. The room has a warm ambiance with candles and decorative elements."
original_dataset/image1025.jpg,dangerous fire,"The image shows a kitchen with flames coming from the oven and microwave, indicating a dangerous fire situation."
```

![Sample Batch 1](sample1.png)

![Sample Batch 2](sample2.png)

## 📚 Dataset Sources & Credits

This project uses datasets from the following sources:

1. **IDFire: Image Dataset for Indoor Fire Load Recognition**  
   Source: [IEEE DataPort](https://ieee-dataport.org/documents/idfire-image-dataset-indoor-fire-load-recognition)  
   Authors: Sheraz Ahmed, Andreas Dengel et al.  
   License: [DataPort Terms of Use](https://ieee-dataport.org/terms-of-use)  
   Description: A curated dataset containing indoor fire and no-fire scenarios for fire load recognition.

2. **Home Fire Dataset**  
   Source: [GitHub - PengBo0/Home-fire-dataset](https://github.com/PengBo0/Home-fire-dataset)  
   Author: Pengbo Liu  
   License: MIT License (as stated on the repository)  
   Description: A dataset of home environments containing fire and no-fire images used for fire classification and detection tasks.

3. **DFireDataset**  
   [GitHub - gaiasd/DFireDataset](https://github.com/gaiasd/DFireDataset)  
   Author: Gaia Scagnetto  
   License: Creative Commons Attribution 4.0 International (CC BY 4.0)  
   Description: Dataset designed for detecting fires in complex scenes including blurred, nighttime, and outdoor images.

4. **Fire Detection from Images**  
   [GitHub - robmarkcole/fire-detection-from-images](https://github.com/robmarkcole/fire-detection-from-images)  
   Author: Rob Mark Cole  
   License: MIT License  
   Description: A lightweight fire dataset used in early CNN-based fire detection research, with cropped fire/non-fire examples.

All datasets are used strictly for education, research and non-commercial purposes.
