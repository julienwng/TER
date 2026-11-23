from modules.modele import modele
import graphviz
from math import sqrt

def afficher(g, fichier="graphe", moteur="sfdp"):
        '''
        g : graph ; le graphe à afficher
        fichier : str ; nom du fichier de sortie (sans extension)
        moteur : str ; algorithme de placement ("sfdp", "neato", "fdp")
        '''
        dot = graphviz.Graph(engine=moteur, format="png")
        dot.attr(overlap="false", outputorder="edgesfirst")
        dot.attr("node", shape="circle", label="", style="filled", fixedsize="true")
        dot.attr("edge", color="gray70")

        for v in g.get_nodes():
            taille = 0.05 + 0.05 * sqrt(v.get_degree())
            c = v.get_color()
            dot.node(v.get_label(), width=str(taille), height=str(taille),
                    fillcolor=c, color=c)

        for a, b in g.get_edges():
            dot.edge(a.get_label(), b.get_label())

        dot.render(fichier, view=True, cleanup=True)

new_modele = modele()
new_modele.attachement_pref(300, 0.5, 0)
afficher(new_modele.graph)
