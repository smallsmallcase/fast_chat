from transformers import pipeline
import torch
def main():
    print("Hello, world!")
    

if __name__ == "__main__":
    main()
def bert():

pipeline = pipeline(
    task="fill-mask",
    model="google-bert/bert-base-uncased",
    torch_dtype=torch.float16,
    device=0
)
result =  pipeline("sun arise from the [MASK]")
print(result)