sandwitch = 1500
signer = 10
import time
eat = 0
#   변수들
while True:
    try:
        num = (int(input("-----------------------------\n샌드위치는 1500원이다.\n몇원을 낼까? (숫자만 적어보자)\n▶")))
        print("난",str(num)+"원을 냈다.")
        break
        #   금액 작성 (answer → num으로 패치함)
    except ValueError:
        print("숫자만 적자.")
if int(num) >= 1500:
    signer += 10
    print("-----------------------------\n만드는중...\n-----------------------------")
    time.sleep(2)
    #   금액 확인
if int(num) < 1500:
    print("-----------------------------\n돈이 부족합니다.\n-----------------------------")
    signer -= 5
    #   금액 부족
if signer > 7:
    #   샌드위치 만들기 시작!
    time.sleep(1.5)
    print("■■■■■■■■■■■■■■■■■■■■■■■")
    time.sleep(0.3)
    print("ㅇㅇ-ㅇㅇ-ㅇㅇ-ㅇㅇ-ㅇㅇ")
    time.sleep(0.3)
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(0.3)
    print("-----------------------")
    time.sleep(0.3)
    print("■■■■■■■■■■■■■■■■■■■■■■■")
    #   샌드위치 만들기 끝!
    time.sleep(1.5)
    print("샌드위치가 나왔다.")
    num -= 1500
    while True:
        try:
            eat = (str(input("샌드위치를 먹을까? [y/n]\n▶")))
            break
        except ValueError:
            print("y/n")
yes = "y"
no = "n"
if yes in str(eat):
    print("-----------------------------\n맛있게 먹었다!\n-----------------------------")
    # print(str(num)+"원이 남았다.")
if no in str(eat):
    print("-----------------------------\n샌드위치를 지나가던 친구에게 줬다ㅋㅋ\n-----------------------------")
    # print(str(num)+"원이 남았다.")
    #   성공 메세지 출력
if signer < 7:
    print("샌드위치 시키기 미션 실패!\n다시 주문하시고 싶으시다면 실행버튼을 눌러주세요.")
    #   실패 메세지 출력

#   소감: 완전히 독학으로 만든거지만 제대로 작동해서 래전드인듯 ㅋㅋ (참고로 첫작품임)
#   기타: 코딩학원에서 만든거 아님 독학으로만 만든거임(구글검색및 학교 도서관에 있는 책 1권 참고함)
#   제작자: DH.Ku
#   제작일: 24.09.10.   최근 패치일: 
#   print("Bye")
