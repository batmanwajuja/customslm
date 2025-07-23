import torch
import re

def vectorize_log(log, vocab):
    vec = torch.zeros(len(vocab))
    for word in log.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

def extract_ip(log):
    match = re.search(r"(?:\d{1,3}\.){3}\d{1,3}", log)
    return match.group() if match else None
