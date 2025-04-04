def is_standard(message):
    # Ensure only allowed characters are present
    allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]"
    for char in message:
        if char not in allowed_characters:
            return False
    return True

def expand_block(block):
    # Expand blocks of the form [number+letters]
    number = ""
    letters = ""
    for char in block:
        if char.isdigit():
            number += char
        else:
            letters += char
    return int(number) * letters  # Repeat letters by the number

def spaceMessage(message):
    if not is_standard(message):
        return "Your message is not standard! Please write your message based on the protocol."

    while '[' in message:
        # Process innermost block first
        end = message.index(']')
        start = message.rindex('[', 0, end)
        block = message[start+1:end]
        # Replace the block with its expanded form
        message = message[:start] + expand_block(block) + message[end+1:]

    return message

# Test examples
print(spaceMessage("ABCD"))              # Output: ABCD
print(spaceMessage("AB[3CD]"))           # Output: ABCDCDCD
print(spaceMessage("IF[2E]LG[5O]D"))     # Output: IFEELGOOOOOD
print(spaceMessage("[3BG]USBB[2DA]"))    # Output: BGBGBGUSBBDADA
print(spaceMessage("[3BG]USBB[2Da]"))    # Output: Your message is not standard!
