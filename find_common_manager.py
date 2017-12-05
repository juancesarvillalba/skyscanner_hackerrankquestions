def OutputFindCommonManager(count):
   input  = """5
   Hilary
   James
   Sarah Fred
   Sarah Paul
   Fred Hilary
   Fred Jenny
   Jenny James
   """

   lines = input.split('\n')
   givenEmployees = lines[1:3]
   relationships = list(reversed(map(lambda rel: rel.split(' '),lines[3:len(lines)-1])))
   employee1 = [selectedEmployees[0]]
   employee2 = [selectedEmployees[1]]
   allUniqueEmployees = set(reduce(lambda a,b:a+b,relationships))
    
   for item in givenEmployees:
      for relate in relationships:
         manager = relate[0]
         employee = relate[1]
         if employee == employee1[len(employee1)-1]:
	          employee1.append(manager)
         if employee == employee2[len(employee2)-1]:
	          employee2.append(manager)
     

  for item in unique_employee:
	    if item in employee1 and item in employee2:
 	       print item
	       break
