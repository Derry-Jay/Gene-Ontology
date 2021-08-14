import re


class OtherOperations:

    def generateSelectStatement(self, tableName, attributes, data=None):
        sst = '''select '''
        j = 0
        for i in attributes:
            sst += i
            if j < len(attributes) - 1:
                sst += ''', '''
            j += 1
        sst += ''' from ''' + tableName
        j = 0
        if data != None and len(data.keys()) != 0:
            sst += ''' where '''
            for k in data.keys():
                sst += (k + '''=%s ''')
                if j < len(data.keys()) - 1:
                    sst += '''and '''
        return sst

    def generateUpdateStatement(self, tableName, data):
        ust = '''update ''' + tableName + ''' set'''
        k = 0
        pk = ''
        for i in data.keys():
            if re.search('_id', i) is None and re.search('_token', i) is None:
                ust += (i + '''=%s''')
                if k < len(data.keys()) - 2:
                    ust += ''', '''
                else:
                    ust += ''' '''
                k += 1
            elif re.search('_token', i) is None:
                pk = re.search('_token', i).string
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

    def logicalXOR(self, a, b):
        return False if a and b else a or b
