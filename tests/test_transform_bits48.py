#!/usr/bin/env python
##test/ok
from crypto_agama.agama_transform_tools import str_to_hex,bin_to_hex, hex_to_bin, hex_to_bin4, bin8_to_hex


print("x-test3 ---",hex_to_bin("0x3",to_string=True), bin_to_hex(hex_to_bin("0x3")))
print("--test33---",hex_to_bin("33"), bin_to_hex(hex_to_bin("0x33")))
print("--test333--",hex_to_bin("333"), bin_to_hex(hex_to_bin("0x333")))
print("--test333a-",hex_to_bin("333a"))
print()

print("===  hex_to_bin4 bin8_to_hex ===")
print("4-test3 ---",hex_to_bin4("3"), bin8_to_hex(hex_to_bin4("3")))
print("--test33---",hex_to_bin4("33"), bin8_to_hex(hex_to_bin4("33")))
print("--test333--",hex_to_bin4("333"), bin8_to_hex(hex_to_bin4("333")))
print("--test333a-",hex_to_bin4("333a"), bin8_to_hex(hex_to_bin4("333a")))
print()

print("===  bin_to_hex bin8_to_hex ===")
print("4-01 ---", bin_to_hex("01"),bin8_to_hex("01"))
print("--010---", bin_to_hex("010"),bin8_to_hex("010"))
print("--0101--", bin_to_hex("0101"),bin8_to_hex("0101"))
print("--01011-", bin_to_hex("01011"),bin8_to_hex("01011"))
print("--0101..", bin_to_hex("01011011000100"),bin8_to_hex("01011011000100"))
print("- 10 ---", bin_to_hex("10"),bin8_to_hex("10"))
print()

print("===  bin_to_hex bin8_to_hex ===")
print("---test-",bin_to_hex("1"), bin8_to_hex("1"))                     #  0x1  = 0x01
print("---test-",bin_to_hex("11001"), bin8_to_hex("11001"))             #  0x19 = 0x19
print("---test-",bin_to_hex("110011"), bin8_to_hex("110011"))           #  0x33 = 0x33
print("---test-",bin_to_hex("1100110"),bin8_to_hex("1100110"))          #  0x66 = 0x66
print("---test-",bin_to_hex("11001100"),bin8_to_hex("11001100"))        #  0xcc = 0xcc L8
print("---test-",bin_to_hex("110011001"),bin8_to_hex("110011001"))      #  0x199 x 0xcc01 L9 / 110011001 00000001 / L16
print("---test-",bin_to_hex("1100110011"),bin8_to_hex("1100110011"))    #  0x333 x 0xcc03
print("---test-",bin_to_hex("11001100111"),bin8_to_hex("11001100111"))  #  0x667 x 0xcc07
print("---test-",bin_to_hex("11001100111010111111"),bin8_to_hex("11001100111010111111")) # 0xccebf 0xcceb0f
print()

print(str_to_hex("abc"))
#print(string_to_ascii("abc"))
print(str_to_hex("abc háčky a spřežky"))
#print(string_to_ascii("abc háčky a spřežky nejdou"))