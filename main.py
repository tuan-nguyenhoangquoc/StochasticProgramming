import networkx as nw
import matplotlib
import matplotlib.pyplot as plt
import random as rand
from networkx.algorithms.flow import edmonds_karp

class MyGraph:
    map_size = 0
    map_width = 0
    map_height = 0
    def __init__(self, map_size, map_width, map_height):
        self.map_size = map_size
        self.map_width = map_width
        self.map_height = map_height
        self.Graph = nw.DiGraph()
        self.Node_position = {}
        self.map = {
            "axes.labelsize": self.map_size, 
            "axes.titlesize": self.map_size,
            "xtick.labelsize": self.map_size,
            "ytick.labelsize": self.map_size,
            "figure.figsize": (self.map_width, self.map_height),
            "axes.titlepad": 10
        }
        plt.rcParams.update(self.map)

    def add_node(self, node, demand=0, color="#add8e6", pos=(0,0)):
        self.Graph.add_node(node, demand=demand, color=color)
        self.Node_position[node] = pos

    def add_edge(self, node1, node2, weight=1, capacity=0):
        self.Graph.add_edge(node1, node2, weight=weight, capacity=capacity)

    def draw_graph(self):
        edge_capacity = nw.get_edge_attributes(self.Graph, "capacity")
        node_colors = list(nw.get_node_attributes(self.Graph, "color").values())
        nw.draw(self.Graph, pos=self.Node_position, with_labels=True, font_color='purple', node_size=2000, node_color=node_colors)
        nw.draw_networkx_edge_labels(self.Graph, pos=self.Node_position, edge_labels=edge_capacity)
        plt.show()

    def max_flow(self):
        Max_flow, flowPath = nw.maximum_flow(self.Graph, 1, 12, flow_func=edmonds_karp)
        print(f"The value of total maximum flow: {Max_flow}")
        for Node in flowPath: 
            print(f"{Node}-->{flowPath[Node]}")

        Max_flow_min_cost = nw.max_flow_min_cost(self.Graph, 1, 12)
        min_cost_value = nw.cost_of_flow(self.Graph, Max_flow_min_cost)
        print(f"The value of min cost value: {min_cost_value}")
        return min_cost_value


def create_scenario(link_weight,link_capacity):
    graph=MyGraph(20,10,4)
    graph.add_node(1, demand=-500, color="#00FF00", pos=(-2, 2))
    graph.add_node(2, pos=(-1, 2))
    graph.add_node(3, pos=(0, 2))
    graph.add_node(4, pos=(1, 2))
    graph.add_node(5, pos=(-2, 1))
    graph.add_node(6, pos=(-1, 1))
    graph.add_node(7, pos=(0, 1))
    graph.add_node(8, pos=(1, 1))
    graph.add_node(9, pos=(-2, 0))
    graph.add_node(10, pos=(-1, 0))
    graph.add_node(11, pos=(0, 0))
    graph.add_node(12, demand=500, color="#00FF00", pos=(1, 0))

    graph.add_edge(1, 2, weight=A_prior_plan_weight[0], capacity=A_prior_plan_capacity[0])
    graph.add_edge(1, 5, weight=A_prior_plan_weight[1], capacity=A_prior_plan_capacity[1])
    graph.add_edge(2, 3, weight=A_prior_plan_weight[2], capacity=A_prior_plan_capacity[2])
    graph.add_edge(2, 6, weight=A_prior_plan_weight[3], capacity=A_prior_plan_capacity[3])
    graph.add_edge(3, 4, weight=A_prior_plan_weight[4], capacity=A_prior_plan_capacity[4])
    graph.add_edge(3, 7, weight=link_weight[5], capacity=link_capacity[5])
    graph.add_edge(4, 8, weight=link_weight[6], capacity=link_capacity[6])
    graph.add_edge(5, 6, weight=link_weight[7], capacity=link_capacity[7])
    graph.add_edge(5, 9, weight=link_weight[8], capacity=link_capacity[8])
    graph.add_edge(6, 7, weight=link_weight[9], capacity=link_capacity[9])
    graph.add_edge(6, 10, weight=link_weight[10], capacity=link_capacity[10])
    graph.add_edge(7, 8, weight=link_weight[11], capacity=link_capacity[11])
    graph.add_edge(7, 11, weight=link_weight[12], capacity=link_capacity[12])
    graph.add_edge(8, 12, weight=link_weight[13], capacity=link_capacity[13])
    graph.add_edge(9, 10, weight=link_weight[14], capacity=link_capacity[14])
    graph.add_edge(10, 11, weight=link_weight[15], capacity=link_capacity[15])
    graph.add_edge(11, 12, weight=link_weight[16], capacity=link_capacity[16])

    # graph.draw_graph()
    min_cost_stg2=graph.max_flow()
    min_cost_scenario.append(min_cost_stg2)

