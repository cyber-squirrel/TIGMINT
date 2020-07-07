## Code for Instagram osint


from bs4 import BeautifulSoup as insta
import requests 
import json
from json import loads 

def Username(user):
	url = f"https://www.instagram.com/{user}"  #Instagram URL
	res = requests.get(url)
	soup = insta(res.text, 'html.parser')
	jscript=soup.find_all('script')     #finding all the scripts which is used in instagram page
	required_script = jscript[4]        #Using Script number 4
	data = required_script.contents[0]
	D_object = data[data.find('{"config"') : -1]
	json_data = loads(D_object)
	json_data = json_data['entry_data']['ProfilePage'][0]['graphql']['user']
	output = {
	    'full_name': json_data['full_name'],
	    'username': json_data['username'],
            'biography': json_data['biography'],
	    'followers_count': json_data['edge_followed_by'],
            'following_count': json_data['edge_follow'],
            'Private_Account': json_data['is_private'],
	    'Business_Account' : json_data['is_business_account'],
	    'Business_category' :json_data['business_category_name'],
	    'Verified_Account' : json_data['is_verified'],
	    'Connected_Fb_Page': json_data['connected_fb_page'],
            'total_posts': json_data['edge_owner_to_timeline_media']['count'],
            'profile_pic_url' : json_data['profile_pic_url_hd'],
            'external_url': json_data['external_url']
        }
	print(output)
	with open('insta.json', 'w') as json_file:
		json.dump(output, json_file)
	
user = input("Enter Username : ")
Username(user)
