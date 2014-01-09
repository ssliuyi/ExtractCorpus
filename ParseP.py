import json

class PassageParser:

    inputAddr = 'cn'
    outputAddr = 'parseResult_cn_new'


    def DeleteBrace(self,text):
        p1=text.find('{')
        if p1 != -1:
            str1 = text[p1:-1]
            return str1


    def WriteParsePassage(self):
        f = open(self.inputAddr)
        fw = open(self.outputAddr,'w')
        for line in f.readlines():
            jsonText = line.replace('\n',' ')
            jsonText = self.DeleteBrace(jsonText)
            if None != jsonText:
                parsedText = json.loads(jsonText)
                fw.writelines(parsedText['content'].replace('\n','').encode('utf-8'))
                fw.writelines('\n'.encode('utf-8'))
        f.close()
        fw.close()


if __name__=="__main__":
    p = PassageParser()
    p.WriteParsePassage()
