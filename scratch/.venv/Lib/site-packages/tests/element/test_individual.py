from gedcom.element.element import Element
from gedcom.element.individual import IndividualElement
import gedcom.tags


def test_initialization():
    individual_element = IndividualElement(level=-1, pointer="", tag=gedcom.tags.GEDCOM_TAG_INDIVIDUAL, value="")
    assert isinstance(individual_element, Element)
    assert isinstance(individual_element, IndividualElement)
