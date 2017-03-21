from pylab import *
# from cdc import db, code_names

diabetespath = "D:\School\Research\Sean\Data_Yr\\diabetes.txt"
accidentpath = "D:\School\Research\Sean\Data_Yr\\accident.txt"
alzpath = "D:\School\Research\Sean\Data_Yr\\alzheimers.txt"
cancerpath = "D:\School\Research\Sean\Data_Yr\\cancer.txt"
resppath = "D:\School\Research\Sean\Data_Yr\\chronic_lower_resp.txt"
flupath = "D:\School\Research\Sean\Data_Yr\\flupneu.txt"
nephpath = "D:\School\Research\Sean\Data_Yr\\kidney_disease.txt"
heartpath = "D:\School\Research\Sean\Data_Yr\\heart_disease.txt"
strokepath = "D:\School\Research\Sean\Data_Yr\\stroke.txt"
suicidepath = "D:\School\Research\Sean\Data_Yr\\suicide.txt"

death_list = ['Heart Disease', 'Cancer', 'Chronic Lower Respiratory Disease', 'Accident', 'Stroke', 'Alzheimers',
              'Diabetes', 'Flu/Pneumonia', 'Kidney Disease', 'Suicide']

state_key = np.genfromtxt("D:\School\Research\Sean\state_map.csv", dtype='str', delimiter=',')
state_dict = {k: v for k, v in state_key}

race_key = np.genfromtxt("D:\School\Research\Sean\\race_map.csv", dtype='str', delimiter=',')
race_dict = {k: v for k, v in race_key}


def age_key(age):
    if age < 25:
        return '20-24'
    elif age < 35:
        return '25-34'
    elif age < 45:
        return '35-44'
    elif age < 55:
        return '45-54'
    elif age < 65:
        return '55-64'
    elif age < 75:
        return '65-74'
    elif age < 85:
        return '75-84'
    elif age >= 85:
        return '85+'
    else:
        print('Insert age between 20~85+.')
        return


def state_key(state):
    return state_dict[state]


def race_key(race):
    return race_dict[race]


def total_deaths(age=21, gender='F', state="California", race='Asian', year=2013):
    print('From 1999-2014, for a', age, 'year old ', race, gender, 'from', state)

    results = []
    for ii in death_list:
        results.append((ii, deaths_by_disease(ii, age, gender, state, race)))

    print('Deaths from year', year, ':')
    for ii in results:
        if ii[1]:
            print(ii[0], '-', ii[-1][-1][1])


def death_plot(data_count, dis):
    if data_count:
        x_val = [x[0] for x in data_count]
        y_val = [x[1] for x in data_count]
        plt.figure()
        plt.plot(x_val, y_val)
        plt.plot(x_val, y_val, 'or')
        plt.title(dis)
        plt.xlabel('Year')
        plt.ylabel('Deaths')
        plt.show()


def data_pull(dis):
    if dis == 'Diabetes':
        return np.genfromtxt(diabetespath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Accident':
        return np.genfromtxt(accidentpath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Alzheimers':
        return np.genfromtxt(alzpath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Cancer':
        return np.genfromtxt(cancerpath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Chronic Lower Respiratory Disease':
        return np.genfromtxt(resppath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Flu/Pneumonia':
        return np.genfromtxt(flupath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Kidney Disease':
        return np.genfromtxt(nephpath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Heart Disease':
        return np.genfromtxt(heartpath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Stroke':
        return np.genfromtxt(strokepath, dtype='str', delimiter='\t', skip_header=1)
    elif dis == 'Suicide':
        return np.genfromtxt(suicidepath, dtype='str', delimiter='\t', skip_header=1)
    else:
        print('Wrong disease.')
        return


def deaths_by_disease(dis, age, gender, state, race):
    age_code = age_key(age)
    state_code = state_key(state)
    race_code = race_key(race)
    data = data_pull(dis)
    count = 0
    data_count = []

    for ii in range(data.shape[0]):
        data_row = data[ii]
        if(data_row[1] == age_code and data_row[3] == gender and data_row[2] == state_code and
           data_row[4] == race_code):
                count += int(data_row[5])
                data_count.append((int(data_row[0]), int(data_row[5])))
    print('Total deaths due to', dis, ':', count)

    # death_plot(data_count, dis)
    return data_count


total_deaths()
