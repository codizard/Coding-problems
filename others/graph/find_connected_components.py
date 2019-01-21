def countComponents(n, edges):
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)
                
        visited = [0] * n
        g = {x:[] for x in xrange(n)}
        # print g
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        # print g
        # return            
        ret = 0
        for i in xrange(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1
                
        return ret
print countComponents(5,[[0,1], [1,2], [3,4]])

