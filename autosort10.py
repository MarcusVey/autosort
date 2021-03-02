import os
import shutil
import sys
import re
from time import sleep

folder_path = r'C:\Users\marcus.eriksson\OneDrive - YILDIRIM HOLDING A.S\Pictures\Camera Roll\2021'
# folder_path = r'\\192.168.110.117\lagring\Marcus_Phone'
prere1 = re.compile(r"^[a-zA-Z]{5,8}")
prere2 = re.compile(r"^[a-z]{5,8}\_[a-z]{5,8}")
datere = re.compile(r"(\d{8}\_\d{6})")
prefixre = re.compile(r"-IMG_")

os.chdir(folder_path)

def monthConversion(smonth):

    return {
            '01' : '1. JANUARI ' + year,
            '02' : '2. FEBRUARI ' + year,
            '03' : '3. MARS ' + year,
            '04' : '4. APRIL ' + year,
            '05' : '5. MAJ ' + year,
            '06' : '6. JUNI ' + year,
            '07' : '7. JULI ' + year,
            '08' : '8. AUGUSTI ' + year,
            '09' : '9. SEPTEMBER ' + year,
            '10' : '10. OKTOBER ' + year,
            '11' : '11. NOVEMBER ' + year,
            '12' : '12. DECEMBER ' + year
    } [smonth]

while(True):

    for file in os.listdir(folder_path):

        if os.path.isfile(file) and file.endswith('.jpg'):
                
            prefix_split = prefixre.split(file, maxsplit=1)

            try:
                year = prefix_split[1][0:4]
                nmonth = prefix_split[1][4:6]
                day = prefix_split[1][6:8]
                prefix = prefix_split[0]
            except IndexError as Err:
                print(Err)
                print("IndexError, could not split out prefix on", file)
                
            if prefixre.search(file) != None and datere.search(file) != None and prere1.search(file) or prere2.search(file) != None:

                image_path = monthConversion(nmonth) + '/' + day + '/' + prefix

                try:
                    os.makedirs(folder_path + '/' + image_path)
                    print('\n' + folder_path + '/' + image_path, "does not exist, creating directory.")
                except:
                    pass

                try:
                    shutil.move(file, folder_path + '/' + image_path)
                    print("\nMoving", file, "to", folder_path + '/' + image_path)
                except:
                    pass

            elif datere.search(file) != None:

                r1 = datere.split(file)
                print(r1)

                year = r1[1][0:4]
                month = r1[1][4:6]
                day = r1[1][6:8]

                unsort_path = monthConversion(month) + '/' + day + '/Ej sorterbart/'

                try:
                    os.makedirs(folder_path + '/' + unsort_path)
                    print('\n' + folder_path + '/' + unsort_path, "does not exist, creating directory.")
                except:
                    pass

                try:
                    shutil.move(file, folder_path + '/' + unsort_path)
                    print("\nMoving", file, "to", folder_path + '/' + unsort_path)
                except:
                    pass

            else:
                pass


    print("\nAll images are sorted")
    for i in range(60, 0, -1):
        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()
        sleep(1)