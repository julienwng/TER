class node:
    def __init__(self, label="", color="", neighb=None):
        '''
        label: string; nom du noeud/sommet
        color: string; couleur du noeud/sommet
        neighb: node set; voisins du noeud
        '''
        self.label = label
        self.color = color
        self.neighb = set() if neighb is None else set(neighb)

    def get_label(self):
        return self.label

    def get_color(self):
        return self.color

    def get_neighb(self):
        return self.neighb
    
    def get_degree(self):
        return len(self.neighb)
    
    def change_label(self, label):
        self.label = label

    def change_color(self, color):
        self.color = color

    def add_neighb(self, neighb):
        self.neighb.add(neighb)

    def remove_neighb(self, neighb):
        self.neighb.remove(neighb)
