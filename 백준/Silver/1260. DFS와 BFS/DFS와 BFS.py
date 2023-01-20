N, M, V = map(int, input().split())

graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

v1 = [0]*(N+1)
v2 = v1.copy()

def dfs(V):
    v1[V] = 1
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and v1[i] == 0:
            dfs(i)
            

def bfs(V):
    q = [V]
    v2[V] = 1
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if graph[V][i] ==1 and v2[i]==0:
                q.append(i)
                v2[i] = 1

dfs(V)
print()
bfs(V)


