from enum import Enum
from typing import Optional

from GraphML.GraphMLElement import GraphMLElement
from GraphML.common.Desc import Desc
from GraphML.common.ID import ID, IDType


class ForType(Enum):
    GRAPH = "graph"
    NODE = "node"
    EDGE = "edge"
    HYPEREDGE = "hyperedge"
    PORT = "port"
    ENDPOINT = "endpoint"
    ALL = "all"


class Key(GraphMLElement):
    """
    Representa un elemento `<key>` en GraphML.
    """

    def __init__(
            self,
            key_id: ID = ID.autogenerate(IDType.KEY),
            for_type: ForType = ForType.ALL,
            desc: Optional[Desc] = None,
            default_value: Optional[str] = None,
            extra_attrib: Optional[dict] = None,
    ):
        """
        Inicializa un elemento de clave.

        Args:
            key_id (ID): Identificador único para la clave.
            for_type (str): Dominio de definición de la clave (por defecto, "all").
            desc (Optional[Desc]): Descripción opcional de la clave.
            default_value (Optional[str]): Valor por defecto para esta clave.
            extra_attrib (Optional[dict]): Atributos personalizados adicionales.
        """
        super().__init__(desc, extra_attrib)
        self.key_id = key_id
        self.for_type = for_type
        self.default_value = default_value

    def to_xml(self) -> str:
        """
        Convierte la clave a su representación XML.

        Returns:
            str: Representación XML de la clave.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        default_xml = f"<default>{self.default_value}</default>" if self.default_value else ""

        extra_attributes = self.render_attributes()
        attributes = f'id="{self.key_id}" for="{self.for_type}"'
        attributes += f" {extra_attributes}" if extra_attributes else ""

        return (
                f"<key {attributes}>" +
                f"{desc_xml}" +
                f"{default_xml}" +
                f"</key>"
        )

    def __str__(self):
        return f"{self.key_id}"
