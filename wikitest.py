import wikipedia
import csv
import re
def get_csv_list(file):
    with open(file, encoding='utf-8') as f:
        r = csv.reader(f)
        return_list = list(r)
    return_list = return_list[0]
    f.close()
    return return_list
guests = get_csv_list('guest_names.csv')

science_matches = {'scientist','physicist','astrophysicist',
                    'astronomer','geneticist','researcher',
                    'psychologist','biologist','paleontologist',
                    'mathematician', 'phd','philosopher',
                    'professor','chemist','paleontologist',
                    'geologist','climatologist','primatologist',
                    'cosmologist'}
comedy_matches = {'comedian','standup'}
sport_matches = {'martial','boxer','fighter',
                    'kickboxer','fighting','ufc',
                    'bellator','wrestler','jiujitsu',
                    'ibjjf','adcc','surfer',
                    'football','powerlifter','strongman',
                    'bodybuilder','triathlete','ultramarathon'}

classes = get_csv_list('classeslist0.csv')
for i in range(len(classes)):
    classes[i] = int(classes[i])

for i,name in enumerate(guests):
    print(i)
    if classes[i] > 0:
        continue
    if name == 'Brian Redban':
        classes[i] = 2
        continue
    if name == 'Cameron Hanes':
        classes[i] = 0
        continue
    if name == 'Dr. Rhonda Patrick':
        classes[i] = 3
        continue
    try:
        wiki_string = wikipedia.page(name).summary.lower()
        keep_characters = ' '
        #remove non-alphanumeric characters, and turn into a set of words
        wiki_string = set(re.sub(r'[^\w'+keep_characters+']', '',wiki_string).split())

        if bool(comedy_matches & wiki_string):
            classes[i] = 2
            print(str(classes[i])+'  '+name)
            continue
        if bool(sport_matches & wiki_string):
            classes[i] = 1
            print(str(classes[i])+'  '+name)
            continue
        if bool(science_matches & wiki_string):
            classes[i] = 3
            print(str(classes[i])+'  '+name)
    except Exception as e:
        print(e)

with open('classeslist0.csv', 'w', newline='',encoding='utf-8') as myfile:
     wr = csv.writer(myfile)
     wr.writerow(classes)
myfile.close()