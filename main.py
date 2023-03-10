import os
import csv
import shutil

# Constants
path = './Students/'
students = os.listdir(path)

def sep():
    print("- - - - - - - - - - - - - - -")

def show_report(rFile):
    with open(rFile, 'r') as file:
        reader = csv.reader(file)
        greatest_grade = 0
        current_grade = 0
        for row in reader:
            print(row)
            if row[0] != "SUBJECT":
                current_grade = current_grade + int(row[1])
                greatest_grade = greatest_grade + int(row[2])
        if current_grade != 0:
            percentage = current_grade * 100 / greatest_grade
            print(" ----- %" + "{:.2f}".format(percentage) + " ----- ")

def show_students():
    id = 1
    for student in students:
        print(str(id) + " " + student)
        id = id + 1

def add_entry():
    new_subject = input("[?] Subject: ")
    new_grade = input("[?] Mark: ")
    new_full = input("[?] Full Mark: ")
    return [new_subject, new_grade, new_full]

def entry_bool(rFile):
    add_entry_bool = input("[?] Do you want to add entries to it? [y/n] ")
    if add_entry_bool == 'y' or add_entry_bool == 'Y':
        new_entry = add_entry()
        with open(rFile, 'a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow([new_entry[0], new_entry[1], new_entry[2]])
            print("[+] Added new entry!")
        show_report(rFile)
        entry_bool(rFile)

def enter_student_profile(sName):
    if sName in students:
        month = input("[?] Report's Month (number): ")
        year = input("[?] Report's Year (last two digits): ")
        readingFile = path + sName + "/" + month + "-" + year + ".csv"
        if os.path.exists(readingFile) and os.stat(readingFile).st_size != 0:
            sep()
            show_report(readingFile)
            entry_bool(readingFile)
        else:
            with open(readingFile, 'a') as file:
                writer = csv.writer(file, lineterminator='\n')
                print("[+] Added report card for the " + str(month) + " month of 20" + year + " !")
                writer.writerow(["SUBJECT", "MARK", "FULL MARK"])
            sep()
            show_report(readingFile)
            sep()
            entry_bool(readingFile)

def main():
    show_students()
    sep()
    print("[1] Enter\t[2] Add\n[0] Print")
    option = input("Choose an index: ")
    # Print
    if int(option) == 0:
        sep()
        month = input("[?] Report's Month (number): ")
        year = input("[?] Report's Year (last two digits): ")
        folder_name = input("[?] Folder's Name to copy to: ")
        os.mkdir("./" + folder_name)
        copy_path = "./" + folder_name + "/"
        for student_folder in students:
            readingFile = path + student_folder + "/" + month + "-" + year + ".csv"
            if os.path.exists(readingFile):
                shutil.copy(readingFile, copy_path)
                old_name = copy_path + month + "-" + year + ".csv"
                new_name = copy_path + student_folder + "-" + month + "-" + year + ".csv"
                os.rename(old_name, new_name)
        print("[+] Copyed the Files!")
    # Enter
    elif int(option) == 1:
        student_id = input("Student's ID: ")
        student_name = students[int(student_id) - 1]
        print("[!] Opened " + student_name + "'s profile...")
        print("[!] Available files are: " + str(os.listdir(path + student_name)))
        enter_student_profile(student_name)
    # Add
    elif int(option) == 2:
        student_name = input("Student's Name: ")
        if student_name not in students:
            os.mkdir(path + student_name) # Added Student Folder
            students.append(student_name)
            print("[+] Added " + student_name + " to the students' database!")
            sep()
            main()
    else:
        print("[!] Out of index.")
    
if __name__ == "__main__":
    main()