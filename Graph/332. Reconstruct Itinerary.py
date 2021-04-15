from collections import defaultdict

def findItinerary(tickets):
        result = []
        travel = defaultdict(list)

        for node in sorted(tickets, reverse=True):
            travel[node[0]].append(node[1])
        
        def dfs(node):
            while travel[node]:
                dfs(travel[node].pop())
            result.append(node)

        dfs("JFK")
        return result[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))