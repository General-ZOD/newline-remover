/*
@author: General ZOD
@file: newline_remover.py
*/
This script removes all the extra newlines (lines between paragraphs) in any text file
---------------------------------------------------------------------------------

To use the script, just run the script in a shell, supplying the file's ABSOLUTE PATH as an argument just like
python newline_remover.py path_to_filename
OR as a module
 call the "main(absolute_path_to_file)" function


TECHNICAL 

algorithm
------------
- Get the file (how the file is gotten depends on how the program is called)
- Check if the file exists and exit if it doesn't
- Open the file and create a temporary file to store the content
- Loop through the file's content, taking content from each line per loop
   - since the file's size isn't known, there might not be enough memory if the whole file was loaded into 
     memory at once
- Remove the newline sign and check if the content is empty; write the content into the new file if the content is not empty
- Once done, rename the new file to the old file  
