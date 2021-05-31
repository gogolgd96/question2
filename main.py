import csv
maths = []
biology = []
english = []
physics = []
chemistry = []
hindi = []
with open('Student_marks_list.csv','r') as myfile:
	this_reader = csv.reader(myfile, delimiter=",")
	header = next(this_reader)
	#print(header)
	for line in this_reader:
		maths.append(int(line[1]))
		biology.append(int(line[2]))
		english.append(int(line[3]))
		physics.append(int(line[4]))
		chemistry.append(int(line[5]))
		hindi.append(int(line[6]))
myfile.close()
maths_max=0
for i in maths:
	if i>maths_max:
		maths_max=i 
biology_max=0
for i in biology:
	if i>biology_max:
		biology_max=i 
english_max=0
for i in english:
	if i>english_max:
		english_max=i 
physics_max=0
for i in physics:
	if i>physics_max:
		physics_max=i 
chemistry_max=0
for i in chemistry:
	if i>chemistry_max:
		chemistry_max=i 
hindi_max=0
for i in hindi:
	if i>hindi_max:
		hindi_max=i
maths_topper=[]
biology_topper=[]
english_topper=[]
physics_topper=[]
chemistry_topper=[]
hindi_topper=[]
with open('Student_marks_list.csv','r') as myfile:
	this_reader2 = csv.reader(myfile, delimiter=",")
	header = next(this_reader2)
	for line in this_reader2:
		if int(line[1])==maths_max:
			maths_topper.append(line[0])
		if int(line[2])==biology_max:
			biology_topper.append(line[0])
		if int(line[3])==english_max:
			english_topper.append(line[0])
		if int(line[4])==physics_max:
			physics_topper.append(line[0])
		if int(line[5])==chemistry_max:
			chemistry_topper.append(line[0])
		if int(line[6])==hindi_max:
			hindi_topper.append(line[0])
myfile.close()
print("The topper in maths are: ",maths_topper)
print("The topper in biology are: ",biology_topper)
print("The topper in english are: ",english_topper)
print("The topper in physics are: ",physics_topper)
print("The topper in chemistry are: ",chemistry_topper)
print("The topper in hindi are: ",hindi_topper)
total_marks=[]
with open('Student_marks_list.csv','r') as myfile:
	this_reader3 = csv.reader(myfile, delimiter=',')
	header = next(this_reader3)
	for line in this_reader3:
		total_marks.append(int(line[6])+int(line[1])+int(line[2])+int(line[3])+int(line[4])+int(line[5]))
	total_marks.sort(reverse=True)
	for line in this_reader3:
		if total_marks[0]==int(line[6])+int(line[1])+int(line[2])+int(line[3])+int(line[4])+int(line[5]):
			print("The 1st rank holder is ",line[0])
		if total_marks[1]==int(line[6])+int(line[1])+int(line[2])+int(line[3])+int(line[4])+int(line[5]):
			print("The 2nd rank holder is ",line[0])
		if total_marks[2]==int(line[6])+int(line[1])+int(line[2])+int(line[3])+int(line[4])+int(line[5]):
			print("The 3rd rank holder is ",line[0])
myfile.close()
