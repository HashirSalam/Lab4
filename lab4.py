
#https://github.com/HashirSalam/Lab4.git
import csv

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)



class Data:

   def __init__(self,acitivity, user,priority):
      self.date = ""  
      self.activity = acitivity
      self.user = user
      self.priority = priority
 
   def displayData(self):
      print " Activity: ", self.activity , ", User : ", self.user ,  ", Priority: ", self.priority



original = file('Academic _Schedule.csv', 'rU')
reader = csv.reader(original)
print "Loading Please Wait .... \n\n\n\n"



totalBandwidth = 800
totalStudents = 10500
toalFaculty = 1500
courses = 2000

activities = []
uactivities = {}

#we know that the maximum number of users simultaneously connected with LMS has never increased above 65%.
#6 hr 4 slots

for rows in reader:

     activities.append(rows[2])



activities = set(activities)        #getting unique entries

for a in activities:
    if (a == "Lab Task Upload(5pm)"):
        data1 = Data(a ,"Student","1st")
                
    elif (a == "Lecture Download"):
        data2 = Data(a ,"Student","3rd")   
    elif (a == "Data Backup(1am-2am)" or a == "Data Backup(3am-4am)"):
        data3 = Data(a ,"System","1st")
    elif (a == "Assignment Submission(12am)"):
        data4 = Data(a ,"Student","2nd")
    elif (a == "Assignment Grading"):
        data5 = Data(a ,"Faculty","3rd")
    elif (a == "1st Student Feedback" or a == "2nd Student Feedback"):
        data6 = Data(a ,"Student","4th")  
    elif (a == "Student Result Comments"):
        data7 = Data(a ,"Student","5th")   
    elif (a == "Project Submission(12am)"):
        data8 = Data(a ,"Student","1st")
    elif (a == "Quiz Grading" or a == "Project Grading"):
        data9 = Data(a ,"Faculty","3rd") 
    elif (a == "New User Registration"):
        data10 = Data(a ,"Student","2nd")   
    elif (a == "Final Grading"):
        data11 = Data(a ,"Faculty","2nd")  
    elif (a == "Project Upload Link Creation"):
        data12 = Data(a ,"Faculty","1st")   
    elif (a == "Maintenance"):
        data13 = Data(a ,"System","1st")   
    elif (a == "Lecture Preparation"):
        data14 = Data(a ,"Faculty","4th")  
    elif (a == "Assignment Upload"):
        data15 = Data(a ,"Student","1st") 
    elif (a == "Course Registration"):
        data16 = Data(a ,"Student","4th") 
    elif (a == "ESE GuideLine Update"):
        data17 = Data(a ,"Faculty","5th")

data1.displayData()
data2.displayData()
data3.displayData()
data4.displayData()
data5.displayData()
data6.displayData()
data7.displayData()
data8.displayData()
data9.displayData()
data10.displayData()
data11.displayData()
data12.displayData()
data13.displayData()
data14.displayData()
data15.displayData()
data16.displayData()
data17.displayData()


    

arrayofdata=[ ["Activity",'User','Prirority'] ,[data1.activity ,data1.user , data1.priority ] ,[data2.activity ,data2.user , data2.priority ] ,[data3.activity ,data3.user , data3.priority ] ,[data4.activity ,data4.user , data4.priority ] ,[data5.activity ,data5.user , data5.priority ] ,[data6.activity ,data6.user , data6.priority ] ,[data7.activity ,data7.user , data7.priority ] ,[data7.activity ,data7.user , data7.priority ] ,[data8.activity ,data8.user , data8.priority ] ,[data9.activity ,data9.user , data9.priority ] ,[data10.activity ,data10.user , data10.priority ] ,[data11.activity ,data11.user , data11.priority ] ,[data12.activity ,data12.user , data12.priority ] ,[data13.activity ,data13.user , data13.priority ] ,[data14.activity ,data14.user , data14.priority ] ,[data15.activity ,data15.user , data15.priority ] ,[data16.activity ,data16.user , data16.priority ] ,[data17.activity ,data17.user , data17.priority ]  ]
             
with open('output.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in arrayofdata:
        thedatawriter.writerow(row)
