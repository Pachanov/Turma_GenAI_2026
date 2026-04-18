#!/usr/bin/env python3

from transformers import AutoTokenizer

text = "Tokenizacão é fundamental para modelos de linguagem"

tokenizers = {
"BPE (GPT-like)": "gpt2",
"WordPiece (BERT)": "bert-base-multilingual-cased"

}

for name, model in tokenizers.items():
    tok = AutoTokenizer. from_pretrained(model)
print(f"\n{name}:")
print(tok.tokenize(text))