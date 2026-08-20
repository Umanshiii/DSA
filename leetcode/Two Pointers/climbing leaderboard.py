def climbingLeaderboard(ranked, player):
    dic = []
    for i in ranked:
        if not dic or i != dic[-1]:
            dic.append(i)
    
    ans = []
    for i in player:
        left, right = 0, len(dic) - 1
        while left <= right:
            mid = (left + right) // 2
            if dic[mid] == i:
                ans.append(mid + 1)
                break
            elif dic[mid] < i:
                right = mid - 1
            else:
                left = mid + 1
        else:
            ans.append(left + 1)
    
    return ans


ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, player))