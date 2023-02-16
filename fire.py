All={}

def save(m):
    with open("Manager.m","wb") as f:
        pickle.dump(m,f)
def load():
    with open("Manager.m","rb") as f:
        return pickle.load(f)