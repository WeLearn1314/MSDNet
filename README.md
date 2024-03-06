# MSDNet
A new multi-scale CNN with pixel-wise attention for image denoising (MSDNet) by Jibin Deng*, Chaohua Hu has been published in Signal, Image and Video Processing, 2023.
 
# Prerequisites:

python

tensorflow

keras

opencv-python

scikit-image

# Denoising Training
For train the MSDNet, please run:

python mainimprovement.py

# Denoising Testing
For test the MSDNet, please run:

python mainimprovement.py --pretrain sigma (e.g., 15, 25 and 50)/model_50.h5 --only_test True

# Denoising Datasets
The gray train dataset "Train400" you can download here:

https://download.csdn.net/download/qq_41104871/87646484

The color train dataset "BSD400" you can download here:

https://download.csdn.net/download/qq_41104871/87647333

# Deraining Datasets
The dataset "Rain100H" and "Rain100L" you can download here:

https://1drv.ms/f/s!AqLfQqtZ6GwGgep-hgjLxkov2SSZ3g