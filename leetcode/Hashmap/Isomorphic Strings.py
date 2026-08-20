def isIsomorphic(self, s: str, t: str) -> bool:
  detail = {}
  used = set()        
  for i in range(len(s)):
    if s[i] not in detail:
      if t[i] in used:
        return False
        detail[s[i]] = t[i]
        used.add(t[i])
    else:
      if detail[s[i]] != t[i]:
        return False
        
  return True
