{"changed":true,"filter":false,"title":"NEWNEAPRACTICE.py","tooltip":"/NEA/NEWNEAPRACTICE.py","value":"def login():\n    \"\"\"Function used to log teacher in\"\"\"\n    loginDetails = open(\"Files/Login/LoginDetails.txt\", \"r\")\n    readLD = loginDetails.read()\n    listLD = readLD.split(\",\")\n    loginDetails.close()\n    username = str(input(\"Enter Username: \"))\n    password = str(input(\"Enter Password: \"))\n    while (username != listLD[0]) or (password != listLD[1]):\n        print(\"\\nThose login details are incorrect please re-enter them\\n\")\n        username = str(input(\"Enter Username: \"))\n        password = str(input(\"Enter Password: \"))\n    print(\"\\nThank you\\n\")\n\ndef read_file(subfile, fileName):\n    \"\"\"function reads student credentials into a multidimensional array\n       for later use\"\"\"\n    credentials = open(\"Files/\" + subfile + \"/\" + fileName, \"r\")\n    listCr = []\n    nextLine = credentials.readline()\n    while nextLine != \"\":\n        listCr.append(nextLine.split(\",\"))\n        nextLine = credentials.readline()\n    credentials.close()\n    return listCr\n\ndef get_reports():\n    reportsList = read_file(ReportsList.txt)\n    allReports = []\n    for i in range(len(\"Reports\", reportsList)):\n        allReports.append(read_file(reportsList[i][0]))\n    return allReports\n\ndef create_report(credentials):\n    ###Selection v\n    allNames = []\n    for i in credentials:\n        name = (i[3] + \" \" + i[4]).upper()\n        allNames.append(name)\n    students = []\n    credentialsList = []\n    moreStudents = True\n    moreCredentials = True\n\n    while moreStudents == True:\n        currentName = input(\"Input students name: \")\n        while (currentName.upper()) not in allNames:\n            print(\"That student doesn't exist\")\n            currentName = input(\"Input students name: \")\n\n        students.append(currentName)\n        leave = \"\"\n        while leave != \"y\" and leave != \"n\":\n            leave = input(\"Do you want to add another student enter 'y' or 'n': \")\n            if leave == \"n\":\n                moreStudents = False\n\n\n    while moreCredentials == True:\n        currentCred = input(\"Input credential: \")\n        while currentCred not in credentials[0]:\n            print(\"That credential doesn't exist\")\n            currentCred = input(\"Input credential: \")\n\n        credentialsList.append(currentCred)\n\n            \n        leave = \"\"\n        while leave != \"y\" and leave != \"n\":\n            leave = input(\"Do you want to add another credential enter 'y' or 'n': \")\n            if leave == \"n\":\n                moreCredentials = False\n    ###Create array v\n    credentialIndexs = []\n    for i in credentialsList: #Gets indexes for creds\n        cIndex = credentials[0].index(i)\n        credentialIndexs.append(cIndex)\n\n    counter = 0\n    studentIndex = []\n    for i in students: #Gets indexes for students\n        sIndex = allNames.index(i.upper())\n        studentIndex.append(sIndex)\n\n    reportList = []\n\n    titles = [\"Name\"] + credentialsList #Adds array containing column headings to the master array\n    reportList.append(titles)\n\n    for i in range(len(students)): #Adds New array for each student\n        reportList.append([])\n        reportList[i + 1].append(students[i])\n\n    for i in range(len(credentials)): #Adds Credentials into correct place in array\n        for j in range(len(credentials[i])):\n            if i in studentIndex and j in credentialIndexs:\n                reportList[students.index(allNames[i].lower()) + 1].append(credentials[i][j])\n    ###Store Array\n    reportNamesRead = open(\"Files/Reports/ReportsList.txt\", \"r\")\n    reportNames = reportNamesRead.read().split(\",\")\n    reportNamesRead.close()\n    nameOfFile = input(\"Enter Report Name: \")\n    while nameOfFile in reportNames: #Makes sure no 2 files are named the same\n        print(\"That name is taken\")\n        nameOfFile = input(\"Enter Report Name: \")\n\n    reportNames.append(nameOfFile) #Adds new file name to ReportsList\n    reportNamesWrite = open(\"Files/Reports/ReportsList.txt\", \"w\")\n    toWrite = \",\".join(map(str, reportNames))   \n    reportNamesWrite.write(toWrite)\n    reportNamesWrite.close()\n\n    report = open(\"Files/Reports/\" + nameOfFile + \".txt\", \"w\")\n\n    for i in reportList:\n        report.write(\",\".join(map(str, i)))\n        report.write(\"\\n\")\n    report.close()\n        \n    \n#\n\n#login()\ncredentials = read_file(\"credentials\", \"StudentCredentials.txt\")\nprint(credentials)\ncreate_report(credentials)\n\n#\n","undoManager":{"mark":-2,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["def login():","    \"\"\"Function used to log teacher in\"\"\"","    loginDetails = open(\"Files/Login/LoginDetails.txt\", \"r\")","    readLD = loginDetails.read()","    listLD = readLD.split(\",\")","    loginDetails.close()","    username = str(input(\"Enter Username: \"))","    password = str(input(\"Enter Password: \"))","    while (username != listLD[0]) or (password != listLD[1]):","        print(\"\\nThose login details are incorrect please re-enter them\\n\")","        username = str(input(\"Enter Username: \"))","        password = str(input(\"Enter Password: \"))","    print(\"\\nThank you\\n\")","","def read_file(subfile, fileName):","    \"\"\"function reads student credentials into a multidimensional array","       for later use\"\"\"","    credentials = open(\"Files/\" + subfile + \"/\" + fileName, \"r\")","    listCr = []","    nextLine = credentials.readline()","    while nextLine != \"\":","        listCr.append(nextLine.split(\",\"))","        nextLine = credentials.readline()","    credentials.close()","    return listCr","","def get_reports():","    reportsList = read_file(ReportsList.txt)","    allReports = []","    for i in range(len(\"Reports\", reportsList)):","        allReports.append(read_file(reportsList[i][0]))","    return allReports","","def create_report(credentials):","    ###Selection v","    allNames = []","    for i in credentials:","        name = (i[3] + \" \" + i[4]).upper()","        allNames.append(name)","    students = []","    credentialsList = []","    moreStudents = True","    moreCredentials = True","","    while moreStudents == True:","        currentName = input(\"Input students name: \")","        while (currentName.upper()) not in allNames:","            print(\"That student doesn't exist\")","            currentName = input(\"Input students name: \")","","        students.append(currentName)","        leave = \"\"","        while leave != \"y\" and leave != \"n\":","            leave = input(\"Do you want to add another student enter 'y' or 'n': \")","            if leave == \"n\":","                moreStudents = False","","","    while moreCredentials == True:","        currentCred = input(\"Input credential: \")","        while currentCred not in credentials[0]:","            print(\"That credential doesn't exist\")","            currentCred = input(\"Input credential: \")","","        credentialsList.append(currentCred)","","            ","        leave = \"\"","        while leave != \"y\" and leave != \"n\":","            leave = input(\"Do you want to add another credential enter 'y' or 'n': \")","            if leave == \"n\":","                moreCredentials = False","    ###Create array v","    credentialIndexs = []","    for i in credentialsList: #Gets indexes for creds","        cIndex = credentials[0].index(i)","        credentialIndexs.append(cIndex)","","    counter = 0","    studentIndex = []","    for i in students: #Gets indexes for students","        sIndex = allNames.index(i.upper())","        studentIndex.append(sIndex)","","    reportList = []","","    titles = [\"Name\"] + credentialsList #Adds array containing column headings to the master array","    reportList.append(titles)","","    for i in range(len(students)): #Adds New array for each student","        reportList.append([])","        reportList[i + 1].append(students[i])","","    for i in range(len(credentials)): #Adds Credentials into correct place in array","        for j in range(len(credentials[i])):","            if i in studentIndex and j in credentialIndexs:","                reportList[students.index(allNames[i].lower()) + 1].append(credentials[i][j])","    ###Store Array","    reportNamesRead = open(\"Files/Reports/ReportsList.txt\", \"r\")","    reportNames = reportNamesRead.read().split(\",\")","    reportNamesRead.close()","    nameOfFile = input(\"Enter Report Name: \")","    while nameOfFile in reportNames: #Makes sure no 2 files are named the same","        print(\"That name is taken\")","        nameOfFile = input(\"Enter Report Name: \")","","    reportNames.append(nameOfFile) #Adds new file name to ReportsList","    reportNamesWrite = open(\"Files/Reports/ReportsList.txt\", \"w\")","    toWrite = \",\".join(map(str, reportNames))   ","    reportNamesWrite.write(toWrite)","    reportNamesWrite.close()","","    report = open(\"Files/Reports/\" + nameOfFile + \".txt\", \"w\")","","    for i in reportList:","        report.write(\",\".join(map(str, i)))","        report.write(\"\\n\")","    report.close()","        ","    ","#","","#login()","credentials = read_file(\"credentials\", \"StudentCredentials.txt\")","print(credentials)","create_report(credentials)","","#",""],"id":1}]]},"ace":{"folds":[],"scrolltop":1908.5,"scrollleft":0,"selection":{"start":{"row":128,"column":0},"end":{"row":128,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":111,"state":"start","mode":"ace/mode/python"}},"timestamp":1509382619674}