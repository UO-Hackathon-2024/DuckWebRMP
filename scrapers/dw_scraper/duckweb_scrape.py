import requests
from bs4 import BeautifulSoup
import json


duckweb_url = 'https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202401&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&sel_subj=CS&sel_crse=&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a&submit_btn=Show+Classes'




def main(): 

    response = requests.get(duckweb_url)
    
    duck_response = BeautifulSoup(response.text, 'html.parser')
    
    acros = get_all_acronyms(duck_response)

    print(acros)
    
    i = 0
    """
    response = requests.get('''https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202401&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&submit_btn=Submit&sel_subj=AAAP&sel_crse=&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a''')
        
    duck_response = BeautifulSoup(response.text, 'html.parser')

    
    courses = search_through_subj_urls(duck_response)

    print(courses) 

    courses = remove_labs(courses)
    print(courses)
    courses = remove_2man_labs(courses)
    print(courses)
    courses = remove_independent(courses)
    print(courses)

    prof_dict = add_to_dictionary(courses)
    print(prof_dict)
    """

    for ele in acros:
        #print(ele)
    
        if i == 2:
            break
    
        duckweb_url2 = f'''https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202401&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&submit_btn=Submit&sel_subj={ele}&sel_crse=&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a'''

        #print(duckweb_url2)
        i += 1
    
        response = requests.get(duckweb_url2)
        
        duck_response = BeautifulSoup(response.text, 'html.parser')
    
        
        courses = search_through_subj_urls(duck_response) 

        courses = remove_labs(courses)
        courses = remove_2man_labs(courses)
        courses = remove_independent(courses)

        prof_dict = add_to_dictionary(courses)
        #print(prof_dict)

        for ele in prof_dict:
            print(ele, prof_dict[ele])
        #with open('profs.json', 'w') as file:
            #json.dump(prof_dict, file)
            
        print('DONE BABY')



#------------------------------Turn data into list-----------------------------------------------------


def get_all_acronyms(response):
    subject_acros_plus_class = response.find_all('select', attrs={'name':'sel_subj'})
    
    acro_list = []
    for subj in subject_acros_plus_class:
    
        parsed = subj.text
        #print(parsed)
        parsed = parsed.replace('\n', '|').replace('\xa0','N/A').split('|')
        #subject_and_arco_list.append(parsed)
        parsed.pop(0)
        parsed.pop(0)
        #parsed.pop()

    for acro in parsed:

        acro_list.append(acro[:4].strip("- "))


    return acro_list



def get_subject_urls(response): 
    # Get the subject names in a list 
    subject_names = response.find_all('td', attrs={'colspan':"6"})
    subject_urls = []
    subjects = []
    for name in subject_names: 
        parsed = name.text.replace('\n', '|').replace('\xa0', '')
        if not parsed[3].isdigit() and not parsed[3] == ' ': 
            sub = parsed[0] + parsed[1] + parsed[2] + parsed[3]
            num = parsed[5] + parsed[6] + parsed[7]
        elif not parsed[2].isdigit() and not parsed[2] == ' ': 
            sub = parsed[0] + parsed[1] + parsed[2]
            num = parsed[4] + parsed[5] + parsed[6]
        else: 
            sub = parsed[0] + parsed[1]
            num = parsed[3] + parsed[4] + parsed[5]

        sub = sub.replace(" ", "")
        num = num.replace(" ", "")

        url = f"""https://duckweb.uoregon.edu/duckweb/hwskdhnt.P_ListCrse?term_in=202401&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_cred=dummy&sel_tuition=dummy&sel_open=dummy&sel_weekend=dummy&sel_title=&sel_to_cred=&sel_from_cred=&submit_btn=Submit&sel_subj={sub}&sel_crse={num}&sel_crn=&sel_camp=%25&sel_levl=%25&sel_attr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a"""
        
        subject_urls.append(url)
        subjects.append(sub + num)
    return subject_urls, subjects

def search_through_subj_urls(main_response): 
    course_url_and_courses = get_subject_urls(main_response)
    course_urls = course_url_and_courses[0]
    courses = course_url_and_courses[1]

    course_infos = []

    for i in range(len(courses)): 

        print(f"Searching course {i}")
        response = requests.get(course_urls[i])
        soup = BeautifulSoup(response.text, 'html.parser')
        
        teacher_name = soup.find_all('td',  attrs={'width': '110', 'rowspan': '1'})


        for prof in teacher_name:
            prof_class = prof.find_parent('tr')
            course_info = prof_class.text.replace('\n', '|').replace('\xa0','N/A').split('|')
            #print(course_info, '------------------')
            course_info = list(filter(lambda ele: ele != '', course_info))
            #print(course_info, '-------------------')

            if len(course_info) == 9:
                course_info.pop()
            #print(course_info, '++++++++++++++++++++++++')
            
            course_info.append(courses[i])

            course_infos.append(course_info)

    return course_infos


    




#-------------------------------------FILTER CLASSES WE WANT -------------------------------------------------


def remove_labs(li):

    lab_free = []
    
    for classes in li:
        if not any(klass in classes for klass in ["+ Lab", "+ Dis"]):
            lab_free.append(classes)

    return lab_free




def remove_2man_labs(li):

    temp = []

    for ele in li:
        if len(ele) != 1:
            #print(len(ele))
            temp.append(ele)
    
    return temp






def map_lab_free_classes(li):

    count = 0

    for ele in li:
        ele.append(count)
        count += 1
    pass


def add_names(class_names, classes):

    for ele in range(len(class_names)):
        classes[ele].append(class_names[ele][0])

    return classes



def remove_independent(li):

    indy_free = []
    
    for classes in li:
        if not any(klass in classes for klass in ["STAFF ","-"]):
            indy_free.append(classes)

    return indy_free



def add_to_dictionary(course_names=list[list]):
    prof_dict = {}

    for course in course_names: 
        if len(course) >= 9: 
            crn = course[1]
            avail = course[2]
            time = course[4]
            day = course[5]
            location = course[6]
            name = course[7]
            course_title = course[8]
        else: 
            continue

        if name not in prof_dict: 
            prof_dict[name] = {"crn": [crn], "avail": [avail], "time": [time], "day": [day], "location":[location],  
                               "course_title":[course_title] }
        else: 
            prof = prof_dict[name]
            prof["crn"].append(crn)
            prof["avail"].append(avail)
            prof["time"].append(time)
            prof["day"].append(day)
            prof["location"].append(location)
            prof["course_title"].append(course_title)



    return prof_dict











        
        
if __name__ == "__main__": 
    main()


















