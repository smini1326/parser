import base64
import binascii
import codecs

print('-'*20)
f = open('test_text.bin', 'rb')
lines = f.readlines()
f.close()

# 변수별 byte 선언
year_byte = 3
mon_byte = 1
day_byte = 4 # 범위가 1 ~ 31이라서 문자열 타입으로 저장
str_byte = 6 # 한글 1글자 = 3 byte

pos = 0 # 인덱스 위치

result=""
for line in lines:
    pos = 0

    year = int(line[pos:year_byte], 16)
    pos += year_byte

    year_str = bytearray.fromhex(line[pos:pos+str_byte].decode('utf-8')).decode()
    pos += str_byte

    mon = int(line[pos:pos+mon_byte], 16)
    pos += mon_byte

    mon_str = bytearray.fromhex(line[pos:pos+str_byte].decode('utf-8')).decode()
    pos += str_byte

    day = bytearray.fromhex(line[pos:pos+day_byte].decode('utf-8')).decode()
    pos += day_byte

    day_str = bytearray.fromhex(line[pos:pos+str_byte].decode('utf-8')).decode()
    pos += str_byte

    result += ('{}{}{}{}{}{}'.format( \
        year,
        year_str,
        mon,
        mon_str,
        day,
        day_str
    )
    )
    #print(result)

print(result)

f = open('parsing_data.txt', 'w')
f.write(result)
f.close()


exit()



