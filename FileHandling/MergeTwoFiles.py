def merge():
    try:
        with open('./FileHandling/sample.txt', 'r') as file1, open('./FileHandling/sample2.txt') as file2, open('merge.txt', 'w') as file3:
        
            content1 = file1.read().split() 
            content2 = file2.read().split()
            all_content = content1 + content2
            unique_content = set(all_content)


            file3.write(' '.join(unique_content))

        print("Files merged successfully with duplicate words removed!")

    except FileNotFoundError as e:
        print(f"Error: One of the files was not found. Details: {e}")

    except IOError as e:
        print(f"Error: An issue occurred while reading or writing the file. Details: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
   merge()

if __name__ == "__main__":
    main()
