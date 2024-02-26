import argparse
from haffman import CodeGenerator

def main():
    parser = argparse.ArgumentParser(description='Сгенерируйте код Хаффмана из текстового файла')
    parser.add_argument('file', help='Путь к входному текстовому файлу')

    args = parser.parse_args()
    
    cgen = CodeGenerator()
    cgen.gen_code(args.file)

if __name__ == "__main__":
    main()
