import os
from participants_getter import participant_names

def test_all_people_receiving():
    '''
    Tests if all participants are receiving a gift
    '''
    generated_recipiants = []
    test_file_dir = os.getcwd()+'/givers_recipients'
    for filename in os.listdir(test_file_dir):
        if not filename.endswith(".txt"):
            continue
        with open(os.path.join(test_file_dir, filename), 'r') as f: 
            name = f.readline()
            generated_recipiants.append(name)

    for participant in participant_names:
        assert participant in generated_recipiants

def test_all_people_giving():
    '''
    Tests if all participants are giving a gift
    '''
    generated_givers = []
    test_file_dir = os.getcwd()+'/givers_recipients'
    for filename in os.listdir(test_file_dir):
        if not filename.endswith(".txt"):
            continue
        giver_name, txt = filename.split('.')
        generated_givers.append(giver_name)

    for participant in participant_names:
        assert participant in generated_givers

test_all_people_giving()
test_all_people_receiving()