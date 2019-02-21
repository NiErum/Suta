sunhwan=766785
running=True
while running:
    guess=int(input("순환이등급을 입력하세요 :"))
    if guess==sunhwan:
        print('\n순환이의 등급을 잘 아는구나!')
        running=False
    elif guess<sunhwan:
        print('\n순환이가 그렇게 높을리가 없어')
    else:
        print('\n그건 니점수고')
