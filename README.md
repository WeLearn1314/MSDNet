# MSDNet
This website shares the code of the "A new multi-scale CNN with pixel-wise attention for image denoising" finished by Jibin Deng*, Chaohua Hu, , 2023.
 
# Prerequisites:

python == 3.6.2

tensorflow == 2.0.0

keras == 2.3.1

opencv-python == 4.5.5.62

scikit-image == 0.17.2

# Training
For train the MSDNet, please run:

python mainimprovement.py

# Testing
For test the MSDNet, please run:

python mainimprovement.py --pretrain sigma/model_50.h5 --only_test True