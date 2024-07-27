This repo takes as input an image (square), and produces as output the normal map (2048x2048 when using upsamling modules as in the original code).

To run the demo, first download the ckpt from Hugglingface (https://huggingface.co/spaces/Wuvin/Unique3D/tree/main/ckpt) and put it under the root. Then run the following command:

```bash
python app/run.py
```

This code is mostly based on Unique3D. See the original repo for installation and usage instructions.

```
.
├── app
├── ckpt                                               # download from huggingface first.
│   ├── image2normal
│   │   ├── feature_extractor
│   │   │   └── preprocessor_config.json
│   │   ├── image_encoder
│   │   │   ├── config.json
│   │   │   └── model.safetensors
│   │   ├── model_index.json
│   │   ├── scheduler
│   │   │   └── scheduler_config.json
│   │   ├── unet
│   │   │   ├── config.json
│   │   │   └── diffusion_pytorch_model.safetensors
│   │   ├── unet_state_dict.pth
│   │   └── vae
│   │       ├── config.json
│   │       └── diffusion_pytorch_model.safetensors
│   └── realesrgan-x4.onnx
├── custum_3d_diffusion
├── data
│   ├── output.png
│   └── test.png
├── README.md
└── scripts
```