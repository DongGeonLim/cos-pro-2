'''문제1
A 학교에서는 단체 티셔츠를 주문하기 위해 학생별로 원하는 티셔츠 사이즈를 조사했습니다. 
선택할 수 있는 티셔츠 사이즈는 작은 순서대로 "XS", "S", "M", "L", "XL", "XXL" 총 6종류가 있습니다.

학생별로 원하는 티셔츠 사이즈를 조사한 결과가 들어있는 리스트 shirt_size가 매개변수로 주어질 때, 
사이즈별로 티셔츠가 몇 벌씩 필요한지 가장 작은 사이즈부터 순서대로 리스트에 담아 return 하도록 solution 함수를 완성해주세요. '''

#You may use import as below.
#import math
'''
def solution(shirt_size):
    #Write code here.
    x = 6
    student_answers = []
    answer = []
    for num in range(x):
	    student_answer = input()
	    student_answers.append(student_answer)
    for i in range(len(student_answers)):
	    size_num = student_answers.count(shirt_size[i])
	    answer.append(size_num)
    
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "M", "L", "XL", "XXL"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

'''
#정답
def solution(shirt_size):
    size_counter = [0 for _ in range(6)]
    for ss in shirt_size:
        if ss == "XS":
            size_counter[0] += 1
        elif ss == "S":
            size_counter[1] += 1
        elif ss == "M":
            size_counter[2] += 1
        elif ss == "L":
            size_counter[3] += 1
        elif ss == "XL":
            size_counter[4] += 1
        elif ss == "XXL":
            size_counter[5] += 1
    return size_counter

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("Solution: return value of the function is ", ret, " .")