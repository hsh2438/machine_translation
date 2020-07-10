import os
import pandas
import pickle


def load_data(file_path):
    excel = pandas.read_excel(open(file_path, 'rb'))
    korean = excel['원문']
    english = excel['번역문']
    assert len(korean) == len(english)
    
    return [(korean[i], english[i]) for i in range(len(korean))]


if __name__ == '__main__':
    dataset = []

    file_list = os.listdir('data')
    for file_name in file_list:
        if file_name.endswith('.xlsx'):
            print(file_name)
            dataset.extend(load_data(os.path.join('data', file_name)))
    
    print('{} pair data.'.format(len(dataset)))
    pickle.dump(dataset, open('dataset.pickle', 'wb'))
