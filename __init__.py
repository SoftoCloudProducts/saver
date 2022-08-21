print('This app is using Softo Cloud Saver')

class Saver():
    def __init__(self, fileName):
        self.fileName = fileName
    
    def read(self, field):
        with open(self.fileName + '.sc', 'r') as f:
            lines = f.readlines()
            for line in lines:
                try:
                    line.split(' = ')[1]
                    
                    fieldName = line.split(' = ')[0]
                    fieldMeaning = line.split(' = ')[1]

                    if field == str(fieldName):
                        return ''.join(fieldMeaning.split('\n'))

                except IndexError:
                    print(f'InvalidSyntax: use field = meaning\non {self.fileName}.sc, {lines.index(line) + 1}')

    def write(self, field, meaning):
        with open(self.fileName + '.sc', 'r') as f:
            lines = f.readlines()

            for line in lines:
                fieldName = line.split(' = ')[0]
                
                if fieldName == field:
                    lines[lines.index(line)] = f'{field} = {meaning}\n'
                    
                    with open(self.fileName + '.sc', 'w') as f:
                        print('фав')
                        f.write(''.join(lines))
                        return
            with open(self.fileName + '.sc', 'w') as f:
                lines.append(f'{field} = {meaning}\n')
                print('фав1')
                f.write(''.join(lines))