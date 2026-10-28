
import os
import sys
import shutil


def fileOrganizer(folder_location):
    fileExtensions = {
        "Image": (".jpeg", ".jpg", ".png", ".gif"),
        "Text": (".txt",),
        "PDF": (".pdf",),
        "Document": (".doc", ".docx"),
        "Excel": (".xls", ".xlsx"),
        "Video": (".mp4", ".mkv"),
        "Audio": (".mp3", ".wav")
    }

    for file in os.listdir(folder_location):
        file_path = os.path.join(folder_location, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        matched = False

        # Find the correct category
        for category, extensions in fileExtensions.items():
            if file.lower().endswith(extensions):
                target_folder = os.path.join(
                    folder_location, category
                )

                # Create folder if it does not exist
                os.makedirs(target_folder, exist_ok=True)

                destination_path = os.path.join(
                    target_folder, file
                )

                shutil.move(file_path, destination_path)
                print(f"Moved: {file} -> {category}/")

                matched = True
                break

        # Move unsupported file types to Other
        if not matched:
            other_folder = os.path.join(
                folder_location, "Other"
            )
            os.makedirs(other_folder, exist_ok=True)

            destination_path = os.path.join(
                other_folder, file
            )

            shutil.move(file_path, destination_path)
            print(f"Moved: {file} -> Other/")


while True:
    FolderLocation = input(
        "Enter folder path or type Exit to quit: "
    ).strip()

    if FolderLocation.lower() == "exit":
        print("Exiting program...")
        sys.exit()

    try:
        if not os.path.isdir(FolderLocation):
            print("Invalid folder path. Try again.")
            continue

        if not os.listdir(FolderLocation):
            print("The folder is empty. Nothing to organize.")
            continue

        fileOrganizer(FolderLocation)
        print("File organization completed!")

    except Exception as e:
        print(f"An error occurred: {e}")
