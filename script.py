import sys
import json
inFile = sys.argv[1]
outFile = sys.argv[2]

def remove_slide_skip(input_data):
    print("Starting processing of Python Notebook.")
    for index, cell in enumerate(input_data['cells']):
        if type(cell.get("metadata")) is dict:
            metadata = cell.get("metadata")
            slideshow = metadata.get("slideshow")
            slide_type = slideshow.get("slide_type")
            if slide_type == 'skip':
                print("Found slide_type of 'skip', deleting.")
                del input_data["cells"][index]

    print("Finished processing Python Notebook.")
    return input_data


with open(inFile) as json_file:
    data = json.load(json_file)

processed = remove_slide_skip(data)

with open(outFile, 'w') as o:
    json.dump(processed, o)
