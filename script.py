import sys
import json
inFile = sys.argv[1]
outFile = sys.argv[2]

if (len(sys.argv) > 3):
    note_removal_flag = sys.argv[3]
else:
    note_removal_flag = None

def remove_slide_skip(input_data, note_removal=False):
    print("Starting processing of Python Notebook.")
    
    def loop(slidetype_value):
        for index, cell in enumerate(input_data['cells']):
            if type(cell.get("metadata")) is dict:
                metadata = cell.get("metadata")
                slideshow = metadata.get("slideshow")
                slide_type = slideshow.get("slide_type")
                if (slide_type == slidetype_value):
                    print(f"Found slide_type of {slidetype_value}, deleting.")
                    del input_data["cells"][index]

    if note_removal == '--notes':
        loop("notes")
        loop("skip")
    else:
        loop("skip")

    print("Finished processing Python Notebook.")
    return input_data


with open(inFile) as json_file:
    data = json.load(json_file)

processed = remove_slide_skip(data, note_removal=note_removal_flag)

with open(outFile, 'w') as o:
    json.dump(processed, o)
