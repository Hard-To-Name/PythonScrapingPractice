import re, requests

term = {"Fall": "92", "Summer2": "76", "SummerOL": "51", "Summer10": "39",
        "Summer1": "25", "Spring": "14", "Winter": "03"}

c_dict = {"A": ['AC ENG', 'AFAM', 'ANATOMY', 'ANESTH', 'ANTHRO', 'ARABIC', 'ART', 'ART HIS', 'ART STU', 'ARTS', 'ARTSHUM', 'ASIANAM'],
          "B": ['BANA', 'BATS', 'BIO SCI', 'BIOCHEM', 'BME', 'BSEMD'],
          "C": ['CAMPREC', 'CBEMS', 'CEM', 'CHEM', 'CHINESE', 'CLASSIC', 'COGS', 'COM LIT', 'COMPSCI', 'CRITISM', 'CSE'],
          "D": ['DANCE', 'DERM', 'DEV BIO', 'DRAMA'],
          "E": ['E ASIAN', 'EARTHSS', 'ECO EVO', 'ECON', 'ED AFF', 'EDUC', 'EECS', 'EHS', 'ENGLISH', 'ENGR', 'ENGRCEE', 'ENGRMAE', 'ENGRMSE', 'EPIDEM', 'ER MED', 'EURO ST'],
          "F": ['FAM MED', 'FIN', 'FRENCH'],
          "G": ['GERMAN', 'GLBL ME', 'GLBLCLT', 'GREEK'],
          "H": ['HEBREW', 'HINDI', 'HISTORY', 'HUMAN', 'HUMARTS'],
          "I": ['I&C SCI', 'IN4MATX', 'INT MED', 'INTL ST', 'ITALIAN'],
          "JK":['JAPANSE', 'KOREAN'],
          "L": ['LATIN', 'LAW', 'LINGUIS', 'LIT JRN', 'LPS'],
          "M": ['MATH', 'MED', 'MED ED', 'MED HUM', 'MGMT', 'MGMT EP', 'MGMT FE', 'MGMT HC', 'MGMTMBA', 'MGMTPHD', 'MIC BIO', 'MOL BIO', 'MPAC', 'MUSIC'],
          "N": ['NET SYS', 'NEURBIO', 'NEUROL', 'NUR SCI'],
          "O": ['OB/GYN', 'OPHTHAL'],
          "P": ['PATH', 'PED GEN', 'PEDS', 'PERSIAN', 'PHARM', 'PHILOS', 'PHRMSCI', 'PHY SCI', 'PHYSICS', 'PHYSIO', 'PLASTIC', 'POL SCI', 'PORTUG', 'PSY BEH', 'PSYCH', 'PUB POL', 'PUBHLTH'],
          "R": ['RAD SCI', 'RADIO', 'REL STD', 'ROTC', 'RUSSIAN'],
          "S": ['SOC SCI', 'SOCECOL', 'SOCIOL', 'SPANISH', 'SPPS', 'STATS', 'SURGERY'],
          "T-Z": ['TAGALOG', 'TOX', 'UCDC', 'UNI AFF', 'UNI STU', 'VIETMSE', 'VIS STD', 'WOMN ST', 'WRITING']
          }

def get_info():
    url = "https://www.reg.uci.edu/perl/WebSoc"
    header = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    while True:
        try:
            response = requests.post(url, data = data_input())
            break
        except: print("Order Invalid.")
    return response.text

def data_input():
    while True:
        try:
            year_term_text = input("Please input year and term (year term):")
            year_term = year_term_text.split()[0]+"-"+term[year_term_text.split()[1]]
            break
        except: print("Please enter valid year & term.")
    print("\n".join([key+":\n"+", ".join([str(index+1)+"."+c_dict[key][index] for index in range(len(c_dict[key]))]) for key in c_dict]))
    while True:
        try:
            dept_text = input("Please input department (e.g. A 1, D 4, JK 1):")
            dept = c_dict[dept_text.split()[0]][int(dept_text.split()[1])-1]
            break
        except: print("Please enter valid department.")
    course_num = input("Please input course number (or leave it blank):")
    course_code = input("Please input course code (or leave it blank):")
    
    data_form = {"YearTerm": year_term,
                 "Dept": dept,
                 "CourseNum": course_num,
                 "CourseCodes": course_code,
                 "Submit": "Display Text Results"
                 }

    return data_form
    
if __name__ == "__main__":
    info = get_info()
    print("\n\n\n--------------Search Result--------------\n\n\n")
    print(info)
