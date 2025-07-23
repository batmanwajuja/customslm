# train.py
import json
import torch
import torch.nn as nn
import torch.optim as optim
from preprocess import build_vocab, vectorize_log
from model import TinyCyberModel
import argparse
import os

# 🧠 --- 1. Setup CLI argument for dataset path ---
parser = argparse.ArgumentParser(description="Train the TinyCyberModel on log data.")
parser.add_argument("--data", default="data/logs.jsonl", help="Path to training data (.jsonl)")
parser.add_argument("--output", default="trained/model.pt", help="Where to save the trained model")
args = parser.parse_args()

# 🧾 --- 2. Load and parse dataset ---
if not os.path.exists(args.data):
    raise FileNotFoundError(f"Could not find training data at {args.data}")

with open(args.data, "r") as f:
    dataset = [json.loads(line) for line in f]

logs = [entry["log"] for entry in dataset]
labels_text = [entry["label"] for entry in dataset]

# 🧮 --- 3. Encode labels ---
label_to_idx = {"safe": 0, "suspicious": 1, "critical": 2}
y = torch.tensor([label_to_idx[lbl] for lbl in labels_text])

# 🔤 --- 4. Build vocab and vectorize logs ---
vocab = build_vocab(logs)
x = torch.stack([vectorize_log(log, vocab) for log in logs])

# 🧠 --- 5. Define model ---
model = TinyCyberModel(input_dim=len(vocab), hidden_dim=64, output_dim=3)

# 🧪 --- 6. Training setup ---
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)
epochs = 100

# 🚂 --- 7. Training loop ---
for epoch in range(1, epochs + 1):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# 💾 --- 8. Save model and vocab ---
os.makedirs(os.path.dirname(args.output), exist_ok=True)
torch.save({"model": model.state_dict(), "vocab": vocab}, args.output)
print(f"✅ Model saved to {args.output}")
