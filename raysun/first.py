from io import text_encoding
import regex as re


test_string = "hello! こんにちは!"
utf8_encoded = test_string.encode("utf-8")
print(utf8_encoded)
# b'hello! \xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf!'
print(type(utf8_encoded))
# <class 'bytes'>
# Get the byte values for the encoded string (integers from 0 to 255).
list1 = list(utf8_encoded)
print(list1)
# [104, 101, 108, 108, 111, 33, 32, 227, 129, 147, 227, 130, 147, 227, 129, 171, 227, 129,
# 161, 227, 129, 175, 33]
# One byte does not necessarily correspond to one Unicode character!
print(len(test_string))
# 13
print(len(utf8_encoded))
# 23
print(utf8_encoded.decode("utf-8"))
# hello! こんにちは!



def decode_utf8_bytes_to_str_wrong(bytestring: bytes):
    return "".join([bytes([b]).decode("utf-8") for b in bytestring])

def decode_utf8_bytes_to_str_correct(bytestring: bytes):
    return "".join(bytestring.decode("utf-8"))


text = 'hello'
text = '我'
# res = decode_utf8_bytes_to_str_wrong(text.encode('utf-8'))
res = decode_utf8_bytes_to_str_correct(text.encode('utf-8'))
print("decode_utf8_bytes_to_str_correct is: " + res)


for i in text.encode('utf-8'):
    print(i)
    print(bytes([i]))
print("for end")


# \xC0: 11000000
hexText = b'\xC4\x07'

hexText = b'\xE4\x07'
print(hexText.decode('utf-8'))



PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
res = re.findall(PAT, "some text that i'll pre-tokenize")
print(res)

res = b'test'
print(res)
print(list(res))



print(type(b'hello'))
print(type('hello'))

# print(test_string.encode('utf-8').decode('utf-16'))
