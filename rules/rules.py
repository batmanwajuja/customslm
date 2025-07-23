# rules/rules.py

def rule_based_decision(log, ml_label):
    log = log.lower()

    if "root login" in log and "unknown" in log:
        return "critical"
    if ml_label == "suspicious" and ("scan" in log or "port sweep" in log):
        return "critical"
    return ml_label
