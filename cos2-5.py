'''#문제5
게임 캐릭터가 몬스터와 1:1 전투를 하려 합니다. 몬스터는 처음에 일정 수치의 체력(HP)을 가지고 있습니다. 
캐릭터가 전투에서 이기려면 몬스터를 공격해 몬스터의 체력을 0이하로 만들어야합니다. 
캐릭터는 공격 마법만 사용하며, 공격 마법은 항상 같은 데미지를 입힙니다. 
몬스터는 힐링 마법만을 사용하며, 힐링 마법은 항상 같은 수치로 체력을 회복합니다. 
둘은 항상 번갈아 가며 마법을 사용하고, 처음에는 항상 캐릭터가 먼저 공격을 시작합니다.

캐릭터의 공격력 attack과 몬스터가 자신의 차례에 회복하는 체력 recovery, 
몬스터의 초기 체력 hp가 매개변수로 주어질 때, 몬스터를 잡기 위해서 최소 
몇 번 공격해야 하는지 return 하도록 solution 함수를 작성하려 합니다. 
빈칸을 채워 전체 코드를 완성해주세요.

---
#####매개변수 설명
캐릭터의 공격력 attack과 몬스터가 자신의 차례에 회복하는 체력 recovery, 몬스터의 초기 체력 hp가 solution 함수의 매개변수로 주어집니다.

* attack은 1 이상 100 이하의 자연수입니다.
* recovery는 1 이상 100 이하의 자연수입니다.
* 캐릭터의 공격력은 항상 몬스터의 회복력보다 큽니다(recovery < attack).
* hp는 200 이상 1,000 이하의 자연수입니다.

---
#####return 값 설명
몬스터를 잡기 위해서 최소 몇 번 공격해야 하는지 return 해주세요.

---
#####예시

| attack | recovery | hp  | return |
|--------|----------|-----|--------|
| 30     | 10       | 60 | 3      |

#####예시 설명

몬스터의 체력 변화는 아래와 같습니다.

| 차례 | hp 변화  | 남은 hp |
|-------|----------|---------|
| 캐릭터     | 없음        | 60      |
| 몬스터     | 공격 -30 | 30      |
| 캐릭터     | 회복 +10 | 40      |
| 몬스터     | 공격 -30 | 10      |
| 캐릭터     | 회복 +10 | 20      |
| 몬스터     | 공격 -30 | -10       |

따라서 최소 3번 공격해야 몬스터를 잡을 수 있습니다.
def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += @@@
        hp -= @@@
        if hp <= 0:
            @@@
        hp += @@@
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")'''


def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


'''
정답
def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= attack
        if hp <= 0:
            break
        hp += recovery
    return count

'''