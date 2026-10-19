import os  # Import the os module for file system operations
import json
import shutil

def create_Base_Folders(folder='savedFiles', subfolder='/savedFiles/Architecture'):
	from com.inductiveautomation.ignition.gateway import IgnitionGateway
	context = IgnitionGateway.get()
	projectParentFolder = str(context.systemManager.dataDir.absoluteFile).replace('\\','/')
	folders_to_create = [projectParentFolder +"/"+ folder]
	if subfolder!="":
		folders_to_create.append(projectParentFolder +"/"+ folder +"/"+ subfolder)
	
	logger = system.util.getLogger("createSystemFolder")  # Set up logging
	for folderPath in folders_to_create:
		try:
			if not os.path.exists(folderPath):
				os.mkdir(folderPath)
				logger.trace('Created: {}'.format(folderPath))
			else:
				logger.trace('Folder Already Exists: {}'.format(folderPath))
		except OSError as e:
			logger.warn('Folder Creation Error: {}'.format(e))

def create_folder(folderPath):
	logger = system.util.getLogger("createSystemFolder")  # Set up logging
	try:
		if not os.path.exists(folderPath):
			create_Base_Folders()
			os.mkdir(folderPath)
			logger.trace('Created: {}'.format(folderPath))
		else:
			logger.trace('Folder Already Exists: {}'.format(folderPath))
	except OSError as e:
		logger.warn('Folder Creation Error: {}'.format(e))


def read_file(file_path):
	"""	Reads and retrieves the contents of a JSON file.
	Args:
	    file_path (str): Path to the JSON file.
	Returns:
	    str: Contents of the JSON file as a string. Returns None on failure.
	"""
	logger = system.util.getLogger("FileSystemOpen")
	try:
		with open(file_path, 'r') as file:
			file_content = file.read()
			data = file_content
			logger.trace('File Read Successfully: "{}"'.format(file_path))
			return data
	except IOError as e:
		logger.warn("Error reading file: {}".format(e))
		return None
	except ValueError as e:
		logger.warn("Error decoding JSON: {}".format(e))
		return None

def save_file_to_directory(file_name,directory_path, data):
	logger = system.util.getLogger("FileSystemSave")
	try:
	    if not os.path.exists(directory_path):
	   		create_Base_Folders()
	   		os.mkdir(directory_path)
	except OSError as e:
	    logger.warn("Error Saving to Directory: {}".format(e))
	    return False
	# Specify the file path
	file_path = '{}/{}.json'.format(directory_path,file_name)
	# Write the data to a JSON file
	with open(file_path, 'w') as json_file:
		json.dump(data, json_file)
		logger.trace("{} saved".format(file_name))
		return True
		
def move_file(src_path, dest_path):
    logger = system.util.getLogger("FileSystemMove")
    try:
        # Check if the source file exists
        if os.path.exists(src_path):
            # Rename (move) the file
            os.rename(src_path, dest_path)
            logger.trace('File moved successfully from "{}" to "{}"'.format(src_path, dest_path))
        else:
            logger.warn("Source file does not exist: {}".format(src_path))
    except OSError as e:
        logger.warn("Error moving file: {}".format(e))

def rename_directory(old_dir_path, new_dir_path):
    logger = system.util.getLogger("FileSystemRename")
    try:
        # Check if the old directory exists
        if os.path.exists(old_dir_path):
            # Rename the directory
            os.rename(old_dir_path, new_dir_path)
            logger.trace('File renamed successfully from "{}" to "{}"'.format(old_dir_path, new_dir_path))
        else:
            logger.trace("File does not exist: {}".format(old_dir_path))
    except OSError as e:
        logger.warn("Error renaming file: {}".format(e))
        
def delete_file(file_path):
    logger = system.util.getLogger("FileSystemDeleteFile")
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Remove the file
            os.remove(file_path)
            logger.trace("File deleted successfully: {}".format(file_path))
        else:
            logger.trace("File does not exist: {}".format(file_path))
    except OSError as e:
        logger.warn("Error deleting file: {}".format(e))

def delete_directory(directory_path):
    logger = system.util.getLogger("FileSystemDeleteDirectory")
    try:
        # Check if the directory exists
        if os.path.exists(directory_path):
            # Remove the directory and all its contents
            shutil.rmtree(directory_path)
            logger.trace("Directory and all its contents deleted successfully: {}".format(directory_path))
        else:
            logger.trace("Directory does not exist: {}".format(directory_path))
    except OSError as e:
        logger.warn("Error deleting directory: {}".format(e))
        

def downloadArchitecture(jsonFile, filename):
	fileSave=system.util.jsonEncode(jsonFile)
	filename='{}_{}.json'.format(filename.replace('.json',''),system.date.format(system.date.now(),"yyyyMMdd"))
	system.perspective.download(filename, fileSave)