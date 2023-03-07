import codecs
import csv


def load_careers():
    
    
    ##with codecs.open("Careers.xlsx", 'r', encoding='utf-8', errors='ignore') as f:
    
    with open("Courses.csv", 'rt') as f:
        reader = csv.reader(f)
        
        
        for row in reader:
            break

        counter = 0
        
        for row in reader:
            
            for i in row:
                print(i)


if __name__ == '__main__':
    load_careers()