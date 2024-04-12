{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ML ASSIGNMENT 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### QUESTION 1\n",
    "\n",
    "The following is a list of 10 students ages:\n",
    "\n",
    "ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]\n",
    "\n",
    "• Sort the list and find the min and max age\n",
    "\n",
    "• Add the min age and the max age again to the list\n",
    "\n",
    "• Find the median age (one middle item or two middle items divided by two)\n",
    "\n",
    "• Find the average age (sum of all items divided by their number)\n",
    "\n",
    "• Find the range of the ages (max minus min)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the sorted listed of ages:  [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]\n",
      "minimum age:  19\n",
      "maximum age:  26\n"
     ]
    }
   ],
   "source": [
    "#Sort the list and find the min and max age\n",
    "ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]\n",
    "ages.sort() #Sorting the list using sort() method\n",
    "print(\"the sorted listed of ages: \",ages)\n",
    "\n",
    "min_age=min(ages) #minimum of ages in the given list\n",
    "max_age=max(ages) #maximum of ages in the given list\n",
    "\n",
    "print(\"minimum age: \",min_age)\n",
    "print(\"maximum age: \",max_age)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "original length:  10\n",
      "Length after appending:  12\n"
     ]
    }
   ],
   "source": [
    "#Add the min age and the max age again to the list\n",
    "print(\"original length: \",len(ages))\n",
    "ages.append(min_age) #appending minimum age again to the list of ages\n",
    "ages.append(max_age) #appending maximum age again to the list of ages\n",
    "\n",
    "print(\"Length after appending: \",len(ages))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ages:  [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]\n",
      "median:  24.0\n"
     ]
    }
   ],
   "source": [
    "# Find the median age (one middle item or two middle items divided by two)\n",
    "print(\"ages: \",ages)\n",
    "length=len(ages)\n",
    "if(length%2==0):\n",
    "    #find one of the two middle indices of the list\n",
    "    ind=length//2-1 \n",
    "    #calculating median\n",
    "    med=(ages[ind]+ages[ind+1])/2 \n",
    "else:\n",
    "    #in the case of dd length, the median is just the middle element\n",
    "    med=ages[length//2] \n",
    "print(\"median: \",med)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "average:  22.75\n"
     ]
    }
   ],
   "source": [
    "#Find the average age (sum of all items divided by their number)\n",
    "\n",
    "total=sum(ages) #find the sum of all eages in the list usinf sum() function\n",
    "avg=total/length\n",
    "print(\"average: \",avg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Range:  7\n"
     ]
    }
   ],
   "source": [
    "#Find the range of the ages (max minus min)\n",
    "range=max(ages)-min(ages)\n",
    "print(\"Range: \",range)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### QUESTION 2\n",
    "• Create an empty dictionary called dog\n",
    "\n",
    "• Add name, color, breed, legs, age to the dog dictionary\n",
    "\n",
    "• Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary\n",
    "\n",
    "• Get the length of the student dictionary\n",
    "\n",
    "• Get the value of skills and check the data type, it should be a list\n",
    "\n",
    "• Modify the skills values by adding one or two skills\n",
    "\n",
    "• Get the dictionary keys as a list\n",
    "\n",
    "• Get the dictionary values as a lisT"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length:  0\n"
     ]
    }
   ],
   "source": [
    "#Create an empty dictionary called dog\n",
    "\n",
    "dog=dict() #intializing an empty dictionary\n",
    "print(\"length: \",len(dog))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'snoopy', 'color': 'black', 'breed': 'poodle', 'legs': 4, 'age': 2}\n"
     ]
    }
   ],
   "source": [
    "#Add name, color, breed, legs, age to the dog dictionary\n",
    "dog[\"name\"]=\"snoopy\"\n",
    "dog[\"color\"]=\"black\"\n",
    "dog[\"breed\"]=\"poodle\"\n",
    "dog[\"legs\"]=4\n",
    "dog[\"age\"]=2 \n",
    "\n",
    "print(dog)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student details: \n",
      "{'first_name': 'Pavani Reddy', 'last_name': 'Katkuri', 'gender': 'Female', 'age': 23, 'Marital_status': 'Single', 'Skills': ['C', 'C++', 'Java', 'Python', 'Cyber Security', 'Machine Learning', 'Cloud Computing'], 'country': 'India', 'City': 'Hyderabad', 'address': 'Ecil'}\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Create a student dictionary and add first_name, last_name, gender, \n",
    "age, marital status, skills, country, city and address as keys for the dictionary\n",
    "'''\n",
    "#initializing empty student dictionary\n",
    "student={}\n",
    "\n",
    "#adding irst_name, last_name, gender, age, marital status, skills, country, city\n",
    "student[\"first_name\"]=\"Pavani Reddy\"\n",
    "student[\"last_name\"]=\"Katkuri\"\n",
    "student[\"gender\"]=\"Female\"\n",
    "student[\"age\"]=23\n",
    "student[\"Marital_status\"]=\"Single\"\n",
    "student[\"Skills\"]=[\"C\",\"C++\",\"Java\",\"Python\",\"Cyber Security\",\"Machine Learning\",\"Cloud Computing\"]\n",
    "student[\"country\"]=\"India\"\n",
    "student[\"City\"]=\"Hyderabad\"\n",
    "student[\"address\"]=\"Ecil\"\n",
    "\n",
    "print(\"Student details: \")\n",
    "print(student)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Student length:  9\n"
     ]
    }
   ],
   "source": [
    "#Get the length of the student dictionary\n",
    "dict_len=len(student)\n",
    "print(\"Student length: \",dict_len)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['C', 'C++', 'Java', 'Python', 'Cyber Security', 'Machine Learning', 'Cloud Computing']\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "#Get the value of skills and check the data type, it should be a list\n",
    "student_skills=student[\"Skills\"] #Getting the value of skills of student\n",
    "print(student_skills)\n",
    "skills_type=type(student_skills) #getting the data type of skills key\n",
    "print(skills_type)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['C', 'C++', 'Java', 'Python', 'Cyber Security', 'Machine Learning', 'Cloud Computing', 'HTML']\n",
      "['C', 'C++', 'Java', 'Python', 'Cyber Security', 'Machine Learning', 'Cloud Computing', 'HTML', 'CSS']\n"
     ]
    }
   ],
   "source": [
    "#Modify the skills values by adding one or two skills\n",
    "student[\"Skills\"].append(\"HTML\") #appending a new skill to the value of skills of student\n",
    "print(student[\"Skills\"])\n",
    "student[\"Skills\"].append(\"CSS\")\n",
    "print(student[\"Skills\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The keys are: \n",
      "['first_name', 'last_name', 'gender', 'age', 'Marital_status', 'Skills', 'country', 'City', 'address']\n"
     ]
    }
   ],
   "source": [
    "#Get the dictionary keys as a list\n",
    "keys_list=[] #initializing an empty list to store keys\n",
    "for k,v in student.items():\n",
    "    keys_list.append(k)\n",
    "print(\"The keys are: \")\n",
    "print(keys_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The values are: \n",
      "['Pavani Reddy', 'Katkuri', 'Female', 23, 'Single', ['C', 'C++', 'Java', 'Python', 'Cyber Security', 'Machine Learning', 'Cloud Computing', 'HTML', 'CSS'], 'India', 'Hyderabad', 'Ecil']\n"
     ]
    }
   ],
   "source": [
    "#Get the dictionary values as a lisT\n",
    "values_list=[] #initializing an empty list to store values\n",
    "for k,v in student.items():\n",
    "    values_list.append(v)\n",
    "print(\"The values are: \")\n",
    "print(values_list)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### QUESTION 3\n",
    "• Create a tuple containing names of your sisters and your brothers (imaginary siblings are \n",
    "fine)\n",
    "\n",
    "• Join brothers and sisters tuples and assign it to siblings\n",
    "\n",
    "• How many siblings do you have?\n",
    "\n",
    "• Modify the siblings tuple and add the name of your father and mother and assign it to \n",
    "family_member"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type:  <class 'tuple'>\n",
      "Brothers: \n",
      "('Sai', 'Bunny', 'Arjun', 'Vishnu')\n",
      "\n",
      "type:  <class 'tuple'>\n",
      "Sisters: \n",
      "('Bhargavi', 'Roopa', 'Honey', 'Pinky')\n"
     ]
    }
   ],
   "source": [
    "#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)\n",
    "\n",
    "brothers=() #initializing an empty tuple to store brothers\n",
    "sisters=() #initializing an empty tuple to store sisters\n",
    "\n",
    "#adding elemets to brothers\n",
    "brothers = brothers+(\"Sai\",) \n",
    "brothers += (\"Bunny\",)\n",
    "brothers += (\"Arjun\",)\n",
    "brothers += (\"Vishnu\",)\n",
    "\n",
    "print(\"type: \",type(brothers))\n",
    "print(\"Brothers: \")\n",
    "print(brothers)\n",
    "\n",
    "print()\n",
    "#adding elements to sisters\n",
    "sisters+=(\"Bhargavi\",\"Roopa\",\"Honey\",\"Pinky\",)\n",
    "\n",
    "print(\"type: \",type(sisters))\n",
    "print(\"Sisters: \")\n",
    "print(sisters)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type:  <class 'tuple'>\n",
      "siblings: \n",
      "('Sai', 'Bunny', 'Arjun', 'Vishnu', 'Bhargavi', 'Roopa', 'Honey', 'Pinky')\n"
     ]
    }
   ],
   "source": [
    "#Join brothers and sisters tuples and assign it to siblings\n",
    "siblings=() #Initializing an empty tuple\n",
    "siblings=(brothers+sisters) #concatenating two tuples using '+' operator\n",
    "print(\"type: \",type(siblings))\n",
    "print(\"siblings: \")\n",
    "print(siblings)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total no.of siblings:  8\n"
     ]
    }
   ],
   "source": [
    "#How many siblings do you have?\n",
    "print(\"total no.of siblings: \",len(siblings))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type:  <class 'tuple'>\n",
      "family member: \n",
      "('Sai', 'Bunny', 'Arjun', 'Vishnu', 'Bhargavi', 'Roopa', 'Honey', 'Pinky', 'Reddy', 'Shobha')\n"
     ]
    }
   ],
   "source": [
    "#Modify the siblings tuple and add the name of your father and mother and assign it to family_member\n",
    "family_member=() #initializing an empty tuple\n",
    "family_member += siblings + (\"Reddy\",\"Shobha\")\n",
    "\n",
    "print(\"type: \",type(family_member))\n",
    "print(\"family member: \")\n",
    "print(family_member)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### QUESITON 4\n",
    "it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}\n",
    "\n",
    "A = {19, 22, 24, 20, 25, 26}\n",
    "\n",
    "B = {19, 22, 20, 25, 26, 24, 28, 27}\n",
    "\n",
    "age = [22, 19, 24, 25, 26, 24, 25, 24]\n",
    "\n",
    "• Find the length of the set it_companies\n",
    "\n",
    "• Add 'Twitter' to it_companies\n",
    "\n",
    "• Insert multiple IT companies at once to the set it_companies\n",
    "\n",
    "• Remove one of the companies from the set it_companies\n",
    "\n",
    "• What is the difference between remove and discard\n",
    "\n",
    "• Join A and B\n",
    "\n",
    "• Find A intersection B\n",
    "\n",
    "• Is A subset of B\n",
    "\n",
    "• Are A and B disjoint sets\n",
    "\n",
    "• Join A with B and B with A\n",
    "\n",
    "• What is the symmetric difference between A and B\n",
    "\n",
    "• Delete the sets completely\n",
    "\n",
    "• Convert the ages to a set and compare the length of the list and the set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length:  7\n"
     ]
    }
   ],
   "source": [
    "#Find the length of the set it_companies\n",
    "it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}\n",
    "print(\"length: \",len(it_companies))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "length:  8\n",
      "{'Facebook', 'IBM', 'Amazon', 'Microsoft', 'Google', 'Oracle', 'Apple', 'Twitter'}\n"
     ]
    }
   ],
   "source": [
    "#Add 'Twitter' to it_companies\n",
    "it_companies.add('Twitter')\n",
    "print(\"length: \",len(it_companies))\n",
    "print(it_companies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Facebook', 'IBM', 'Amazon', 'Microsoft', 'HSBC', 'EPAM', 'Google', 'Oracle', 'Apple', 'Infosys', 'Adobe', 'Twitter'}\n"
     ]
    }
   ],
   "source": [
    "#Insert multiple IT companies at once to the set it_companies\n",
    "dup_set={'Adobe','HSBC','EPAM','Infosys'} #initializing a set\n",
    "it_companies.update(dup_set) #adding the second set\n",
    "\n",
    "print(it_companies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Facebook', 'IBM', 'Amazon', 'Microsoft', 'HSBC', 'Google', 'Oracle', 'Apple', 'Infosys', 'Adobe', 'Twitter'}\n"
     ]
    }
   ],
   "source": [
    "#Remove one of the companies from the set it_companies\n",
    "it_companies.remove('EPAM') #removing the company 'EPAM'\n",
    "print(it_companies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A:  {19, 20, 22, 24, 25, 26}\n",
      "B:  {19, 20, 22, 24, 25, 26, 27, 28}\n"
     ]
    }
   ],
   "source": [
    "#Join A and B\n",
    "A = {19, 22, 24, 20, 25, 26}\n",
    "B = {19, 22, 20, 25, 26, 24, 28, 27}\n",
    "A.union(B) #all unique elements and all common elements will be printed once\n",
    "B.union(A)\n",
    "print(\"A: \",A)\n",
    "print(\"B: \",B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The common elements are: \n",
      "{19, 20, 22, 24, 25, 26}\n"
     ]
    }
   ],
   "source": [
    "#Find A intersection B\n",
    "A = {19, 22, 24, 20, 25, 26}\n",
    "B = {19, 22, 20, 25, 26, 24, 28, 27}\n",
    "int_Set=A.intersection(B)\n",
    "print(\"The common elements are: \")\n",
    "print(int_Set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#Is A subset of B\n",
    "res=A.issubset(B)\n",
    "print(res) #returns true or false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No\n"
     ]
    }
   ],
   "source": [
    "#Are A and B disjoint sets\n",
    "res1=A.isdisjoint(B)\n",
    "if res1==True:\n",
    "    print(\"A and B are dijoint\")\n",
    "else:\n",
    "    print(\"No\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A:  {19, 20, 22, 24, 25, 26}\n",
      "B:  {19, 20, 22, 24, 25, 26, 27, 28}\n"
     ]
    }
   ],
   "source": [
    "#Join A with B and B with A\n",
    "A = {19, 22, 24, 20, 25, 26}\n",
    "B = {19, 22, 20, 25, 26, 24, 28, 27}\n",
    "A.union(B) #all unique elements and all common elements will be printed once\n",
    "B.union(A)\n",
    "print(\"A: \",A)\n",
    "print(\"B: \",B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{27, 28}\n"
     ]
    }
   ],
   "source": [
    "#What is the symmetric difference between A and B\n",
    "sym_dif=A.symmetric_difference(B)\n",
    "print(sym_dif)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "set()\n",
      "set()\n"
     ]
    }
   ],
   "source": [
    "# Delete the sets completely\n",
    "A.clear() #deleting setA completelt from memory\n",
    "B.clear() ##deleting setA completelt from memory\n",
    "print(A)\n",
    "print(B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List ages length:  12\n",
      "set ages length:  6\n"
     ]
    }
   ],
   "source": [
    "#Convert the ages to a set and compare the length of the list and the set.\n",
    "set_age=set(ages)\n",
    "print(\"List ages length: \",len(ages))\n",
    "print(\"set ages length: \",len(set_age))\n",
    "\n",
    "#the lengths are differnet because the set removes the duplicated ages"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 5\n",
    "\n",
    "The radius of a circle is 30 meters.\n",
    "\n",
    "• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_\n",
    "\n",
    "• Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_\n",
    "\n",
    "• Take radius as user input and calculate the area."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area:  2826.0\n"
     ]
    }
   ],
   "source": [
    "#Calculate the area of a circle and assign the value to a variable name of area_of_circle\n",
    "#initializing radius ad rad\n",
    "rad=30\n",
    "#calcluating area of circle\n",
    "area_of_circle=3.14*rad*rad\n",
    "print(\"Area: \",area_of_circle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Circumference:  188.4\n"
     ]
    }
   ],
   "source": [
    "#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle\n",
    "_circum_of_circle=2*3.14*rad\n",
    "print(\"Circumference: \",_circum_of_circle)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius: 20\n",
      "Area from user input radius:  1256.0\n"
     ]
    }
   ],
   "source": [
    "rad_inp=int(input(\"Enter radius: \"))\n",
    "new_area=3.14*rad_inp*rad_inp\n",
    "print(\"Area from user input radius: \",new_area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 6\n",
    "“I am a teacher and I love to inspire and teach people”\n",
    "\n",
    "• How many unique words have been used in the sentence? Use the split methods and set to get the unique words.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total no.of unique words:  6\n"
     ]
    }
   ],
   "source": [
    "s=\"I am a teacher and I love to inspire and teach people\" #initializing a string\n",
    "count=0 #initializing the count of unique wors to 0\n",
    "unique_s=s.split() #using split to split each word in the given string\n",
    "for word in unique_s:\n",
    "    if s.count(word)==1: #getting the count of each word in th estring\n",
    "        count+=1\n",
    "print(\"total no.of unique words: \",count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 7\n",
    "Use a tab escape sequence to get the following lines.\n",
    "\n",
    "     Name Age Country City\n",
    " \n",
    "     Asabeneh 250 Finland Helsinki"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name\tAge\tCountry\tCity\n",
      "Nikesh\t250\tIndia\tHyderabad\n"
     ]
    }
   ],
   "source": [
    "#\\t escape sequence\n",
    "print(\"Name\\tAge\\tCountry\\tCity\")\n",
    "print(\"Nikesh\\t250\\tIndia\\tHyderabad\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 8\n",
    "Use the string formatting method to display the following:\n",
    "\n",
    "radius = 10\n",
    "\n",
    "area = 3.14 * radius ** 2\n",
    "\n",
    "“The area of a circle with radius 10 is 314 meters square.”"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The area of a circle with radius 10 is 314 meters square\n"
     ]
    }
   ],
   "source": [
    "radius=10 #initializing radius to 10\n",
    "area=3.14*radius**2\n",
    "print(\"The area of a circle with radius {} is {} meters square\".format(radius,int(area)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 9\n",
    "Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)\n",
    "\n",
    "Ex: L1: [150, 155, 145, 148]\n",
    "\n",
    "Output: [68.03, 70.3, 65.77, 67.13]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "Enter weights: 150 155 145 148\n",
      "[68.04, 70.31, 65.77, 67.13]\n"
     ]
    }
   ],
   "source": [
    "n=int(input()) #initializing n with user input\n",
    "wei_g=list(map(int,input(\"Enter weights: \").split()))\n",
    "wei_kg=[]\n",
    "for x in wei_g:\n",
    "    wei_kg.append(round(x*0.453592,2))\n",
    "print(wei_kg)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## QUESTION 10\n",
    "The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature value, labeled f. Note that there are two data points with the same feature value of 6. These are shown as two x’s one above the other. \n",
    "\n",
    "1. Divide this data equally into two parts. Use first part as training and second part as \n",
    "testing. Using KNN classifier, for K=3, what would be the predicted outputs for the test \n",
    "samples? Show how you arrived at your answer. \n",
    "2. Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity \n",
    "values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Given data elements are taken in the tabular form as below,\n",
    "\n",
    "\n",
    "\n",
    "Feature\tLabel\n",
    "1\tO\n",
    "2\tO\n",
    "3\tX\n",
    "6\tX\n",
    "6\tX\n",
    "7\tO\n",
    "10\tO\n",
    "11\tO\n",
    "\n",
    "\n",
    "\n",
    "Here, the first four rows of data are considered to be the Training dataset and the next four rows are selected as the Testing dataset.\n",
    "\n",
    "Now, according to the KNN Classifier we shall now consider K=3 and then the distance between the testing and training data is demonstrated below.\n",
    " \n",
    "\n",
    "\n",
    "\n",
    "In the below table the columns are the training dataset and rows are the testing dataset.\n",
    "\n",
    "\t1(O)\t2(O)\t3(X)\t6(X)\n",
    "6\t5\t4\t3\t0\n",
    "7\t6\t5\t4\t1\n",
    "10\t9\t8\t7\t4\n",
    "11\t10\t9\t8\t5\n",
    "\n",
    "\n",
    "The highlighted rows are the distance values.\n",
    "\n",
    "\n",
    "Let us now assume ‘O’ as negative and ‘X’ as positive values. Now the prediction on testing data is as below:\n",
    "\n",
    "\n",
    "\tTrue label\tPredicted label\tO/P\n",
    "6\tX\tX\tTp\n",
    "7\tO\tX\tFp\n",
    "10\tO\tX\tFp\n",
    "11\tO\tX\tFp\n",
    "\n",
    "\n",
    "Confusion matrix for the above prediction is:\n",
    "\n",
    "TN\tFP\n",
    "FN\tTP\n",
    "\n",
    "The final confusion matrix is :\n",
    "0 3\n",
    "0 1\n",
    "\n",
    "\n",
    "Accuracy of the classifier\t= (TP + TN) / (P + N) = 1 / 4 = 0.25 Sensitivity of the classifier\t= TP / P\t= 1/1\t= 1\n",
    "Specificity of the classifier\t= TN / N\t= 0/3   = 0\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
