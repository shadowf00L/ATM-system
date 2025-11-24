# account.py
# Shared account data 

account = {
    "pin": "1234",
    "balance": 1000.0
}

def to_dict():
    
    return {"pin": account["pin"], "balance": float(account["balance"])}
