import os
import xml.etree.ElementTree as ET
import codecs

def process_meta_file(meta_file, old_substring, new_substring):
    try:
        # Try to open and read the file with different encodings
        for encoding in ['utf-8', 'utf-16', 'iso-8859-1', 'windows-1252']:
            try:
                with codecs.open(meta_file, 'r', encoding=encoding) as file:
                    content = file.read()
                break
            except UnicodeDecodeError:
                continue
        else:
            print(f"Could not decode {meta_file} with any known encoding")
            return

        # Check if the old_substring exists in the content before parsing
        if old_substring not in content:
            print(f"'{old_substring}' not found in {meta_file}")
            return

        # Parse the meta file content as XML
        root = ET.fromstring(content)
        changes_made = False

        # Function to process elements recursively
        def process_element(element):
            nonlocal changes_made
            if element.text and old_substring in element.text:
                element.text = element.text.replace(old_substring, new_substring)
                changes_made = True
                print(f"Replaced '{old_substring}' with '{new_substring}' in text of <{element.tag}> in {meta_file}")

            for attr, value in element.attrib.items():
                if old_substring in value:
                    element.attrib[attr] = value.replace(old_substring, new_substring)
                    changes_made = True
                    print(f"Replaced '{old_substring}' with '{new_substring}' in attribute '{attr}' of <{element.tag}> in {meta_file}")

            for child in element:
                process_element(child)

        # Process the root element and all its children
        process_element(root)

        if changes_made:
            # Write the changes back to the file
            tree = ET.ElementTree(root)
            tree.write(meta_file, encoding="utf-8", xml_declaration=True)
            print(f"Changes saved to {meta_file}")
        else:
            #print(f"No changes made in {meta_file}")

    except ET.ParseError as e:
        print(f"XML parsing error in {meta_file}: {e}")
    except Exception as e:
        print(f"Error processing {meta_file}: {e}")

def main():
    path = "D:\\txData\\CFXDefaultFiveM_C41E8E.base\\resources\\allinone_cars"
    old_substring = "dc_s500mansory"
    new_substring = "none"

    # File renaming part
    print("Renaming files:")
    for root, dirs, files in os.walk(path):
        print(f"Searching in folder: {root}")
        for file in files:
            if old_substring in file:
                old_file_name = os.path.join(root, file)
                new_file_name = os.path.join(root, file.replace(old_substring, new_substring))
                os.rename(old_file_name, new_file_name)
                print(f"Renamed {old_file_name} to {new_file_name}")

    # Meta file content modification part
    print("\nProcessing meta files:")
    for root, dirs, files in os.walk(path):
        print(f"Searching in folder: {root}")
        for file in files:
            if file.endswith(".meta"):
                meta_file = os.path.join(root, file)
                print(f"Processing meta file: {meta_file}")
                process_meta_file(meta_file, old_substring, new_substring)

    print("Processing complete.")

if __name__ == "__main__":
    main()
