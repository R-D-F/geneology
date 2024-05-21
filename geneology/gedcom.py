"""

"""
import arcpy
import json

def get_json_as_list_of_dict(file_name):
    with open (file_name, 'r') as file:
        data = json.load(file)
    return data



def add_message():
    arcpy.AddMessage("hello world")

def main():
    data = get_json_as_list_of_dict(r"C:/Users/rifra/homework/geneology/family_dict.json")
    # Set your workspace (adjust this path to where you want to store the feature class)
    arcpy.env.workspace = r"C:/Users/rifra/homework/geneology/geneology/geneology.gdb"

    # Define the spatial reference (WGS 1984)
    spatial_reference = arcpy.SpatialReference(3857)

    # Create a new feature class
    feature_class_name = "BirthPlaces"
    arcpy.CreateFeatureclass_management(arcpy.env.workspace, feature_class_name, "POINT", spatial_reference=spatial_reference)

    # Add fields to the feature class
    arcpy.AddField_management(feature_class_name, "FirstName", "TEXT")
    arcpy.AddField_management(feature_class_name, "LastName", "TEXT")
    arcpy.AddField_management(feature_class_name, "BirthDay", "TEXT")
    arcpy.AddField_management(feature_class_name, "BirthPlace", "TEXT")

    wgs84_sr = arcpy.SpatialReference(4326)  # WGS 1984 spatial reference
    with arcpy.da.InsertCursor(feature_class_name, ["SHAPE@", "FirstName", "LastName", "BirthDay", "BirthPlace"]) as cursor:
        for entry in data:
            # Create the point in WGS 1984
            point_wgs84 = arcpy.Point(entry['birth_place_long'], entry['birth_place_lat'])
            point_geom_wgs84 = arcpy.PointGeometry(point_wgs84, wgs84_sr)
            
            # Project the point to Web Mercator
            point_geom_mercator = point_geom_wgs84.projectAs(spatial_reference)
            
            # Insert the projected point
            cursor.insertRow([point_geom_mercator, entry['name'][0].strip(), entry['name'][1].strip(), entry['birth_day'].strip(), entry['birth_place'].strip()])


main()