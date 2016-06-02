from django.utils.encoding import smart_str
class Movie():

    def __init__(self, title, release_date, description, picture_url):
        '''Movie object constructor'''
        self.title = title
        self.release_date = release_date
        self.description = description
        self.picture_url = picture_url

    def __str__(self):
        return smart_str(self.description)