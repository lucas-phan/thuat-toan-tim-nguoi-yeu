#Lucas Happy Coding
#Youtube: https://www.youtube.com/channel/UC08J7-d66B4pqUN9PNrAACw

from PIL import Image
import imagehash
import glob

result = []
info = {}

for boy_url in glob.glob('ban-trai/*.jpg'):

    boy_hash = imagehash.average_hash(Image.open(boy_url))

    flag = 100
    right_people = ''

    for girl_url in glob.glob('ban-gai/*.jpg'):
        #tao ma hash cho tat ca ban nu
        girl_hash = imagehash.average_hash(Image.open(girl_url))
        
        #kiem tra khac biet giua cac ma hash voi nhau
        diff_hash = boy_hash - girl_hash

        #tim ra chi so khac biet thap nhat
        if flag > diff_hash:
            flag = diff_hash
            right_people = girl_url

    #Tra ve ket qua
    info = {
        'boy': boy_url,
        'girl': right_people,
        'diff': flag
    }

    result.append(info)

#In ra ket qua
for data in result:
    print(data)

