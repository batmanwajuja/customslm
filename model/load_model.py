import torch
from model.tiny_model import TinyCyberModel

def load_model(model_path="trained/model.pt"):
    checkpoint = torch.load(model_path)
    model = TinyCyberModel(input_dim=len(checkpoint["vocab"]), hidden_dim=64, output_dim=3)
    model.load_state_dict(checkpoint["model"])
    model.eval()
    return model, checkpoint["vocab"]
