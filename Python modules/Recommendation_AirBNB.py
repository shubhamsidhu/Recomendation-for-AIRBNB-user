
import csv, sys, webbrowser, random
#import random
import collections as coll 




#records[random.randint(1,len(records))][3]



def user_listings(records):

	return [record[0] for record in records if user_id == record[3]]

def user_fellows(records,user_listings):

	return {record[3] for record in records if  record[0] in user_listings }

def triangle_count(records,user_fellows):

	return coll.Counter([record[0] for record in records if record[3] in user_fellows])

def recommendation_listings(triangle_count,user_listings,num = 5):

	for listing in user_listings:
		if listing in triangle_count:
			triangle_count.pop(listing)
	return triangle_count.most_common(num)		


if __name__ == '__main__':

	user_id = sys.argv[1]
	#user_id = '44694342'

	csvfile = open('data/reviews.csv',newline='',encoding='utf-8')
	reader = csv.reader(csvfile)
	header = next(reader)
	records = list(reader)
	
	#if not user_id:
	#	user_id = records[random.randint(1,len(records))][3]

	user_listings = user_listings(records)
	user_fellows  = user_fellows(records,user_listings)
	triangle_count= triangle_count(records,user_fellows)
	recommendation_listings = recommendation_listings(triangle_count,user_listings)

	airbnb_url = 'http://airbnb.com/rooms/'

	for listing in recommendation_listings:

		webbrowser.open(airbnb_url+listing[0])
	print(recommendation_listings)















    