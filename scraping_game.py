from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urljoin


def get_html():
    url = input('write the url to extraxt info: ')
    try:
        raw_html=requests.get(url)
    except:
        print('trouble with URL')
    return(raw_html)
        

def get_images_iterable(raw_request):
    file_prefix = input ('where do you want to save the images? ')
    try:
        parsed_html = BeautifulSoup(raw_request.content, "html.parser")
    except:
        print('troble parsing')
    
    try:
        os.mkdir(file_prefix)
    except OSError as e:
        print(e)
        pass

    image_urls = [urljoin(raw_request.url, img['src']) for img in parsed_html.find_all('img')]
    for image in image_urls:
        image_data=requests.get(image)
        filename= file_prefix +'/'+ os.path.basename(image)
        with open(filename,'wb') as new_image:
            new_image.write(image_data.content)

my_html=get_html()

get_images_iterable(my_html)
