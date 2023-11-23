# Scheduling Problem Reduction 
**Implementing a reduction of The Scheduling Problem as a Graph Coloring Problem**

Below shows a representation of courses adjancences
![alt text](https://github.com/TokamLilian/sch-problem-reduc/blob/101eb34a6b66289c557c25e162147e6a92e5344c/miscellaneous/Graph_Template_01.png)

## Table of Contents
-  [Installation](#installation)
-  [Setup](#setup)
-  [The Scheduling Problem](#the-scheduling-problem)
-  [Graph Colorings and the Scheduling Problem](#graph-colorings-and-the-scheduling-problem)
-  [Reduction from the Scheduling Problem to Graph Coloring](#reduction-from-the-scheduling-problem-to-graph-coloring)
-  [Solution Approach for Reducing the Scheduling Problem to Graph Coloring](#solution-approach-for-reducing-the-scheduling-problem-to-graph-coloring)
-  [Conclusion](#conclusion)

## Installation

Make sure to have `python 3.7` or later installed on computer
**Clone the repository**
```bash
git clone https://github.com/TokamLilian/sch-problem-reduc
pip install flask
cd sch-problem-reduc/src
```

---

## Setup
Start the server in the correct directory `sch-problem-reduc/src`
```bash
py app.py
```

The client side is automatically launched `index.html` in a new browser tab

---

## The scheduling problem
The scheduling problem involves allocating resources or tasks to specific time slots while satisfying constraints.
The goal is to minimize completion time, resource utilization, or other relevant criteria. 
The complexity of scheduling problems varies, with some being [NP-hard](https://en.wikipedia.org/wiki/NP-hardness), necessitating the use of approximation algorithms and heuristics in practical applications.

---

## Graph colorings and the scheduling problem
Graph colorings and the scheduling problem are related computational challenges.
[Graph coloring](https://en.wikipedia.org/wiki/Graph_coloring) involves assigning colors to vertices in a graph such that no adjacent vertices share the same color.
This concept is applied in scheduling problems where tasks or events are assigned time slots or resources, ensuring that conflicting elements are scheduled independently.
In the context of the scheduling problem, the graph coloring problem can be seen as a way to reduce the problem to a graph coloring problem.

Below shows a coloring of the graph of courses
![alt text](https://github.com/TokamLilian/sch-problem-reduc/blob/c034f457625d22c618b884deb75711c5e6da6ee9/miscellaneous/Colored_graph_001.png)

---

## Reduction from the Scheduling Problem to Graph Coloring 
Reduction from the scheduling problem to graph coloring involves representing tasks as vertices in a graph and creating edges between conflicting tasks.
The scheduling constraints are translated into graph properties as follows:
- Each course is represented by a node in the graph.
- Each course has a set of dependencies, represented by edges between nodes.

By applying graph coloring algorithms to the constructed graph, an optimal schedule can be derived, with each color representing a distinct time slot or resource allocation for tasks.
This reduction demonstrates the interconnected nature of these computational problems.

---

## Solution Approach for Reducing the Scheduling Problem to Graph Coloring
Hence, To reduce the scheduling problem to graph coloring, Apply [graph coloring algorithms](https://en.wikipedia.org/wiki/Graph_coloring#:~:text=the%20branch%2Dwidth.-,Exact%20algorithms,-%5Bedit%5D) to find a feasible schedule, with each color indicating a distinct time slot or resource allocation.
This approach leverages graph theory to address scheduling optimization.

---

## Conclusion
In conclusion, the reduction of the scheduling problem to graph coloring provides a valuable computational framework. By transforming scheduling constraints into graph properties and applying graph coloring algorithms,
an efficient solution for resource allocation and time optimization can be achieved.
This approach highlights the practical utility of graph theory in addressing real-world scheduling challenges.