import os
import sys

def main():
    data_path = os.path.join(sys.path[0], "../data/raw/")
    output_path = os.path.join(sys.path[0], "../datasets/dataset2/compiled.txt")
    
    with open(output_path, 'w', encoding='utf-8') as f_out:
        for file in os.listdir(data_path):
            filename = os.fsdecode(file)
            if filename.endswith(".txt"):
                print(os.path.join(data_path, filename))
                with open(os.path.join(data_path, filename), 'r', encoding='utf-8') as f_in:
                    for line in f_in:
                        message = line.partition('>')[2]
                        message = message.lstrip().rstrip()
                        message = '<BOS>' + message + '<EOS>\n'
                        f_out.write(message)
                continue
            else:
                continue


if __name__ == "__main__":
    main()