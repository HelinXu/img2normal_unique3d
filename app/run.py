if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.curdir)
    if 'CUDA_VISIBLE_DEVICES' not in os.environ:
        os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    os.environ['TRANSFORMERS_OFFLINE']='0'
    os.environ['DIFFUSERS_OFFLINE']='0'
    os.environ['HF_HUB_OFFLINE']='0'
    os.environ['GRADIO_ANALYTICS_ENABLED']='False'
    os.environ['HF_ENDPOINT']='https://hf-mirror.com'
    import torch
    torch.set_float32_matmul_precision('medium')
    torch.backends.cuda.matmul.allow_tf32 = True
    torch.set_grad_enabled(False)

    from app.custom_models.normal_prediction import predict_normals
    import PIL


    image_path = "data/test.png"
    image = PIL.Image.open(image_path)
    normals = predict_normals(image)
    normals[0].save("data/output.png")
    print("Output saved to data/output.png")