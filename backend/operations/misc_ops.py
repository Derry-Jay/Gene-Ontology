import re


class OtherOperations:
    def generateUpdateStatement(self, tableName, data):
        ust = '''update ''' + tableName + ''' set'''
        k = 0
        pk = ''
        for i in data.keys():
            if re.search('_id', i) is None:
                ust += (i + '''=%s''')
                if k < len(data.keys()) - 2:
                    ust += ''', '''
                else:
                    ust += ''' '''
                k += 1
            else:
                pk = re.search('_id', i).string
        ust += ('''where ''' + pk + '''=%s''')
        return ust

    def generateCountStatement(self, tableName, data, primaryKey):
        cqs = '''select count(''' + primaryKey + ''') from ''' + \
            tableName + ''' where '''
        k = 0
        for i in data.keys():
            if re.search('_id', i) is None:
                cqs += (i + '''=%s''')
                if k < len(data.keys()) - 1:
                    cqs += ''' and '''
                k += 1
        return cqs

    def generateInsertStatement(self, tableName, data):
        inst = '''insert into ''' + tableName + '''('''
        k = 0
        for i in data.keys():
            inst += i
            if k < len(data.keys()) - 1:
                inst += ''', '''
            else:
                inst += ''') '''
            k += 1
        inst += '''values('''
        for i in range(len(data.keys())):
            inst += '''%s'''
            if i < len(data.keys()) - 1:
                inst += ''', '''
            else:
                inst += ''')'''
        return inst

    def getListFromDict(self, data):
        g = []
        pk = ''
        for i in data.keys():
            if re.search('_id', i) is None:
                g.append(data[i])
            else:
                pk = re.search('_id', i).string
        if pk != '':
            g.append(data[pk])
        return g