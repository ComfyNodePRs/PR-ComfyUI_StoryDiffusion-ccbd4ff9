# ComfyUI_StoryDiffusion
You can using StoryDiffusion in ComfyUI 

[中文说明](https://github.com/smthemex/ComfyUI_StoryDiffusion/edit/main/README-CN.md)
--
StoryDiffusion origin From: [link](https://github.com/HVision-NKU/StoryDiffusion)   
MS-Diffusion origin From: [link](https://github.com/MS-Diffusion/MS-Diffusion)
----
My ComfyUI node list：
-----

1、ParlerTTS node:[ComfyUI_ParlerTTS](https://github.com/smthemex/ComfyUI_ParlerTTS)     
2、Llama3_8B node:[ComfyUI_Llama3_8B](https://github.com/smthemex/ComfyUI_Llama3_8B)      
3、HiDiffusion node：[ComfyUI_HiDiffusion_Pro](https://github.com/smthemex/ComfyUI_HiDiffusion_Pro)   
4、ID_Animator node： [ComfyUI_ID_Animator](https://github.com/smthemex/ComfyUI_ID_Animator)       
5、StoryDiffusion node：[ComfyUI_StoryDiffusion](https://github.com/smthemex/ComfyUI_StoryDiffusion)  
6、Pops node：[ComfyUI_Pops](https://github.com/smthemex/ComfyUI_Pops)   
7、stable-audio-open-1.0 node ：[ComfyUI_StableAudio_Open](https://github.com/smthemex/ComfyUI_StableAudio_Open)        
8、GLM4 node：[ComfyUI_ChatGLM_API](https://github.com/smthemex/ComfyUI_ChatGLM_API)   
9、CustomNet node：[ComfyUI_CustomNet](https://github.com/smthemex/ComfyUI_CustomNet)           
10、Pipeline_Tool node :[ComfyUI_Pipeline_Tool](https://github.com/smthemex/ComfyUI_Pipeline_Tool)    
11、Pic2Story node :[ComfyUI_Pic2Story](https://github.com/smthemex/ComfyUI_Pic2Story)   
12、PBR_Maker node:[ComfyUI_PBR_Maker](https://github.com/smthemex/ComfyUI_PBR_Maker)      
13、ComfyUI_Streamv2v_Plus node:[ComfyUI_Streamv2v_Plus](https://github.com/smthemex/ComfyUI_Streamv2v_Plus)   
14、ComfyUI_MS_Diffusion node:[ComfyUI_MS_Diffusion](https://github.com/smthemex/ComfyUI_MS_Diffusion)   
15、ComfyUI_AnyDoor node: [ComfyUI_AnyDoor](https://github.com/smthemex/ComfyUI_AnyDoor)  
16、ComfyUI_Stable_Makeup node: [ComfyUI_Stable_Makeup](https://github.com/smthemex/ComfyUI_Stable_Makeup)  
17、ComfyUI_EchoMimic node:  [ComfyUI_EchoMimic](https://github.com/smthemex/ComfyUI_EchoMimic)   
18、ComfyUI_FollowYourEmoji node: [ComfyUI_FollowYourEmoji](https://github.com/smthemex/ComfyUI_FollowYourEmoji)   

NEW Update
---
--2024/07/26
--fix some bug,while ControlNet now uses community models.   
-- The base model now has only two options: using repo input or selecting the community model...
--Adjusting the model loading of MS has made the speed faster   


--2024/07/09    
--To fix the bug where MS diffusion cannot run continuously in the txt2img, it is necessary to enable the "reset_txt2img" of the loading model node to be Ture;   
--Fix the error in introducing modules, now change the model storage address to“ models/photomaker”, reuse the model, and avoid wasting hard disk space(the PT model is also located in the photometer directory);  
--Changing the method of selecting models now makes it more convenient to choose other diffusion models;    

--Add a Controlnet layout control button, which defaults to automatic programming.   
--Introducing Controlnet for dual character co image, supporting multi image introduction, 
--Add the function of saving and loading character models   
--It is known that when adding dual characters to the Wensheng diagram, it can only be run once. If you run it again, you need to fix the bug in the sampler or other options loaded on the model. There is currently no time to fix it;   


1.Installation
-----
  In the ./ComfyUI /custom_node directory, run the following:   
```
git clone https://github.com/smthemex/ComfyUI_StoryDiffusion.git
```  
  
2.requirements  
----
```
pip install -r requirements.txt
```

If the module is missing, please pip install   

3 Need  model 
----

You can directly fill in the repo, such as:"stablityai/table diffusion xl base-1.0", or select the corresponding model in the local diffuser menu (provided that you have the model in the "models/diffuser" directory), or you can directly select a single SDXL community model. The priority of repo or local diffusers is higher than that of individual community models.    

Supports all SDXL based diffusion models (such as "G161222/RealVisXL_V4.0", "sd-community/sdxl-flash"）， It also supports non SD models, such as ("stablediffusionapi/sdxl-unstable-diffusers-y", playground-v2.5-1024px-aesthetic）   
When using your local SDXL monomer model (for example: Jumpernaut XL_v9-RunDiffusionPhoto_v2. safetensors), please set local_diffusers to none and download the corresponding config files to run.  

--using dual role same frame function:      

photomaker-v1.bin    [link](https://huggingface.co/TencentARC/PhotoMaker/tree/main)   
photomaker-v2.bin    [link](https://huggingface.co/TencentARC/PhotoMaker-V2/tree/main)  (need  update code )
Need download "ms_adapter.bin" : [link](https://huggingface.co/doge1516/MS-Diffusion/tree/main)    
Need encoder model "laion/CLIP-ViT-bigG-14-laion2B-39B-b160k":[link](https://huggingface.co/laion/CLIP-ViT-bigG-14-laion2B-39B-b160k)   

```
├── ComfyUI/models/
|      ├──photomaker/
|             ├── photomaker-v1.bin
|             ├── photomaker-v2.bin
|             ├── ms_adapter.bin

```

3.2 offline  
You can fill in the absolute address of the diffusion model in repo, using "/"   

--using dual role same frame function:     
Fill in the absolute path of your local clip model in the "laion/CLIP ViT bigG-14-laion2B-39B-b160k" column, using "/". Please refer to the file structure demonstration below for the required files.        
```
├── Any local_path/
|     ├──CLIP ViT bigG-14-laion2B-39B-b160k/
|             ├── config.json
|             ├── preprocessor_config.json
|             ├──pytorch_model.bin.index.json
|             ├──pytorch_model-00001-of-00002.bin
|             ├──pytorch_model-00002-of-00002.bin
|             ├──special_tokens_map.json
|             ├──tokenizer.json
|             ├──tokenizer_config.json
|             ├──vocab.json
```
 
3.3 The model file example for dual role controllnet is as follows, which only supports SDXL community controllnet    
```
├── ComfyUI/models/controlne/   
|     ├──xinsir/controlnet-openpose-sdxl-1.0    
|     ├──xinsir/controlnet-scribble-sdxl-1.0   
|     ├──diffusers/controlnet-canny-sdxl-1.0   
|     ├──diffusers/controlnet-depth-sdxl-1.0   
|     ├──controlnet-zoe-depth-sdxl-1.0  
|     ├──TheMistoAI/MistoLine 
|     ├──xinsir/controlnet-tile-sdxl-1.0

```
Control_img image preprocessing, please use other nodes     

4 Example
----
txt2img mode uses the SDXL model of the single community model Old version examples    
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/txt2txt.png)

img2img mode, prompt words introduced [NC] and # refer to JSON with the same name in the example folder Old version examples    
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/img2imga.png) 

img2img_lora_controlnet_2rolein1img mode, add Lora, add dual character co frame (character 1 and character 2), add controllnet control (controllnet can only control dual character co frame) Latest examples     
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/img2imgcontrolnetdual.png)

txt2img_hyperlora_contrlnet_2role1img mode, adding HYper to accelerate Lora, adding dual characters in the same frame (character 1 and character 2), adding controllnet control (controllnet can only control dual characters in the same frame) Old version examples   
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/txt2img_hyperlora_contrlnet_2role1img.png)

More ControlNet added dual role co frame (Role 1 and Role 2) Old version examples   
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/controlnetnum.png) 

Translate the text into other language examples, and the translation nodes in the diagram can be replaced with any translation node. Old version examples     
![](https://github.com/smthemex/ComfyUI_StoryDiffusion/blob/main/examples/trans1.png)

Function Description of Nodes  
---   
--<Storydiffusion_Model_Loader>--    
--repo: using diffuser models ;     
--Ckptname:  using  community SDLX model selection;   
--Character_weights: Character weights saved using the save_character feature of the sampler node. Selecting "none/none" does not take effect! (Note that the saved character weights cannot be immediately recognized and require a restart of comfyUI);   
--Lora: Selecting SDXL Lora does not take effect when set to "none";   
--Lora_scale: The weight of Lora, which is enabled when Lora takes effect;   
--Trigger_words: The keyword for Lora will be automatically added to the prompt. When enabling Lora, please fill in the corresponding trigger_words for Lora;   
--Scheduler: When selecting a sampler and adding characters to the same frame in the text and animation, if running continuously, an error will be reported. At this time, changing a sampler can continue running, but this bug has not been fixed yet;   
--Model_type: Select either the txt2img or img2img mode, and when using the txt2img mode, the sampler may not be connected to the image;   
--Idnumber: How many roles are used, currently only supporting 1 or 2;   
--Sa32_degree/sa64_degree: an adjustable parameter for the attention layer;   
--Img_width/img_height: The height and width dimensions of the drawing.   
--reset_txt2img: Fixed an error where continuous rendering is not possible when using MS. You need to set "reset_txt2img" to Ture, which will replace the scheduler   

--<Storydiffusion_Sampler>---       
--Pipe/info: The interface that must be linked;   
--Image: The interface that must be linked to the image generation diagram. For dual roles, please follow the example and use the built-in image batch node in comfyUI;   
--Character prompt: The prompt for the character, [character name] must be at the beginning. If using the graphic mode, the keyword "img" must be added, such as a man img;   
--Scene prompts: The prompt for the scene description, [character name], must start at the beginning. It is best for both characters to appear once in the first two lines. [NC] At the beginning, the character does not appear (suitable for non character scenes). When (character A and character B), MS diffusion's dual character mode is enabled, and and the spaces before and after it cannot be ignored# Used for segmented prompt, rendering the entire segment, but only outputting the prompt after #;    
--Split prompt: The symbol for splitting the prompt, which does not take effect when it is empty. It is used to normalize paragraphs when the prompt is external. For example, when you pass in 10 lines of text, the hyphen may not be correct, but using a hyphen, such as ";", can effectively distinguish each line.     
--Negative prompt: only effective when img_style is No_style;      
--Seed/steps/cfg: suitable for commonly used functions in comfyUI;     
--Ip-adapter_strength: img2img controls the weight of ip-adapter in graph generation;   
--Style_strength'ratio: Style weight control, which controls from which step the style takes effect. When the style consistency is not good, you can try increasing or decreasing this parameter;   
--Encoder'repo: Only valid when two characters are in the same image. If you want to use a local model, be sure to use X:/XXX/XXX/laion/CLIP ViT bigG-14-laion2B-39B-b160k, which must be "/";   
--Role-scale: only effective when two characters are in the same image, controlling the weight of the characters in the image;   
--Mask_threshold: It is only effective when two roles are in the same picture, and controls the position of the role in the picture (MS system automatically assigns the role position according to prompt, so appropriate role position information description can be added to prompt);   
--Start_step: Only effective when two characters are in the same image, controlling the number of starting steps for the character's position in the image   
--Save_character: Whether to save the character weights of the current character, file in/ Under ComfyUI_StoryDiffusion/weights/pt, use time as the file name;  
--Controlnet_modelpath: Controlnet's community  model );   
--Controllet_scale: control net weight;   
--Layout_guidance: Is automatic layout enabled? (If automatic layout is enabled, it is best to have clear location information in the prompt, such as on the left and where...)..., For example, up and down, etc;    

--<Comic_Type>--         
--Fonts list: The puzzle node supports custom fonts (place the font file in the fonts directory. fonts/you_font. ttf);   
--Text_size: The size of the puzzle text;   
--Comic_type: Display the style of the puzzle;   
--Split lines: Suitable for non English text that has been translated by other translation nodes and the line break is removed. In this case, using a split symbol can correctly reassign the prompt line break to ensure that the text description is displayed on the correct image;   

--<Pre_Translate_prompt>: Pre processing of translation nodes       
--Keep_charactername: Whether to keep the character name displayed on subsequent text puzzles.   

Tips：

--Add dual character same frame function, usage method: (A and B) have lunch, A. B is the role name, and the middle and parentheses cannot be removed. The parentheses are the effective conditions!!!   
--Because the MS diffusion function was called, in order to use dual role same frame, it is necessary to add an encoder model (laion/CLIP ViT bigG-14 laion2B-39B-b160k, which cannot be replaced with others) and an ip adapet fine-tuning model (ms-adapter.bin, which cannot be replaced);   
--Optimize the loading of Lora's code, and when using accelerated Lora, trigger_words will no longer be added to the prompt list;   
--Playground v2.5 can be effective on txt2img, and there is no Playground v2.5 style Lora available when accelerated Lora can be used;   
--Role-scale, mask_threshold, and start_step mainly regulate the randomness and style consistency of two characters in the same frame;   
--The consistency of style can be adjusted between ip-adapter_strength and style_strength'ratio in img2img;   
--Preprocess translation text nodes, please refer to the example diagram for usage methods. (Pay attention to changing the font for Chinese or other East Asian characters);    
--By default, use the ";" at the end of each paragraph to divide the paragraph. After translation into Chinese, there is a chance that it will be translated as ";", so remember to change it to ";", otherwise it will be a sentence.   
--Edit the config/models. yaml file and remember to use the same format to include your favorite SDXL based diffusion model.   
--Supports diffuser versions 0.28 and above;   
--The process of generating images using PhotosMaker requires the IMG keyword in the character prompt column. You can use keywords such as a woman IMG, a man IMG, etc;   
--No characters appear in the image, add [NC] in front of the scene prompt;   
--Segmented prompt, using #, such as AAAA # BBBB, will generate AAAA content, but the text will only display BBBB   
  


Citation
------

StoryDiffusion
``` python  
@article{zhou2024storydiffusion,
  title={StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation},
  author={Zhou, Yupeng and Zhou, Daquan and Cheng, Ming-Ming and Feng, Jiashi and Hou, Qibin},
  journal={arXiv preprint arXiv:2405.01434},
  year={2024}
}
```
IP-Adapter
```
@article{ye2023ip-adapter,
  title={IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models},
  author={Ye, Hu and Zhang, Jun and Liu, Sibo and Han, Xiao and Yang, Wei},
  booktitle={arXiv preprint arxiv:2308.06721},
  year={2023}
}
```
MS-Diffusion
```
@misc{wang2024msdiffusion,
  title={MS-Diffusion: Multi-subject Zero-shot Image Personalization with Layout Guidance}, 
  author={X. Wang and Siming Fu and Qihan Huang and Wanggui He and Hao Jiang},
  year={2024},
  eprint={2406.07209},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
