'''
Message from Space
You have received an encrypted message from space.
Your task is to decrypt the message with the following simple rules:
* Message string will consist of capital letters, numbers, and brackets only.
* When there's a block of code inside the brackets, such as [10AB],
  it means you need to repeat the letters AB for 10 times.
* Message can be embedded in multiple layers of blocks.

Final decrypted message will only consist of capital letters.

Create a function that takes encrypted message str and returns the decrypted message.
'''
from typing import Final
allowed_characters: Final[str]="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]"
#decrypting message from space

def is_standard(message:str):
    for char in message:
        if char not in allowed_characters:
            return False
    return True

def proccess_command(command:str):
    # local variables
    numbers,letters=[],[]
    result=''
    # identify characters
    for char in command:
        if char.isdigit():  # Check if the character is a digit
            numbers += char
        else:
            letters += char
    num=int(''.join(map(str, numbers)))
    string=str(''.join(letters))
    for i in range(num):
        result+=string
    return result

def spaceMessage(message:str):
    if is_standard(message=message):
        # local variables
        command_indexes=[]
        start,end, word=None, None,''
        words=[]
        for i in range(len(message)):
            if message[i]=='[':
                start=i
            if message[i]==']':
                end=i
            if not(start is None or end is None):
                command_indexes.append((start,end))
                start,end=None, None
        for command_index in command_indexes:
            for ci in range(command_index[0]+1,command_index[1]):
                word+=message[ci]
            words.append(word)
            word=''
        for word in words:
            message=message.replace('['+word+']',proccess_command(word))
        print(message)
    else:
        print('Your message is not standard! please write your message based on the protocol.')

# Test examples
spaceMessage("ABCD")              # Output: ABCD
spaceMessage("AB[3CD]")           # Output: ABCDCDCD
spaceMessage("IF[2E]LG[5O]D")     # Output: IFEELGOOOOOD
spaceMessage("[3BG]USBB[2DA]")    # Output: BGBGBGUSBBDADA
spaceMessage("[3BG]USBB[2Da]")    # Output: Your message is not standard!