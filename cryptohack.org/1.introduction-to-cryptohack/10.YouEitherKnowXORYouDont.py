'''
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!
'''
encrypted_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted_msg = bytes.fromhex(encrypted_msg)

flag_format = b"crypto{"
key = [o1 ^ o2
       for (o1, o2) in zip(encrypted_msg, flag_format)] + [ord("y")]

flag = []
key_len = len(key)
for i in range(len(encrypted_msg)):
    flag.append(
        encrypted_msg[i] ^ key[i % key_len]
    )
flag = "".join(chr(o) for o in flag)

print("Flag:")
print(flag) #crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}