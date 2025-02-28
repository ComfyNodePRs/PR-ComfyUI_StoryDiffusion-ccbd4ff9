import yaml
import torch
from diffusers import StableDiffusionXLPipeline, DiffusionPipeline, AutoPipelineForText2Image, StableDiffusionPipeline
from .pipeline import PhotoMakerStableDiffusionXLPipeline
#from .pipeline_v2 import PhotoMakerStableDiffusionXLPipeline as PhotoMakerStableDiffusionXLPipelineV2
import os
import sys
import diffusers
dif_version = str(diffusers.__version__)
dif_version_int= int(dif_version.split(".")[1])
dir_path = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.dirname(dir_path)
file_path = os.path.dirname(path_dir)

def get_instance_path(path):
    instance_path = os.path.normpath(path)
    if sys.platform == 'win32':
        instance_path = path.replace('\\', "/")
    return instance_path

original_config_file=get_instance_path(os.path.join(path_dir,'config','sd_xl_base.yaml'))
loras_path = get_instance_path(os.path.join(path_dir,"config","lora.yaml"))

def get_lora_dict():
    # 打开并读取YAML文件
    with open(loras_path, 'r', encoding="UTF-8") as stream:
        try:
            # 解析YAML文件内容
            data = yaml.safe_load(stream)

            # 此时 'data' 是一个Python字典，里面包含了YAML文件的所有数据
            # print(data)
            return data

        except yaml.YAMLError as exc:
            # 如果在解析过程中发生了错误，打印异常信息
            print(exc)

datas = get_lora_dict()
lora_lightning_list = datas["lightning_xl_lora"]


def load_models(path,model_type,single_files,use_safetensors,photomaker_path,lora,lora_path,trigger_words,lora_scale):
    photoname=os.path.split(photomaker_path)[-1]
    if model_type == "txt2img":
        if single_files:
            if dif_version_int>=28:
                pipe = StableDiffusionXLPipeline.from_single_file(
                    pretrained_model_link_or_path=path, original_config=original_config_file, torch_dtype=torch.float16)

            else:
                pipe = StableDiffusionXLPipeline.from_single_file(
                    pretrained_model_link_or_path=path, original_config_file=original_config_file, torch_dtype=torch.float16
                )

        else:
            pipe = StableDiffusionXLPipeline.from_pretrained(
                path, torch_dtype=torch.float16,use_safetensors=use_safetensors
            )

        if lora != "none":
            if lora in lora_lightning_list:
                pipe.load_lora_weights(lora_path)
                pipe.fuse_lora()
            else:
                pipe.load_lora_weights(lora_path, adapter_name=trigger_words)
                pipe.fuse_lora(adapter_names=[trigger_words, ], lora_scale=lora_scale)

    elif model_type == "img2img":

        if single_files:
            # print("loading from a single_files")
            if dif_version_int >= 28:
                pipe = PhotoMakerStableDiffusionXLPipeline.from_single_file(
                    pretrained_model_link_or_path=path, original_config=original_config_file,
                    torch_dtype=torch.float16, use_safetensors=use_safetensors)
            else:
                pipe = PhotoMakerStableDiffusionXLPipeline.from_single_file(
                    pretrained_model_link_or_path=path, original_config_file=original_config_file,
                    torch_dtype=torch.float16, use_safetensors=use_safetensors
                )
        else:
            pipe = PhotoMakerStableDiffusionXLPipeline.from_pretrained(
                path, torch_dtype=torch.float16, use_safetensors=use_safetensors
            )
        pipe.load_photomaker_adapter(
            photomaker_path,
            subfolder="",
            weight_name=photoname,
            trigger_word="img"  # define the trigger word
        )
        # else:
        #     if single_files:
        #         # print("loading from a single_files")
        #         if dif_version_int >= 28:
        #             pipe = PhotoMakerStableDiffusionXLPipelineV2.from_single_file(
        #                 pretrained_model_link_or_path=path, original_config=original_config_file,
        #                 torch_dtype=torch.float16, use_safetensors=use_safetensors)
        #         else:
        #             pipe = PhotoMakerStableDiffusionXLPipelineV2.from_single_file(
        #                 pretrained_model_link_or_path=path, original_config_file=original_config_file,
        #                 torch_dtype=torch.float16, use_safetensors=use_safetensors
        #             )
        #     else:
        #         pipe = PhotoMakerStableDiffusionXLPipelineV2.from_pretrained(
        #             path, torch_dtype=torch.float16, use_safetensors=use_safetensors
        #         )
        #     # define the trigger word
        #     pipe.load_photomaker_adapter(
        #         photomaker_path,
        #         subfolder="",
        #         weight_name=photoname,
        #         trigger_word="img",  
        #         pm_version= 'v2',
        #     )
        if lora != "none":
            if lora in lora_lightning_list:
                pipe.load_lora_weights(lora_path)
                pipe.fuse_lora()
            else:
                pipe.load_lora_weights(lora_path, adapter_name=trigger_words)
                pipe.fuse_lora(adapter_names=[trigger_words, ], lora_scale=lora_scale)


    else:
        raise f"using{model_type}node,must choice{model_type}type in model_loader node"
    return pipe

