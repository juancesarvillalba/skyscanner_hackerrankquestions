import sys
//  using python 2.7
// Most holiday destination

def OutputMostPopularDestination(count):

	holidsy_dest = dict()

	while count > 0:
		inputData = raw_input()
    if holiday_dest.has_key(inputData):
		   holiday_dest[inputData] = holiday_dest[inputData] + 1
    else:
       holiday_dest[inputData] = 1
    count = count -1

  print ("Most Popular Destination: ", sorted(holiday_dest.iteritems(),lambda (key,value): (value,key),reverse = True)[0][0])
  
