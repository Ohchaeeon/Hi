lst_a = ["부산","서울","대구"]
lst_b = [340,970,240]

print(list(zip(lst_a,lst_b))) # lst_a 랑 b 를 각 인덱스에 맞게 맵핑하고 list 형태로 출력
result = dict(zip(lst_a,lst_b))
print(result)