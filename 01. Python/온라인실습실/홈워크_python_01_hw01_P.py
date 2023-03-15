score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score['algorithmn'] = 90 # 새로운 성적 추가
score['python'] = 85 # 성적 수정

# 평균 성적 구하기
total_score = score.values()
average_score = sum(total_score) // len(total_score)
print(average_score)