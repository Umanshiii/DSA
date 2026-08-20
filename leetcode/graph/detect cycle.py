def dfs(i,parent,adjlist, visited):
    visited[i]=True

    for x in adjlist[i]:
        if x==parent:
            continue
        if visited[x]:
            return True
        if dfs(x, i, adjlist, visited):
            return True
    return False

n=5
adjlist=[[1,3],[0,2],[4],[0],[2]]
visited=[False]*n

