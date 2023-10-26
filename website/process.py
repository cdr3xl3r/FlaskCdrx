
from werkzeug.security import generate_password_hash, check_password_hash

def printProccess(*args):
    
    for arg in args:
        print(f'Process= {arg}')
def printReturn(*args, **kwargs):
    print(f'Process= <{args,kwargs}>')
            

def sha256(i):
    sha=generate_password_hash(i)
    printProccess('sha256')
    printReturn(sha,process='sha256')
    return sha
    


#scrypt:32768:8:1$OLPnOEPh0GATnZts$4b8465926146dcd808bad2e743dc36e63ee8004a7822253af99fe6a167bc240f04e3f0fd6488d1a306d761fc57f021e74f6aea2e013eb1705d36eb3655d888ee

if __name__ == '__main__':
    admin = 'admin'
    admin1 = 'admin1'
    admin2 = 'admin2'
    test = sha256(admin)