import random
from participants_getter import participant_names

secret_santa_dir = 'givers_recipients/'

if __name__ == '__main__':
    if len(participant_names) < 2:
        raise ValueError('There has to be more than 1 participant')
    
    receivers = []
    for giver in participant_names:
        while True:
            receiver = random.choice(participant_names)
            if giver == receiver:
                continue
            if receiver in receivers:
                continue
            break
        
        receivers.append(receiver)
        path = secret_santa_dir + giver + '.txt'
        with open(path, 'w') as f:
            f.write(receiver)

