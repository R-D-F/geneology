from gedcom.element.element import Element


def test_initialization():
    element = Element(level=-1, pointer="", tag="", value="")
    assert isinstance(element, Element)
