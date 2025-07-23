import re
import torch
from collections import Counter

LABEL_MAP = {"safe": 0, "suspicious": 1, "critical": 2}

def tokenize_log(log):
    log = log.lower()
    log = re.sub(r"[^a-z0-9\s]", "", log)
    return log.split()

def build_vocab(logs, max_vocab_size=512):
    counter = Counter()
    for log in logs:
        tokens = tokenize_log(log)
        counter.update(tokens)
    return {word: idx for idx, (word, _) in enumerate(counter.most_common(max_vocab_size))}

def vectorize_log(log, vocab):
    vec = torch.zeros(len(vocab))
    for token in tokenize_log(log):
        if token in vocab:
            vec[vocab[token]] += 1
    return vec
