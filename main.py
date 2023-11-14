from pyexcel_ods3 import get_data
from pyexcel_xlsx import save_data

#add the path to the .ods file
dataXlsx = get_data(r"your .ods path here")
#add the path where to save the .xlsx file
save_data(r"your .xlsx path here", dataXlsx)
