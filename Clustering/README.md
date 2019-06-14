### The Girvan-Newman Method: Successively Deleting Edges of High Betweenness.
Edges of high betweenness are the ones that, over all pairs of nodes, carry the highest volume
of traffic along shortest paths. Based on the premise that these are the most “vital” edges
for connecting different regions of the network, it is natural to try removing these first. This
is the crux of the Girvan-Newman method, which can now be summarized as follows.

+ (1) Find the edge of highest betweenness — or multiple edges of highest betweenness, if
there is a tie — and remove these edges from the graph. This may cause the graph
to separate into multiple components. If so, this is the first level of regions in the
partitioning of the graph.

+ (2) Now recalculate all betweennesses, and again remove the edge or edges of highest betweenness. This may break some of the existing components into smaller components;
if so, these are regions nested within the larger regions.

+ (...) Proceed in this way as long as edges remain in graph, in each step recalculating all
betweennesses and removing the edge or edges of highest betweenness.
