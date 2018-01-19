from models import Comic
from django.db.transaction import commit_on_success

path = "ml-100k"

@commit_on_success
def populateComics():
    print("Loading comics...")
#     Comic.objects.all().delete()
    
    fileobj=open(path+"\\u.comic", "r")
    line=fileobj.readline()
    while line:
        data = line.split('","')
        if len(data)>1:
            ide = data[0][1:].strip().decode('utf-8', 'replace').encode('utf8')
            tit = data[1].strip().decode('utf-8', 'replace').encode('utf8')
            pre = data[2].strip().decode('utf-8', 'replace').encode('utf8')
            url = data[3].strip().decode('utf-8', 'replace').encode('utf8')
            img = data[4][:-2].strip().decode('utf-8', 'replace').encode('utf8')
            Comic.objects.create(id=ide, comicTitle=tit, comicPrice=pre, comicLink=url, comicImage=img)
        line=fileobj.readline()
    fileobj.close()
    
    print("Comics inserted: " + str(Comic.objects.count()))
    print("---------------------------------------------------------")
       
def populateDatabase():
    populateComics()
    print("Finished database population")
    
if __name__ == '__main__':
    populateDatabase()