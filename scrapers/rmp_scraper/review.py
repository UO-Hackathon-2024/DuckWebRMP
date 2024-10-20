


class Review: 
    def __init__(self): 
        self.__comment = ""
        self.__quality = -1
        self.__difficulty = -1
        self.__course = ""
        self.__prof = ""

    def __str__(self) -> str: 
        return f"Prof: {self.__prof}, Course: {self.__course}, Quality: {self.__quality}, Difficulty: {self.__difficulty}"

    def set_comment(self, comment: str): 
        self.__comment = comment

    def set_quality(self, quality: int):
        self.__quality = quality 

    def set_difficulty(self, diff: int): 
        self.__difficulty = diff

    def set_course(self, course: str): 
        self.__course = course

    def set_prof(self, name: str): 
        self.__prof = name

    def get_comment(self): 
        return self.__comment

    def get_quality(self): 
        return self.__quality

    def get_difficulty(self): 
        return self.__difficulty
    
    def get_course(self): 
        return self.__course
    
    def get_prof(self): 
        return self.__prof

        
