from gedcom.element.element import Element
from gedcom.element.family import FamilyElement
import gedcom.tags


def test_initialization():
    family_element = FamilyElement(level=-1, pointer="", tag=gedcom.tags.GEDCOM_TAG_FAMILY, value="")
    assert isinstance(family_element, Element)
    assert isinstance(family_element, FamilyElement)
