import math

class TfIdf:

    wordRankAddr = 'wordRank'
    pageAddr = 'chinese_news_1w_seg'

    def FreqDist(self,wordList):
        dic = {}
        for word in wordList:
            if word != None:
                if dic.get(word) == None:
                    dic[word] = 1
                else:
                    dic[word] += 1
        return dic

 
    def ComputeTf(self,text):
        wordList = text.split(' ')
        tf =self.FreqDist(wordList)
        return tf


    def ReadWordRank(self,fileAddr):
        f = open(fileAddr)
        wordRank = {}
        for line in f.readlines():
            tmp = line.split(' ')
            wordRank[tmp[0]] = float(tmp[1])
        return wordRank


    def GetSentRank(self):
        wordRank = self.ReadWordRank(self.wordRankAddr) 
        sentRank = []
        idff= open(self.pageAddr)
        for line in idff.readlines():
            reason = '' 
            idf = self.ComputeTf(line)
            scoreSum = 0.0
            for word in idf.keys():
                if wordRank.get(word) == None:
                    pass
                else:
                    reason += (word + '=' + str(wordRank[word]))
                    scoreSum += wordRank[word]
            sentRank.append([scoreSum,line,reason])
        sentRank.sort()
        sentRank.reverse()
        idff.close()
        return sentRank

    def WriteToFile(self,outPutAddr):
        sentRank = self.GetSentRank()
        fsentRank = open(outPutAddr,'w')
        for sent in sentRank:
            fsentRank.write(str(sent[0]).decode('utf-8').encode('utf-8'))
            fsentRank.write(' '.encode('utf-8'))
            fsentRank.write(str(sent[1]).decode('utf-8').encode('utf-8'))
            fsentRank.write(' '.encode('utf-8'))
            fsentRank.write(str(sent[2]).decode('utf-8').encode('utf-8'))
            fsentRank.write('\n'.encode('utf-8'))
        fsentRank.close()
"""
if __name__=="__main__":           
    t = TfIdf()
    wordLib =  t.ComputeIdf('result_seg_cn')       
    f  = open('ttttt','w')
    print repr(wordLib)
    for word in wordLib.keys():
        f.writelines(str(word)+str(wordLib[word]))
        f.write('\n')
    
    print type(wordLib)
    print dir(wordLib)
"""
"""
#this is a old version about tf
    def GetWordRank(self):
        queryText = open(self.queryAddr).read()
        pageText = open(self.pageAddr).read() 
        tf = self.ComputeTf(queryText)
        idf = self.ComputeTf(pageText)
        wordRank={}.fromkeys(idf.keys())
        for word in tf:
            wordRank[word] = (tf[word]/(idf[word]+1.0))
        queryText.close()
        queryAddr.close()
        return wordRank 
"""
"""
if __name__=="__main__":
    fw  = open('wordRank_new','w')
    t = TfIdf()
    wordRank = t.ReadWordRank('wordRank')
    for word in wordRank.keys():
        fw.writelines(str(word)+' '+str(wordRank[word]))
        fw.write('\n')
    fw.close() 
"""
if __name__=="__main__":
    t = TfIdf()
    t.WriteToFile('sentRank')
