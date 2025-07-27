'''
Remove the Computer Virus
Your computer might have been infected by a virus!
Create a function that finds the viruses in files and removes them from your computer.

Examples
removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
output = "PC Files: spotifysetup.exe, dog.jpg"

removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
output = "PC Files: antivirus.exe, cat.pdf"

removeVirus("PC Files: notvirus.exe, funnycat.gif")
output = "PC Files: notvirus.exe, funnycat.gif")

Notes
Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
Return "PC Files: Empty" if there are no files left on the computer.

'''
def removeVirus(s:str) -> str:
    if not s:
        return "PC Files: Empty"
    s=s.strip().split("PC Files: ")[1].split(", ")
    filtered_files = []
    for i,file in enumerate(s):
        lower_file = file.lower()
        if ("virus" in lower_file or "malware" in lower_file):
            if "antivirus" in lower_file or "notvirus" in lower_file:
                filtered_files.append(file)
        else: 
            filtered_files.append(file)
    # print(s)
    if not filtered_files:
        return "PC Files: Empty"
    
    return "PC Files: "+ ", ".join(filtered_files)

print(removeVirus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")) #OK    output:PC Files: spotifysetup.exe, dog.jpg
print(removeVirus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")) #OK output: PC Files: antivirus.exe, cat.pdf
print(removeVirus("PC Files: notvirus.exe, funnycat.gif")) #OK  output:PC Files: notvirus.exe, funnycat.gif
print(removeVirus("")) #OK output:PC Files: Empty
