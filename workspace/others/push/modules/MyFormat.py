import os
import glob

replacements = {
    '\n': '\n\n\n',
    'cảnh giới hạn': 'cảnh bị giới hạn',
    # '\\includegraphics[width': '\\includegraphics[scale=',
    # '\\includegraphics[ width': '\\includegraphics[scale=',
    # '\\includegraphics[height': '\\includegraphics[scale=',
    # '\\includegraphics[ height': '\\includegraphics[scale=',
    # '=': '=',
    # '+': '+',
    # '<!--': '%!',
    # '-->': '',
    # '-': '-',
    # '\\(': '$',
    # '\\)': '$',

    # 'Monolithic': 'kiến trúc nguyên khối',
    # 'monolithic': 'kiến trúc nguyên khối',

    # 'Microservices': 'kiến trúc vi dịch vụ',
    # 'microservices': 'kiến trúc vi dịch vụ',
    # 'Microservice': 'kiến trúc vi dịch vụ',
    # 'microservice': 'kiến trúc vi dịch vụ',
    # 'dịch vụ vi mô': 'vi dịch vụ',


    # 'ddd': 'thiết kế hướng miền',
    # 'DDD': 'thiết kế hướng miền',

    # "newpage":" newpage"
}


class MyFormat:
    # def workspace(workspace_path):
    #     with open(workspace_path, 'r', encoding="utf-8") as file:
    #         contents = file.read()
    #     while '  ' in contents:
    #         contents = contents.replace('  ', ' ')
    #     contents = '\n'.join(line.strip() for line in contents.split('\n'))
    #     while "\n\n\n" in contents:
    #         contents = contents.replace("\n\n\n", "\n\n")
    #     contents = contents.lstrip('\n')
    #     with open(workspace_path, 'w', encoding="utf-8") as file:
    #         file.write(contents)

    # def markdown(git_path):
    #     files = glob.glob(os.path.join(git_path, f'**/*.md'), recursive=True)
    #     for file_markdown in files:
    #         with open(file_markdown, 'r', encoding="utf-8") as file:
    #             contents = file.read()

    #         if contents == '':
    #             continue

    #         contents = contents.replace('\n', '\n\n\n')

    #         while '  ' in contents:
    #             contents = contents.replace('  ', ' ')
    #         contents = '\n'.join(line.strip() for line in contents.split('\n'))
    #         while "\n\n\n" in contents:
    #             contents = contents.replace("\n\n\n", "\n\n")
    #         contents = contents.lstrip('\n')
    #         with open(file_markdown, 'w', encoding="utf-8") as file:
    #             file.write(contents)

    def basic1(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()


        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)
    def basic2(path):
        with open(path, 'r', encoding="utf-8") as file:
            contents = file.read()

        contents = contents.replace('\n', '\n\n\n\n\n')

        while '  ' in contents:
            contents = contents.replace('  ', ' ')
        contents = '\n'.join(line.strip() for line in contents.split('\n'))
        while "\n\n\n" in contents:
            contents = contents.replace("\n\n\n", "\n\n")
        contents = contents.lstrip('\n')
        with open(path, 'w', encoding="utf-8") as file:
            file.write(contents)

    def latex(contents): 
        if os.path.isfile(contents):
            MyFormat.basic1(contents) 
        else:


            latex_files = glob.glob(os.path.join(
                contents, f'**/*.tex'), recursive=True)

            for latex_file in latex_files:
                with open(latex_file, 'r', encoding="utf-8") as file:
                    contents = file.read()

                while '  ' in contents:
                    contents = contents.replace('  ', ' ')

                while '( ' in contents:
                    contents = contents.replace('( ', '(')
                while ' )' in contents:
                    contents = contents.replace(' )', ')')
                while '[ ' in contents:
                    contents = contents.replace('[ ', '[')
                while ' ]' in contents:
                    contents = contents.replace(' ]', ']')
                while '{ ' in contents:
                    contents = contents.replace('{ ', '{')
                while ' }' in contents:
                    contents = contents.replace(' }', '}')

                with open(latex_file, 'w', encoding="utf-8") as file:
                    file.write(contents)

                MyFormat.basic2(latex_file)
