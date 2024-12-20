from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
from langchain_huggingface import ChatHuggingFace
import warnings

warnings.filterwarnings("ignore")

model = AutoModelForCausalLM.from_pretrained('openbmb/MiniCPM-V-2_6-int4',
                                             local_files_only=True,
                                             trust_remote_code=True,
                                             attn_implementation="sdpa")
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-2_6-int4',
                                          local_files_only=True,
                                          trust_remote_code=True)


class VisionModel:
    def __init__(self):
        self.model = model

        self.tokenizer = tokenizer

    def complete(self, prompt: str, image=None):
        msgs = [{'role': 'user', 'content': [prompt, image]}]
        res = self.model.chat(
            image=None,
            msgs=msgs,
            tokenizer=tokenizer,
            sampling=True,
            temperature=0.7,
            stream=True
        )
        generated_text = ""
        for new_text in res:
            generated_text += new_text
            yield new_text


def main():
    vllm = VisionModel()
    prompt = input("Your question please")
    while True:
        vllm.complete(prompt)
        prompt = input("\ntype exit to exit or type another question")
        if prompt == "exit":
            break


if __name__ == "__main__":
    main()
