


# ---- Web Scraper ----
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---- Review Class ----
from review import Review 

# ---- Debug Logging --- 
import logging as log 
log.basicConfig(
    level=log.INFO,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format of the log messages
)

import json
from errors import NoProfFound


def main(): 
    with open('test.json', 'r') as file: 
        course_data = json.load(file)
    for course in course_data: 
        for prof in course_data[course]: 
            try: 
                scrape_prof_reviews(prof)
            except Exception as e: 
                log.info(e)
                continue

    
def scrape_prof_reviews(prof: str): 

    url = prof_to_url(prof)
    #init the web driver
    driver = webdriver.Firefox()
    #navigate to the url 
    driver.get(url)

    try: 

        #loop thorugh the links and find the professor at the university of oregon 
        link_elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '/professor/') and contains(@href, '')]")
        uo_prof_found = False
        for link_element in link_elements: 
            school = link_element.find_element(By.XPATH, "//*[starts-with(@class, 'CardSchool__School')]").text
            if school == "University of Oregon":
                link = link_element.get_attribute("href")
                driver.get(link) #use the link of the uo prof 
                uo_prof_found = True
                break
        if (not uo_prof_found): 
            raise NoProfFound("No professor found")


        #find the elements from the reviews
        comments = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'Comments')]")
        ratings = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'CardNumRating__CardNumRatingNumber')]")
        courses = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'RatingHeader__StyledClass')]")
         
        #The ratings are the same class and come in pairs of two, index by 2 only for the ratings
        i = 0
        ratings_i = 0

        reviews = []
        while(i < len(comments)): 
            review = Review()

            #Set values to the review object
            review.set_prof(prof)
            review.add_comment(comments[i].text)
            review.set_quality(ratings[ratings_i].text)
            review.set_difficulty(ratings[ratings_i + 1].text)
            review.set_course(courses[i].text)

            reviews.append(review)
            log.info(review)

            i += 1
            ratings_i += 2

    except Exception as e: 
        raise e
    finally: 
        driver.quit()


def prof_to_url(prof: str) -> str: 
    #Convert the professor name to a rate my professor search url 
    name = prof.split()
    first_name = name[0]
    last_name = name[1]
    return f"https://www.ratemyprofessors.com/search/professors?q={first_name}%20{last_name}"



if __name__ == "__main__": 
    main()


    
    


    



