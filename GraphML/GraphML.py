from typing import List, Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.graph.Graph import Graph
from GraphML.graph.common import Desc
from GraphML.graph.elements.data.Data import Data
from GraphML.graph.elements.key.Key import Key


class GraphML(GraphMLElement):
    """
    Representa el elemento raíz `<graphml>` en un archivo GraphML.
    """

    def __init__(
            self,
            graphs: List[Graph] = None,
            desc: Desc = None,
    ):
        """
        Inicializa el elemento raíz GraphML.

        Args:
            desc (Optional[Desc]): Descripción opcional para el archivo GraphML.
        """
        super().__init__(desc=desc)
        self.graphs: List[Graph] = graphs or []
        self.keys: List[Key] = []
        self.data_elements: List[Data] = []

    def add_key(self, key: Key) -> "GraphML":
        """Añade un elemento `<key>`."""
        self.keys.append(key)
        return self

    def add_graph(self, graph: Graph) -> "GraphML":
        """Añade un elemento `<graph>`."""
        self.graphs.append(graph)
        # Add all keys from the graph to the list of keys
        self.keys.extend(graph.keys)
        return self

    def add_data(self, data: Data) -> "GraphML":
        """Añade un elemento `<data>`."""
        self.data_elements.append(data)
        return self

    def to_xml(self) -> str:
        """
        Convierte el elemento GraphML a su representación XML.

        Returns:
            str: Representación XML del archivo GraphML.
        """
        desc_xml = self.desc.to_xml() if self.desc else ""
        keys_xml = "".join(key.to_xml() for key in self.keys)
        graphs_xml = "".join(graph.to_xml() for graph in self.graphs)
        data_xml = "".join(data.to_xml() for data in self.data_elements)

        return (
                f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>" +
                f"<graphml>" +
                f"{desc_xml}" +
                f"{keys_xml}" +
                f"{data_xml}" +
                f"{graphs_xml}" +
                f"</graphml>"
        )
