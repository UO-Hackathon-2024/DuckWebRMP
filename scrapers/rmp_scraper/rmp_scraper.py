


# ---- Web Scraper ----
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---- Review Class ----
from review import Review 
from review_to_database import insert_review

import logging as log 
import json
from errors import NoProfFound

log.basicConfig(
    level=log.INFO,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format of the log messages
)


def main(): 
    with open('../dw_scraper/profs.json', 'r') as file: 
        course_data = json.load(file)
    for prof in course_data: 
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
        driver.set_page_load_timeout(20)

        #loop thorugh the links and find the professor at the university of oregon 
        link_elements = driver.find_elements(By.XPATH, "//a[starts-with(@href, '/professor/') and contains(@href, '')]")
        for link_element in link_elements: 
            try: 
                link = link_element.get_attribute("href")
                driver.get(link) #use the link of the uo prof 
            except Exception as e: 
                continue
            


        #find the elements from the reviews
        comments = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'Comments')]")
        ratings = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'CardNumRating__CardNumRatingNumber')]")
        courses = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'RatingHeader__StyledClass')]")
         
        #The ratings are the same class and come in pairs of two, index by 2 only for the ratings
        i = 0
        ratings_i = 0

        while(i < len(comments)): 
            review = Review()

            #Set values to the review object
            review.set_prof(prof)
            review.set_comment(comments[i].text)
            review.set_quality(ratings[ratings_i].text)
            review.set_difficulty(ratings[ratings_i + 1].text)
            review.set_course(courses[i].text)

            insert_review(review)

            i += 1
            ratings_i += 2
        log.info(review)
    except Exception as e: 
        raise e
    finally: 
        driver.quit()


def prof_to_url(prof: str) -> str: 
    #Convert the professor name to a rate my professor search url 
    name = prof.split()
    first_name = name[0]
    last_name = name[1]
    return f"https://www.ratemyprofessors.com/search/professors/1261?q={first_name}%20{last_name}"



if __name__ == "__main__": 
    main()


    
    


    



