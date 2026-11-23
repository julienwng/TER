from modules.graph import *
from random import random, randint

class modele:
    def __init__(self):
        node1 = node("B1", "blue")
        node2 = node("R1", "red")
        self.graph = graph([node1, node2], colors={"blue":1, "red":1})
        self.graph.add_edges(node1, node2)

    def get_graph(self):
        return self.graph

    def attachement_pref(self, n,  r, rho):
        '''
        n : int ; nombre de noeuds dans le modele
        r ; float : probabilité qu'un nouveau noeud soit rouge
        rho ; float : probabilité d'avoir une arete entre deux noeuds de couleurs differentes
        '''
        if r > 1/2 or r < 0:
            raise ValueError("r doit etre entre 0 et 1/2")
        if rho < 0 or rho > 1:
            raise ValueError("rho doit etre entre 0 et 1")

        liste = self.graph.get_nodes().copy() #liste pour choisir les noeuds proportionnellement avec leur nombre de connexions
        cpt = len(liste)

        while cpt < n:
            #On choisit la couleur du nouveau noeud
            if random() < r :
                new_node = node(f"R{self.graph.get_colors()["red"] + 1}", "red")
            else:
                new_node = node(f"B{self.graph.get_colors()["blue"] + 1}", "blue")
            new_node_color = new_node.get_color()

            # Homophilie, tant qu'on relie pas deux noeuds on continue a en choisir un nouveau aléatoirement selon son nb d'aretes
            while True:
                node_chosen = liste[randint(0, len(liste)-1)]
                if (node_chosen.get_color() == new_node_color) or random() < rho:
                    self.graph.add_node(new_node)
                    self.graph.add_edges(node_chosen, new_node)
                    liste.append(new_node)
                    liste.append(node_chosen)
                    self.graph.add_color(new_node_color)
                    cpt += 1
                    break
    