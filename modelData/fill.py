import codecs
import csv
from Careers.models import Career

def load_careers():
    
    ##with codecs.open("Careers.xlsx", 'r', encoding='utf-8', errors='ignore') as f:
    with open("Careers.csv", 'rt') as f:
        reader = csv.reader(f)
        
        
        for row in reader:
            break

        counter = 0
        
        for row in reader:
            
            _, created = Career.objects.get_or_create(
                career_name = row[0],
                onet_id = row[1],
                median_salary = int(row[2]),
                industry = row[3],
                education = row[4]
            )


if __name__ == '__main__':
    load_careers()