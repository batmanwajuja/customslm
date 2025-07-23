# agent/agent.py

from model.load_model import load_model
from utils.parser import vectorize_log
from agent.monitor import read_suricata_logs
from rules.rules import rule_based_decision
from agent.responder import respond
import torch

def classify_log(model, vocab, log):
    vec = vectorize_log(log, vocab)
    output = model(vec)
    label_idx = torch.argmax(output).item()
    return ["safe", "suspicious", "critical"][label_idx]

def run_agent():
    print("🛡️ Hybrid AI Firewall Agent Starting...")
    model, vocab = load_model()

    for log_line in read_suricata_logs():
        ml_label = classify_log(model, vocab, log_line)
        decision = rule_based_decision(log_line, ml_label)
        respond(log_line, decision)

if __name__ == "__main__":
    run_agent()
