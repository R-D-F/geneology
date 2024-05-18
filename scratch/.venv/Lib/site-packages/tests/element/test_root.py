from gedcom.element.element import Element
from gedcom.element.root import RootElement


def test_initialization():
    root_element = RootElement(level=-1, pointer="", tag="ROOT", value="")
    assert isinstance(root_element, Element)
    assert isinstance(root_element, RootElement)
