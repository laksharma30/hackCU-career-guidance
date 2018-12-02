import requests
from pprint import pprint
import json
import pymongo

def getPageUserIds(pageNum):
	headers  = { 'Host': 'boulder.joinhandshake.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://boulder.joinhandshake.com/',
	'X-CSRF-Token': '1eDrww48iSPv8B8xK0HxnF+anJJ8DU2TOa/Uwv8kpO9kiPVofgfm4TtC0IlW9PPrj5Y81L92K9W0ByOJ5suC1g==',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Cookie': '_trajectory_session=V2p3U1NUUDJhZUJHYzgyM0RnT1NEcVhINUQzL0sxYmROcE1FektoM2M0Ujkrdm0rL2ZrOVU1SkNiRytzVm1KUytyTHdyZHlNRUZGbnVBZEZhL0toSnB2emlteGNFT1M3VlJ5OFZaaFg0QkFtOXdlMHIvREl4SWszQkxrdmQwaExrbVhpVnBFWEZtbnV3bSt4QzdRMGt0MzExZHk1MDFiNGsyeUQ1UmNLZWZJV3c3WlFxTzBjRURValFvcW1DYjJEd2VpYTIrU2dQR0RwemlaWmo2ZFJidz09LS00cXZ0anQzQlBhcWdCT09Ic3pGcXNnPT0%3D--d5d2544cf2addc41e8a5fc88d724b9b435934320; production_js_on=true; ajs_user_id=14870268; ajs_group_id=null; ajs_anonymous_id=%2227b1d5c1-dc71-4e41-95ed-c562cb7ede62%22; _ga=GA1.2.38471574.1543695146; _gid=GA1.2.622189068.1543695146; production_submitted_email_address=BAhJIiBsYWtzaHlhLnNoYXJtYUBjb2xvcmFkby5lZHUGOgZFVA%3D%3D--57f6ec064c635b7c076208534a679a6894874ee8; _gat=1; production_auth_token=UW10Z2M4cDJ6cDlsajJkMytYRksxRlFuM0FUZzNybWVyQlZrUEVsa1pNV1FuQmVZN3VRRjRVVFhEQ1UydWNWazJYekFLN1JsbS9KSnAvR0ZleWFOUzdQZFl2S3ExN3h6QXRxbzhZL0EwSFk9LS0yb0tOWmpvbG43ejE2U0x5WVdPamdnPT0%3D--2ffdfbc26c96be629ccc771d0f6348a07c95d017',
	'TE': 'Trailers'}

	r = requests.get('https://boulder.joinhandshake.com/students?page=' + str(pageNum), headers=headers)
	results = json.loads(r.text)
	ids = []

	for result in results['results']:
		ids.append(result['id'])

	return ids

def mongoStuff(all_ids):

	hackCU_client = pymongo.MongoClient('mongodb://localhost:27017/')
	hackCU_DB = hackCU_client['hackCU_DB']
	ids_col = hackCU_DB['ids']
	all_id = ids_col.find()
	my_ids = []
	for i in all_id:
		my_ids.append(i['id'])

	print(len(my_ids))
	print(type(my_ids[0]))
	return my_ids
	# print(all_id)

	# for ID in all_ids:

	# 	ids_col.insert_one({'id':ID})
	# print(hackCU_client.list_database_names())

def mongoStuffWriteStudentInfo(resDict):
	hackCU_client = pymongo.MongoClient('mongodb://localhost:27017/')
	hackCU_DB = hackCU_client['hackCU_DB']
	user_coll = hackCU_DB['users']

	user_coll.insert_one(resDict)

def mongoStuffWriteRelevantData(resDict):
	hackCU_client = pymongo.MongoClient('mongodb://localhost:27017/')
	hackCU_DB = hackCU_client['hackCU_DB']
	useful_coll = hackCU_DB['useful']

	useful_coll.insert_one(resDict)


def getStudentInfo(my_ids):
	headers  = { 'Host': 'boulder.joinhandshake.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://boulder.joinhandshake.com/',
	'X-CSRF-Token': '1eDrww48iSPv8B8xK0HxnF+anJJ8DU2TOa/Uwv8kpO9kiPVofgfm4TtC0IlW9PPrj5Y81L92K9W0ByOJ5suC1g==',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Cookie': '_trajectory_session=V2p3U1NUUDJhZUJHYzgyM0RnT1NEcVhINUQzL0sxYmROcE1FektoM2M0Ujkrdm0rL2ZrOVU1SkNiRytzVm1KUytyTHdyZHlNRUZGbnVBZEZhL0toSnB2emlteGNFT1M3VlJ5OFZaaFg0QkFtOXdlMHIvREl4SWszQkxrdmQwaExrbVhpVnBFWEZtbnV3bSt4QzdRMGt0MzExZHk1MDFiNGsyeUQ1UmNLZWZJV3c3WlFxTzBjRURValFvcW1DYjJEd2VpYTIrU2dQR0RwemlaWmo2ZFJidz09LS00cXZ0anQzQlBhcWdCT09Ic3pGcXNnPT0%3D--d5d2544cf2addc41e8a5fc88d724b9b435934320; production_js_on=true; ajs_user_id=14870268; ajs_group_id=null; ajs_anonymous_id=%2227b1d5c1-dc71-4e41-95ed-c562cb7ede62%22; _ga=GA1.2.38471574.1543695146; _gid=GA1.2.622189068.1543695146; production_submitted_email_address=BAhJIiBsYWtzaHlhLnNoYXJtYUBjb2xvcmFkby5lZHUGOgZFVA%3D%3D--57f6ec064c635b7c076208534a679a6894874ee8; _gat=1; production_auth_token=UW10Z2M4cDJ6cDlsajJkMytYRksxRlFuM0FUZzNybWVyQlZrUEVsa1pNV1FuQmVZN3VRRjRVVFhEQ1UydWNWazJYekFLN1JsbS9KSnAvR0ZleWFOUzdQZFl2S3ExN3h6QXRxbzhZL0EwSFk9LS0yb0tOWmpvbG43ejE2U0x5WVdPamdnPT0%3D--2ffdfbc26c96be629ccc771d0f6348a07c95d017',
	'TE': 'Trailers'}


	uri = 'https://boulder.joinhandshake.com/users/'#4779039/work_experiences'
	for ID in range(1594,len(my_ids)): 
	#+ '/courses'
		ID = my_ids[ID]
		resDict = {'id' : ID}
		try:
			r = requests.get(uri + str(ID) + '/work_experiences', headers=headers)
			if r.text is not None:
				tempDict = json.loads(r.text)
				resDict['work_experiences'] = tempDict

			r = requests.get(uri + str(ID) + '/courses', headers=headers)
			if r.text is not None:
				tempDict = json.loads(r.text)
				resDict['courses'] = tempDict
			r = requests.get(uri + str(ID) + '/skills', headers=headers)
			if r.text is not None:
				tempDict = json.loads(r.text)

				resDict['skills'] = tempDict
		except:
			pass
		# resDict = resDict['user']
		# mongoStuffWriteStudentInfo(resDict)
		mongoStuffWriteRelevantData(resDict)






def main():



	# for pageNum in range(total_pages):
	# 	all_ids.append(getPageUserIds(pageNum))


	# all_ids = [j for i in all_ids for j in i]



	# print(len(all_ids))
	all_ids = []
	my_ids = mongoStuff(all_ids)
	getStudentInfo(my_ids)



if __name__ == '__main__':
	main()



