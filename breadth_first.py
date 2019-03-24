#Write your BFS function here
#It takes 3 arguments 
#g is the graph object as defined from the networkx library
#source and target are the two nodes
#The function should return the distance between the source and target nodes as returned by the BFS algorithm

def calculate_distance(g, source, target):

  visited = [False] * (g.number_of_nodes()+1)
  q = []
  q.append((source,0))
  visited[source]=True
    
  while q:
    cur=q.pop(0)
    if (cur[0]==target):return cur[1]
    for i in g.adj[cur[0]]:
      if(visited[i]==False):
        q.append((i,cur[1]+1))
        visited[i]=True
