import networkx as nx

link=[["PlayerA", "PlayerB"],["PlayerA","PlayerD"],["PlayerA","PlayerE"],
      ["PlayerB", "PlayerC"],
      ["PlayerC", "PlayerD"],["PlayerC", "PlayerF"],
      ["PlayerE", "PlayerB"],["PlayerE", "PlayerF"],
      ["PlayerF", "PlayerE"],
      ]


g = nx.DiGraph()
for x in link:
    g.add_edge(x[0],x[1])

answer=nx.pagerank_scipy(g,alpha=0.5)
print(answer)

answer=sorted(answer.items(),key=lambda item:item[1],reverse = True)
print("\nThe rank of players:")
for x in answer:
    print(x)

