from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import googlemaps



# Path to your `.ged` file
file_path = 'francis_weaver.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)


root_child_elements = gedcom_parser.get_root_child_elements()
# for item in root_child_elements:
#     print(item)
# element_list = gedcom_parser.get_element_list()
# for element in element_list:
#     print(element)
# list_of_families = gedcom_parser.get_families()

# list_family_memebers = gedcom_parser.get_family_members()
# print(list_family_memebers)
birth_list = []
death_list = []
for element in root_child_elements:
    if isinstance(element, IndividualElement):
        birth_list.append({
                            "name": element.get_name(),
                            "birth day":element.get_birth_data()[0],
                            "birth place": element.get_birth_data()[1]
        })
        death_list.append({
                            "name": element.get_name(),
                            "birth day":element.get_death_data()[0],
                            "birth place": element.get_death_data()[1]
        })


# for item in birth_list:
#     for key, value in item.items():
#         print(key)
#         print(value)
#         print()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Riley")
location = geolocator.geocode("hamilton north carolina")
print(location.address)