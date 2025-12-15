import networkx as nx
from database.dao import DAO
class Model:
    def __init__(self):
        """Definire le strutture dati utili"""
        self._graph=nx.Graph()


    def build_weighted_graph(self, year: int):
        """
        Costruisce il grafo pesato dei rifugi considerando solo le connessioni con campo `anno` <= year passato
        come argomento.
        Il peso del grafo è dato dal prodotto "distanza * fattore_difficolta"
        """
        self._graph.clear() # pulisce il grafo
        rifugi=DAO.get_all_rifugi() # recupera tutti i rifugi
        for r in rifugi:
            self._graph.add_node(r["id"], **r) # aggiunge i rifugi al grafo

        connessioni=DAO.get_all_connessioni(year) # recupera tutte le connessioni
        for c in connessioni:
            distanza = c["distanza"]
            difficolta = c["difficolta"]

            weight = distanza

            if difficolta == "media":
                weight = distanza * 1.5
            elif difficolta == "difficile":
                weight = distanza * 2.0

            # Aggiungo l'arco con il peso calcolato
            self._graph.add_edge(c["id_rifugio1"], c["id_rifugio2"], weight=weight)
    def get_edges_weight_min_max(self):
        """
        Restituisce min e max peso degli archi nel grafo
        :return: il peso minimo degli archi nel grafo
        :return: il peso massimo degli archi nel grafo
        """
        if not self._graph.edges():
            return 0, 0

        lista_pesi = []


        for u, v, d in self._graph.edges(data=True):

            peso = d['weight']
            lista_pesi.append(peso)

    def count_edges_threshold(self, soglia):
        """
        Conta quanti archi hanno un peso superiore alla soglia e quanti inferiore.
        """
        conta_minori = 0
        conta_maggiori = 0

        # Itero su tutti gli archi del grafo
        for u, v, d in self._grafo.edges(data=True):


            peso = d['weight']

            if peso > soglia:
                conta_maggiori += 1
            else:
                conta_minori += 1

        return conta_minori, conta_maggiori


    """Implementare la parte di ricerca del cammino minimo"""
    def get_min_path(self, source_id, target_id):
        try:
            path=nx.dijkstra_path(self._graph, source=source_id, target=target_id,weight='weight')
            costo = nx.dijkstra_path_length(self._graph, source=source_id, target=target_id, weight='weight')
            return path,costo
        except nx.NetworkXNoPath:
            return None

    def get_num_nodi(self):
        return self._graph.number_of_nodes()

    def get_num_archi(self):
        return self._graph.number_of_edges()