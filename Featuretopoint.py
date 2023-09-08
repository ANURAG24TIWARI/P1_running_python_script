import arcpy
# assigning path of wilson_zoning to variable
wilson_zone_path = r"E:\Sem_3\programming_3_practical\ProProject_Practical_One1\ProProject_Practical_One\Practical_One.gdb\Wilson_Zoning"
# converting wilson_zoning feature class to point
wilson_point = wilson_zone_path + "_FeatureToPoint"
arcpy.management.FeatureToPoint(wilson_zone_path,wilson_point)