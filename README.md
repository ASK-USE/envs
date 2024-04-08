This should be an app who allows you to convert Jupyter Notebooks in a executable Pythonfile. 
Actually i try to implement some features to allow more functionalities and more options to choose ( like input and output paths). 

actually implemented: 
- converts .ipynb-files in .py-files. (basic functions, only a little bit more than the nbconvert-command can do)
    - names the converted files into a static name, followed by a uniqe number, created from its timestamp. Works pretty well. (no testing besides a simple "does it work?"-Test was done yet)
    - puts the converted file in a defined folder (output) within the projects directory. Later it should be possible to (optionally) define a outputdirectory  
- Added a Markdown-Converter to handle and correctly convert the markdown-cells from a Jupyter Notebook into a pythonfile. (very basic at this monemt)
    - this Markdownconverter is able to convert a picture within the Notebookfile into the Pythonfile. at this moment it only converts a linked picture file from wikipedia. Later this should be able to do the          same that the Notebook does with its Pictures (to prevent copyright issuses, no functionallities beside the notebooks functionallites should be implemented)
   - in the next steps i wanna try to create as much functions as needed to convert aa much markdown functionalities as possible. 

Later goals: 
- Implementing Code- and Markdown-Cells in its given order. Both, markdown and code should be wirking in the Pythonfile, and later in the app. 
- also should the converter be able to create a web-app from the notbook/pythonfile. also it should bew possible to connect with a database.    
