import os

folder_name = "my_folder"

# Create a folder/directory
os.mkdir(folder_name)


# Adding a file inside a folder

import os

folder_name = "my_folder"
file_name = "jessica.txt"
file_path = os.path.join(folder_name, file_name)

# Create a file inside the folder
file = open(file_path, "w")
file.close()

# In this example, the os module is imported to utilize the join() function for creating the file path. The variables folder_name and file_name store 
# the names for the folder and file, respectively. The os.path.join() function is used to concatenate the folder name and file name, 
# creating the complete file path. The open() function is then used with the file path and the mode "w" (write mode) to create 
# the file inside the specified folder.
# After running this code, a new file named "my_file.txt" will be created inside 
# the "my_folder" directory, located in the same directory as your Python script.