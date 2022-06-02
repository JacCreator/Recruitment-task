#needed imports
import os
import pathlib
import re
import csv


class Emails:
    #general class construct
    directory = ''

    def __init__(self, pwd):
        self.directory = pwd

    @classmethod
    def check(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.search(regex, email)):
            return True
        else:
            return False


    #task1 method
    def is_valid(self): # (--incorrect-emails, -ic)
        l = list()
        for file_name in os.listdir(self.directory):
            absolutePath = self.directory + '\\' + file_name
            # opening *.txt files
            if pathlib.Path(absolutePath).suffix == '.txt':
                with open(absolutePath, 'r') as txt_file:
                    for line in txt_file:
                        if self.check(line) == False:
                            incorrectEmail = line.strip('\n')
                            l.append(incorrectEmail)

            #opening *.csv files
            elif pathlib.Path(absolutePath).suffix == '.csv':
                with open(absolutePath, 'r', newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    #skipping the header of csv file
                    next(csv_reader)
                    for row in csv_reader:
                        if self.check(row[1]) == False:
                            l.append(row[1])

        txt_file.close()
        csv_file.close()

        return l


    # task2 method
    def searchByText(self, string): # (--search str, -s str)
        l = list()
        for file_name in os.listdir(self.directory):
            absolutePath = self.directory + '\\' + file_name
            # opening *.txt files
            if pathlib.Path(absolutePath).suffix == '.txt':
                with open(absolutePath, 'r') as txt_file:
                    for line in txt_file:
                        if string in line:
                            stripped_line = line.strip('\n')
                            l.append(stripped_line)

            #opening *.csv files
            elif pathlib.Path(absolutePath).suffix == '.csv':
                with open(absolutePath, 'r', newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    #skipping the header of csv file
                    next(csv_reader)
                    for row in csv_reader:
                        if string in row[1]:
                            l.append(row[1])

        txt_file.close()
        csv_file.close()

        return l


    # task3 method
    def groupByDomain(self): # (--group-by-domain, -gbd)
        d = dict()
        for file_name in os.listdir(self.directory):
            absolutePath = self.directory + '\\' + file_name
            # opening *.txt files
            if pathlib.Path(absolutePath).suffix == '.txt':
               with open(absolutePath, 'r') as txt_file:
                    for line in txt_file:
                        line = line.strip('\n')
                        domain = line[line.find("@"):]
                        words = domain.split(" ")
                        for word in words:
                            if word in d:
                                d[word] += 1
                            else:
                                d[word] = 1

            #opening *.csv files
            elif pathlib.Path(absolutePath).suffix == '.csv':
                with open(absolutePath, 'r', newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    # skipping the header of csv file
                    next(csv_reader)
                    for row in csv_reader:
                        domain = row[1][row[1].find("@"):]
                        words = domain.split(" ")
                        for word in words:
                            if word in d:
                                d[word] += 1
                            else:
                                d[word] = 1

        for key in list(d.keys()):
            if key[0] == '@':
                print(key, ":", d[key])


        txt_file.close()
        csv_file.close()


    # task4 method
    def findNotInLogs(self):
    # (--find-emails-not-in-logs path_to_logs_file, -feil path_to_logs_file)
        s = set()
        for file_name in os.listdir(self.directory):
            logPath = str(self.directory).replace('emails', 'email-sent.logs')
            absolutePath = self.directory + '\\' + file_name
            #opening *.txt files
            log_file = open(logPath, 'r')
            read_log_file = log_file.read()
            if pathlib.Path(absolutePath).suffix == '.txt':
                with open(absolutePath, 'r') as txt_file:
                    for line in txt_file:
                        line = line.strip('\n')
                        if line not in read_log_file:
                            if self.check(line):
                                s.add(line)

            # opening *.csv files
            elif pathlib.Path(absolutePath).suffix == '.csv':
                with open(absolutePath, 'r', newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                     # skipping the header of csv file
                    next(csv_reader)
                    for row in csv_reader:
                        if row[1] not in read_log_file:
                            if self.check(row[1]):
                                s.add(row[1])

        txt_file.close()
        csv_file.close()
        log_file.close()

        return s

def checkInput(num, basic='integer'):
    #integers verification
    if basic == 'integer':
        try:
            num = int(num)
        except Exception as e:
            print(e)
        if not type(num) is int:
            print('Invalid input!')
            return False
            # raise TypeError("Only integers are allowed")
            # Throwing a expection is not neccessary
            # Script make user to enter valid input next time
        if num < 0 or num > 4:
            raise ValueError('Incorrect option, try again!')
        else:
            return True

    #strings verification
    elif basic == 'string':
        num = str(num)
        if not type(num) is str:
            print('Invalid input!')
            #raise TypeError("Only strings are allowed")
            # Throwing a expection is not neccessary
            # Script make user to enter valid input next time
            return False
        else:
            return True




if __name__ == '__main__':
    #finding current directorys
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    path_parent += '\emails'
    #-------------------------
    emails_object = Emails(path_parent)

    while True:
        print('Which task answer do you want to check?')
        print('1 - task one')
        print('2 - task two')
        print('3 - task three')
        print('4 - task fourth')
        print('0 - exit script')
        #correct options
        x = input()

        if checkInput(x) == False:
            continue

        #task1
        if(int(x) == 1):
            print('Number of invalid emails: '
                  + str(len(emails_object.is_valid())))
            print(*emails_object.is_valid(), sep='\n')


        #task2
        elif(int(x) == 2):
            #input validation
            while True:
                user_choice = \
                    input('Write phrase and we find equivalent email:\n')
                if checkInput(user_choice, basic='string') == False:
                    continue
                break

            print("Found emails with user phrase in email: "
                  + str(len(emails_object.searchByText(user_choice))))
            print(*emails_object.searchByText(user_choice), sep='\n')

        #task3
        elif(int(x) == 3):
            print('Number of occurrences of each email address')
            print(emails_object.groupByDomain())

        #task4
        elif(int(x) == 4):
            print('Emails not sent: '
                  + str(len(emails_object.findNotInLogs())))
            print(*sorted(emails_object.findNotInLogs()), sep='\n')

        elif(int(x) == 0):
            print('Dziękuję za uwagę i proszę o przeczytanie pliku README.')
            break






