def solution(cacheSize, cities):
    cache = []
    answer = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            answer += 1
            cache.pop(cache.index(c))
            cache.append(c)
            if len(cache) > cacheSize:
                cache = cache[1:]
        else:
            answer += 5
            cache[:-1]
            cache.append(c)
            if len(cache) > cacheSize:
                cache = cache[1:]
            
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25