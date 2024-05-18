from gedcom.element.element import Element
from gedcom.element.object import ObjectElement
import gedcom.tags


def test_initialization():
    object_element = ObjectElement(level=-1, pointer="", tag=gedcom.tags.GEDCOM_TAG_OBJECT, value="")
    assert isinstance(object_element, Element)
    assert isinstance(object_element, ObjectElement)
