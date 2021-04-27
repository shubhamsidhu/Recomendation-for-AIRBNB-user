import csv, webbrowser
from operator import itemgetter




def top_10 (records,ind,num = 5):

	listings = [(record[0],float(record[ind].strip('$').replace(',',''))) for record in records if record[ind] != '']
	return sorted(listings,key= itemgetter(1),reverse=True)[:num]



if __name__ == '__main__':
	num = 5
	try:
		user_input  = int(input('enter 1 : by_review , 2 : by_review_count , 3 : by_price  :'))
		num = int(input('enter num of listing  :'))
		
	except:
		print('enter appropriate numbers')

	

	if user_input == 1:
		ind = 60
	elif user_input == 2:
		ind = 55
	elif user_input == 3:
		ind = 39
	else:
		ind = 60

	with open('data/listings.csv','r',newline='',encoding='utf-8') as reviews:
		reader = csv.reader(reviews)
		header = next(reader)
		records = list(reader)

	airbnb_url = 'http://airbnb.com/rooms/'


	top_listings = top_10(records,ind,num)

	for listing in top_listings :
		webbrowser.open("http://airbnb.com/rooms/"+listing[0])

	print(top_listings)