# Usage:

A_prior_plan_weight=[rand.randint(1,5) for i in range (17)]
A_prior_plan_capacity=[rand.randint(1,10)*10 for i in range (17)]

graph = MyGraph(20, 10, 4)
graph.add_node(1, demand=-500, color="#00FF00", pos=(-2, 2))
graph.add_node(2, pos=(-1, 2))
graph.add_node(3, pos=(0, 2))
graph.add_node(4, pos=(1, 2))
graph.add_node(5, pos=(-2, 1))
graph.add_node(6, pos=(-1, 1))
graph.add_node(7, pos=(0, 1))
graph.add_node(8, pos=(1, 1))
graph.add_node(9, pos=(-2, 0))
graph.add_node(10, pos=(-1, 0))
graph.add_node(11, pos=(0, 0))
graph.add_node(12, demand=500, color="#00FF00", pos=(1, 0))


graph.add_edge(1, 2, weight=A_prior_plan_weight[0], capacity=A_prior_plan_capacity[0])
graph.add_edge(1, 5, weight=A_prior_plan_weight[1], capacity=A_prior_plan_capacity[1])
graph.add_edge(2, 3, weight=A_prior_plan_weight[2], capacity=A_prior_plan_capacity[2])
graph.add_edge(2, 6, weight=A_prior_plan_weight[3], capacity=A_prior_plan_capacity[3])
graph.add_edge(3, 4, weight=A_prior_plan_weight[4], capacity=A_prior_plan_capacity[4])
graph.add_edge(3, 7, weight=A_prior_plan_weight[5], capacity=A_prior_plan_capacity[5])
graph.add_edge(4, 8, weight=A_prior_plan_weight[6], capacity=A_prior_plan_capacity[6])
graph.add_edge(5, 6, weight=A_prior_plan_weight[7], capacity=A_prior_plan_capacity[7])
graph.add_edge(5, 9, weight=A_prior_plan_weight[8], capacity=A_prior_plan_capacity[8])
graph.add_edge(6, 7, weight=A_prior_plan_weight[9], capacity=A_prior_plan_capacity[9])
graph.add_edge(6, 10, weight=A_prior_plan_weight[10], capacity=A_prior_plan_capacity[10])
graph.add_edge(7, 8, weight=A_prior_plan_weight[11], capacity=A_prior_plan_capacity[11])
graph.add_edge(7, 11, weight=A_prior_plan_weight[12], capacity=A_prior_plan_capacity[12])
graph.add_edge(8, 12, weight=A_prior_plan_weight[13], capacity=A_prior_plan_capacity[13])
graph.add_edge(9, 10, weight=A_prior_plan_weight[14], capacity=A_prior_plan_capacity[14])
graph.add_edge(10, 11, weight=A_prior_plan_weight[15], capacity=A_prior_plan_capacity[15])
graph.add_edge(11, 12, weight=A_prior_plan_weight[16], capacity=A_prior_plan_capacity[16])

graph.draw_graph()
# graph.max_flow()

min_cost_sub1=graph.max_flow()

probability = [0.2, 0.3, 0.5]
graph1 = MyGraph(20,10,4)
graph2 = MyGraph(20,10,4)
graph3 = MyGraph(20,10,4)



min_cost_scenario=[]

for i in range (3):
    link_weight = [rand.randint(1,5) for i in range (17)]
    link_capacity= [rand.randint(1,10)*10 for i in range (17)]
    print(f"scenario {i+1}: \n")
    create_scenario(link_weight, link_capacity)
    
objective_value=0
for i in range (3):
    objective_value = objective_value + probability[i]*min_cost_scenario[i]

objective_value+=min_cost_sub1
print(f"The objective value is : {objective_value}")