import datetime as DT
import struct
from binascii import unhexlify
import sys

def timestamp_parser(hex8byte):

	#one = '88339dcb3836d001' # 89280173047869
	#one = '80DA153650B5D401'
	# print("파싱한 16진수 값 =====>>> ",hex8byte)
	if isinstance(hex8byte,str):
		hex8byte = unhexlify(hex8byte)
		print("바이너리화 =====>>> ",hex8byte)

	nt_timestamp = struct.unpack("<Q", (hex8byte))[0] # < 는 리틀 엔디안 Q 의 경우 unsigned long long 타입이라는 뜻 
	# print(" < 는 리틀앤디안 방식을, Q는 unsigned long long을 의미합니다]\n")
	# print("결과 값 =====>>> ", nt_timestamp)

	# print("연도로 나눠보기 =====>>> " ,nt_timestamp/(60*60*24)/10000000)
	epoch = DT.datetime(1601,1,1,0,0,0)
	# print("일 수와 나머지 =====>>> " ,DT.timedelta(microseconds=nt_timestamp/10)) 
	nt_datetime = epoch + DT.timedelta(microseconds=nt_timestamp/10) 
	print("파싱한 값의 날짜는 =====>>> UTC+0 기준으로 " ,nt_datetime)
	print("파싱한 값의 날짜는 =====>>> UTC+9 기준으로 " ,nt_datetime+DT.timedelta(hours=9))

def parsing_file(path):

	try:
		with open(path,'rb') as f:			

			MZ = f.read(1)
			if MZ == b'L':
				print('lnk file')

			f.seek(28) # createion
			print("=====-Creation Time-=====")
			timestamp_parser(f.read(8))
			f.seek(36)
			print("=====-Access Time-=====")
			timestamp_parser(f.read(8))
			f.seek(44)
			print("=====-Write Time-=====")
			timestamp_parser(f.read(8))

	except FileNotFoundError as e:
		print("cannot found lnk file")
		sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv)!=2:
		print('argv length must 2 length\nplease input lnk path')
		sys.exit(1)
	parsing_file(sys.argv[1])
	