from transformers import pipeline

def main():
    print("Hello, world!")
    classifier = pipeline("sentiment-analysis",model="openai-community/gpt2")
    

if __name__ == "__main__":
    main()