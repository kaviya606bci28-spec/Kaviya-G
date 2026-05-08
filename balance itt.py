import datetime

# Global Data & Exceptions
accounts, daily_wd = {}, {}
class InsufficientFundsError(Exception): pass
class DailyLimitError(Exception): pass
class AccountNotFoundError(Exception): pass

def log(msg): 
    with open("error_log.txt", "a") as f: f.write(f"[{datetime.datetime.now()}] {msg}\n")

def create_account(id, name, bal): accounts[id], daily_wd[id] = {"n": name, "b": bal, "h": []}, 0
def deposit(id, amt):
    if id not in accounts: raise AccountNotFoundError(id)
    if amt < 0: raise ValueError(); 
    if amt > 100000: raise OverflowError()
    accounts[id]["b"] += amt; accounts[id]["h"].append(f"+{amt}")
def withdraw(id, amt):
    if id not in accounts: raise AccountNotFoundError(id)
    if amt > accounts[id]["b"]: raise InsufficientFundsError()
    if daily_wd[id] + amt > 50000: raise DailyLimitError()
    accounts[id]["b"] -= amt; daily_wd[id] += amt; accounts[id]["h"].append(f"-{amt}")
def transfer(f, t, amt): withdraw(f, amt); deposit(t, amt)


