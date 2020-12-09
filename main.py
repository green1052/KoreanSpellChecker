from spell import spell_check

for text in spell_check(input("입력: ")):
    print(f"틀린 단어: {text['orgStr']}\n대치어: {text['candWord']}\n이유: {text['help']}\n\n")
