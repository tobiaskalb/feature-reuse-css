<div align="center">

# Principles of Forgetting in Domain-Incremental Semantic Segmentation in Adverse Weather Conditions

[![Paper](https://img.shields.io/badge/arXiv-2303.14115-brightgreen)](https://arxiv.org/abs/2303.14115)
[![Conference](https://img.shields.io/badge/CVPR-2023-blue)]()

</div>

This repository contains information to reproduce our experiments. 
```

@inproceedings{kalb2023featurereuse,
  title={Principles of Forgetting in Domain-Incremental Semantic Segmentation in Adverse Weather Conditions},
  authors={Kalb, Tobias and Beyerer, J\"urgen},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2023}
}

```

# Augmentations
The data augmentation pipelines we used are described in the [yaml-Files](transformations/). These include:
- [basic augmentation](transformations/base_cityscapes.yaml) for Cityscapes 
- [basic augmentations](transformations/acdc_cs.yaml) used for training on the ACDC subsets
- [Distortion](transformations/cs_distort.yaml)
- [Gaus](transformations/cs_blur_gaus.yaml)
- [Noise](transformations/cs_noise.yaml)
- [AutoAlbum](transformations/cs_autoaug.yaml) with the corresonoding [search configuration]((transformations/autoalbument/search-cityscapes/)) and the resulting [augmentation config](https://github.com/tobiaskalb/feature-reuse-css/blob/main/transformations/autoalbument/cityscapes_auto.json).

As they directly contain our used arguments for the Albumentations transformations, they can also be directly loaded as composed transformations, as shown in ourr [sample notebook](sample_transforms.ipynb).

# Checkpoints
The checkpoints for ResNet50 trained with various SSL methods can be found in their respective repositories:
-  [MoCo v3](https://github.com/facebookresearch/moco-v3)
-  [DINO](https://github.com/facebookresearch/dino)
-  [Barlow Twins](https://github.com/facebookresearch/barlowtwins)
-  [SwAV](https://github.com/facebookresearch/swav)

For ErfNet trained with MoCo v3 and DINO the checkpoints can be found here: https://drive.google.com/drive/folders/1HH4F7gMm4FxqyZcgNBuwicrCFb0r40mh?usp=sharing.

# Model Sources
The segmentation models and the corresponding ImageNet weights were based on the following implementations:
- DeepLabV3+ from [github.com/qubvel/segmentation_models.pytorch](https://github.com/qubvel/segmentation_models.pytorch) (decoder_channels=512, encoder_output_stride= 8, encoder_name= "resnet50")
- ERFNet from [github.com/Eromera/erfnet_pytorch](https://github.com/Eromera/erfnet_pytorch)
- SegFormer-B2 from [HuggingFace](https://huggingface.co/docs/transformers/model_doc/segformer)
- RTFormer-Base from [PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg/tree/develop/configs/rtformer)
- BiSeNetV2 from [github.com/CoinCheung/BiSeNet](https://github.com/CoinCheung/BiSeNet)
- SegHRNet-w48 from [github.com/HRNet/HRNet-Semantic-Segmentation](https://github.com/HRNet/HRNet-Semantic-Segmentation/tree/pytorch-v1.1)


