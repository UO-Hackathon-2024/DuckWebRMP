import requests
from bs4 import BeautifulSoup


duckweb_url = 'https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202401&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&sel_subj=CS&sel_crse=&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&submit_btn=Show+Classes'
#prac_url = 'https://www.python.org'


response = requests.get(duckweb_url)
#prac = requests.get(prac_url)

duck_json = BeautifulSoup(response.text, 'html.parser')

#print(duck_json)

#<td rowspan="1" nowrap="nowrap" class="dddefault" width="110">Flores J</td>

#----------------------------GET THE DATA -----------------------------------------------------

def find_all_teachers_by_subject(file) -> list:
    
    teacher_name = duck_json.find_all('td',  attrs={'width': '110', 'rowspan': '1'})
    li = []
    for teach in teacher_name:
        li.append(prof_class.text.replace('\n', ' '))

    return li    



teacher_name = duck_json.find_all('td',  attrs={'width': '110', 'rowspan': '1'})
class_names = duck_json.find_all('td', attrs={'colspan':"6"})


#------------------------------Turn data into list-----------------------------------------------------

classes_stored = []

for prof in teacher_name:
    #print(prof)
    #print(prof.text)
    prof_class = prof.find_parent('tr')
    #print(prof_class)
    #print(prof_class.text.replace('\n', ' '))
    #print(prof_class.text.replace('\n', '|').replace('\xa0',''))
    #print(prof_class.text.replace('\n', '|').replace('\xa0','').split('|'))
    fixed_prof_class = prof_class.text.replace('\n', '|').replace('\xa0','N/A').split('|')
    
    #print(fixed_prof_class)

    fixed_prof_class = list(filter(lambda ele: ele != '', fixed_prof_class))


    #print(fixed_prof_class)
    classes_stored.append(fixed_prof_class)

#print(classes_stored)

#for class names

class_names_stored = []
map_count = 0

for name in class_names:
    temp = []
    #print(name)
    print(name.text)
    #print(name.text.replace('\n', '|')).replace('\xa0',''))
    #fixed_class_names = name.text.replace('\n', '|').replace('\xa0','')
    #temp.append(fixed_class_names)
    #temp.append(map_count)
    #class_names_stored.append(temp)
    #map_count += 1

    sub = name[0] + name[1] 
    num = name[]

    
f'https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202304&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&submit_btn=Submit&sel_subj={sub}&sel_crse=101&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a
'


#print(class_names_stored)

#for ele in class_names_stored:
    #print(ele)

#print(len(class_names_stored))

#-------------------------------------FILTER CLASSES WE WANT -------------------------------------------------

#print(classes_stored)

#print(len(classes_stored))

def remove_labs(li):

    lab_free = []
    
    for classes in li:
        if not any(klass in classes for klass in ["+ Lab", "+ Dis"]):
            lab_free.append(classes)

    return lab_free

lab_free = remove_labs(classes_stored)

#for ele in lab_free:
#    print(ele)


def remove_2man_labs(li):

    temp = []

    for ele in li:
        if len(ele) != 1:
            #print(len(ele))
            temp.append(ele)
    
    return temp

lab_free = remove_2man_labs(lab_free)

print(len(lab_free))

#for klass in lab_free:
    #print(klass, len(klass))



def map_lab_free_classes(li):

    count = 0

    for ele in li:
        ele.append(count)
        print(ele)
        count += 1
    pass

#map_lab_free_classes(lab_free)

def add_names(class_names, classes):

    for ele in range(len(class_names)):
        classes[ele].append(class_names[ele][0])
        print(ele)

    return classes

#add_names(class_names_stored,lab_free)


def remove_independent(li):

    indy_free = []
    
    for classes in li:
        if not any(klass in classes for klass in ["STAFF ","-"]):
            indy_free.append(classes)

    return indy_free

lab_and_indy_free = remove_independent(lab_free)

#print(len(lab_and_indy_free))

#for klass in lab_and_indy_free:
    #print(klass, len(klass))




def remove_extra(li=list[list]):

    temp = []

    for ele in li:
        #print(ele, len(ele))
        if len(ele) == 9:
            temp.append(ele)
        
    return temp

lab_and_indy_and_research_free = remove_extra(lab_and_indy_free)

#print(len(lab_and_indy_and_research_free))

#for klass in lab_and_indy_and_research_free:
    #print(klass,len(klass))


def add_to_dictionary(cnames=list[list], teachers=list[list]):

    stored = {}
    # { michal: {crn; 3, hours: 4"}, hank: {crn : 3, hours:4}, willis: {crn:3, hours:4} }

    for ele in teachers:
        stored[ele[7]] = 1

    return stored


#print(add_to_dictionary(class_names_stored, lab_and_indy_and_research_free))
        
        













'''
cs314: {
        hank; {
        "hours": 3
        }

        michal{
        hours: 3
        
        }

}
'''







