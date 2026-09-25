from transformers import AutoModelForCausalLM, AutoTokenizer    
from lm_eval.models.huggingface import HFLM    
from lm_eval import simple_evaluate    
from lm_eval import tasks
import json
import torch

model_name = "Qwen/Qwen2.5-0.5B-Instruct-GGUF"

model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        device_map="auto", 
        trust_remote_code=True,
        # attn_implementation="flash_attention_2",
        # torch_dtype=torch.float16
        ).eval()    
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)    
lm = HFLM(pretrained=model,tokenizer=tokenizer,batch_size=32,device="gpu")       
results = simple_evaluate(model=lm,tasks=["arc_challenge","hellaswag","piqa"])   
#将results中的数据导出到json文件中  
filtered_results = results.copy()  
filtered_results = {key: value for key, value in results.items() if key == "results"}  
json_filtered_results = json.dumps(filtered_results, indent=4)  
with open("results.json", "w") as json_file:  
        json_file.write(json_filtered_results) 

