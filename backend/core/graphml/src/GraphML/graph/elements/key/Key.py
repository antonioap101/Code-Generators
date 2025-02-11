from enum import Enum
from typing import Optional

from backend.core.graphml.src.GraphML.GraphMLElement import GraphMLElement
from backend.core.graphml.src.GraphML.graph.common.Desc import Desc
from backend.core.graphml.src.GraphML.graph.common.ID import ID, IDType


class ForType(Enum):
    GRAPH = "graph"
    NODE = "node"
    EDGE = "edge"
    HYPEREDGE = "hyperedge"
    PORT = "port"
    ENDPOINT = "endpoint"
    ALL = "all"


class AttributeType(Enum):
    BOOLEAN = "boolean"
    INT = "int"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"
    STRING = "string"


class Key(GraphMLElement):
    """
    Representa un elemento `<key>` en GraphML.
    """

    def __init__(
            self,
            key_id: ID = None,
            for_type: ForType = ForType.ALL,
            attribute_name: Optional[str] = None,
            attribute_type: AttributeType = AttributeType.STRING,
            desc: Desc = None,
            default_value: Optional[str] = None,
    ):
        """
        Inicializa un elemento de clave.

        Args:
            key_id (ID): Identificador único para la clave.
            for_type (str): Dominio de definición de la clave (por defecto, "all").
            attribute_name (Optional[str]): Nombre del atributo.
            attribute_type (AttributeType): Tipo de atributo.
            desc (Optional[Desc]): Descripción opcional de la clave.
            default_value (Optional[str]): Valor por defecto para esta clave.
        """
        super().__init__(desc)
        self.key_id = key_id if key_id else ID.autogenerate(IDType.KEY)
        self.for_type = for_type
        self.attribute_name = attribute_name or self.key_id
        self.attribute_type = attribute_type
        self.default_value = default_value

    def __hash__(self):
        """Define el hash basado en el identificador único del `Key`."""
        return hash(self.key_id)

    def __eq__(self, other):
        """
        Compara si dos `Key` son iguales basado en sus identificadores únicos.

        Args:
            other (Key): Otro objeto `Key` para comparar.

        Returns:
            bool: True si los identificadores son iguales, False en caso contrario.
        """
        if not isinstance(other, Key):
            return False
        return self.key_id == other.key_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.key_id}"

    @staticmethod
    def for_graph(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                  default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.GRAPH, attribute_name=attribute_name, attribute_type=attribute_type,
                   desc=desc, default_value=default_value)

    @staticmethod
    def for_node(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                 default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.NODE, attribute_name=attribute_name, attribute_type=attribute_type,
                   desc=desc, default_value=default_value)

    @staticmethod
    def for_edge(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                 default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.EDGE, attribute_name=attribute_name, attribute_type=attribute_type,
                   desc=desc, default_value=default_value)

    @staticmethod
    def for_hyperedge(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING,
                      desc: Desc = None, default_value: Optional[str] = None):
        return Key(
            key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.HYPEREDGE, attribute_name=attribute_name, attribute_type=attribute_type,
            desc=desc, default_value=default_value)

    @staticmethod
    def for_port(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                 default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.PORT, attribute_name=attribute_name, attribute_type=attribute_type,
                   desc=desc, default_value=default_value)

    @staticmethod
    def for_endpoint(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                     default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.ENDPOINT, attribute_name=attribute_name,
                   attribute_type=attribute_type, desc=desc, default_value=default_value)

    @staticmethod
    def for_all(key_id: ID = None, attribute_name: Optional[str] = None, attribute_type: AttributeType = AttributeType.STRING, desc: Desc = None,
                default_value: Optional[str] = None):
        return Key(key_id=key_id or ID.autogenerate(IDType.KEY), for_type=ForType.ALL, attribute_name=attribute_name, attribute_type=attribute_type,
                   desc=desc, default_value=default_value)

    def to_xml(self) -> str:
        """
        Convierte la clave a su representación XML.

        Returns:
            str: Representación XML de la clave.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        default_xml = f"<default>{self.default_value}</default>" if self.default_value else ""

        attributes = f'id="{self.key_id}" for="{self.for_type.value}" attr.name="{self.attribute_name}" attr.type="{self.attribute_type.value}"'

        return (
                f"<key {attributes}" + (">" if desc_xml or default_xml else "") +
                f"{desc_xml}" +
                f"{default_xml}" +
                (f"</key>" if desc_xml or default_xml else "/>")
        )
