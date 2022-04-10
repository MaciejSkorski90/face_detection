## Face detection tool

# Description
The application was created for the purpose of detecting identity cards in document collections.
The application creates a list of files with the .jpg extension in the directory, then checks which scans are human faces in 4 rotations by 90 degrees and returns a list with the result.
In the created list in the 'result' column, the application returns '1' (means that at least 1 face has been detected), and '0' (no face has been detected).

# Requirements
- python
- jupyter
- jupyterlab
* pandas
* numpy
* cv2 (open CV)
