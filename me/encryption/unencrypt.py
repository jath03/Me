from me.encryption.changebase import changebase
from pprint import pprint

def unencrypt(encrypted_message, base):
    new_encrypted_message = encrypted_message.split(',')
    answer = []
    for x in range(0, (len(new_encrypted_message))):
        answer.append(chr(int(changebase(int(new_encrypted_message[x]), base, 10))))
    return ''.join(answer)
    

        
        
        
        
