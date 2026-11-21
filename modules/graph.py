from modules.nodes import*

class graph:
    def __init__(self, noeuds=[], aretes=[], colors={}):
        '''
        noeuds : nodes list ; la liste des noeuds du graphe
        aretes : tuple list ; la liste des aretes du graphe
        colors : dic; dictionnaire des couleurs du graphe, clef la couleur, valeur le nombre de couleur
        '''
        self.nodes = noeuds
        self.edges = aretes
        self.colors = colors

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges

    def get_colors(self):
        return self.colors

    def add_node(self, node):
        self.nodes.append(node)

    def add_color(self, color):
        if color in self.colors:
            self.colors[color] += 1

    def add_edges(self, node1, node2):
        '''
        ajoute une arete entre node1 et node2
        '''
        if node1 in self.nodes and node2 in self.nodes:
            self.edges.append((node1, node2))
            node1.add_neighb(node2)
            node2.add_neighb(node1)

    def remove_edges(self, node1, node2):
        '''
        retire une arete entre node1 et node2
        ''' 
        for edge in self.edges:
            if edge == (node1, node2):
                self.edges.remove(edge)
                node1.remove_neighb(node2)
                node2.remove_neighb(node1)
                return

    

    

