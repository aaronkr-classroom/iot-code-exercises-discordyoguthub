#3_set.py
#두 집합의 정의
set1 = {1, 2, 3, 'a', "Hello"}
set2 = {"Hello", 3, 4, 5, 'b'}

#합집합 (union)
union_set = set1 OR set2

#교잡합 (intersection)
int_set = set1 & set2 # && = and

#차집합 (difference)
diff_set = set1 - set2

#대칭 자칩합 (symmetric_diff) union - intersection
ssym_diff_set = set1 ^ set2 # 합집합과 교집합의 차집합

print('union:',union_set)
print(f"intersection: {int_set}")
print(f"difference: {diff_set}")
print((f"symmertric differenxe: {sym_diff_set}")