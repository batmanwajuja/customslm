import torch
from model import TinyCyberModel
from preprocess import tokenize_log, vectorize_log

LABELS = ["Safe", "Suspicious", "Critical"]

def load_model(path="trained/model.pt"):
    checkpoint = torch.load(path)
    vocab = checkpoint['vocab']
    model = TinyCyberModel(input_dim=len(vocab))
    model.load_state_dict(checkpoint['model'])
    model.eval()
    return model, vocab

def run_cli():
    model, vocab = load_model()
    while True:
        log = input("📝 Log line (or 'exit'): ")
        if log.lower() == "exit":
            break
        vec = vectorize_log(log, vocab).unsqueeze(0)
        with torch.no_grad():
            logits = model(vec)
            probs = torch.softmax(logits, dim=1)
            pred = torch.argmax(probs).item()
            print(f"⚠️  Predicted: {LABELS[pred]} (Confidence: {probs[0][pred]:.2f})")

if __name__ == "__main__":
    run_cli()
