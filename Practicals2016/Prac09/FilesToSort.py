import os, shutil


def main():
    # change to desired directory
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())

    for dir_name, subdir_list, file_list in os.walk('.'):
        print(dir_name)
        print(subdir_list)
        print(file_list)
        extensions_to_folders_dict = {".doc": "dance"}
        for f in file_list:
            extension = os.path.splitext(f)[1]
            print("I am")
            print(extension)
            key_exists = False
            for key in extensions_to_folders_dict:
                if key == extension:
                    print("i go into")
                    print(extensions_to_folders_dict[extension])
                    print()
                    key_exists = True

            if not key_exists:
                category = input("What category would you like to sort {} files into? ".format(extension))
                print("{} will now go into {}".format(extension, category))
                print()
                extensions_to_folders_dict[extension] = category

            category = extensions_to_folders_dict[extension]
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

            shutil.move(f, category)




            # print a list of all files (test)
            # print(os.listdir('.'))

            # make a new directory
            # os.mkdir('temp')



            # Option 1: rename file to new name - in place
            # os.rename(filename, final_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp2/' + new_name)

            # Processing subdirectories using os.walk()
            # os.chdir('..')
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)
            #
            #     old_dir = os.getcwd()
            #     os.chdir(dir_name)
            #
            #     for filename in file_list:
            #         final_name = neaten_file_name(filename)
            #         os.rename(filename, final_name)
            #         print(final_name)
            #
            #     os.chdir(old_dir)


main()
