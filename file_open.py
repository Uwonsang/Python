f = open("i_have_a_dream.txt", "r")
contents = f.read()
print(contents)
f.close

with open("i_have_a_dream.txt", "r") as f:
    contents = f.read()
    print(contents)

#문자를 한번에 리스트로 읽기
with open("i_have_a_dream.txt", "r") as f:
    contents = f.readlines()
    print(contents)

#실행 시 마다 한 줄 씩 읽어 오기
with open("i_have_a_dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        if line.strip() == "":
            continue
        print (str(i) + "====" + line.replace("\n",""))
        i = i + 1

with open("i_have_a_dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")	 #빈칸 기준으로 단어를 분리 리스트
    line_list = contents.split("\n")	 #한줄 씩 분리하여 리스트
    # line_list.remove("")

print("Total Number of Characters :", len(contents))
print("Total Number of Words:", len(word_list))
print("Total Number of Lines :", len(line_list))
