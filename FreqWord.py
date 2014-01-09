import math


class TfIdf:

    queryAddr = 'hw_cn_seg_utf8'
    pageAddr = 'chinese_news_1w_seg'
    stopWordsAddr = 'stopWords_utf8'

    def FreqDist(self,wordList):
        dic = {}
        for word in wordList:
            if word != None:
                if dic.get(word) == None:
                    dic[word] = 1
                else:
                    dic[word] += 1
        return dic

    def GetStopWords(self):
        f = open(self.stopWordsAddr)
        text = f.read()
        stopWordsList = text.split('\n'.encode('utf-8'))
        #print repr(stopWordsList)
        return stopWordsList

    def FilterStopWords(self,dic):
        stopWordsList = self.GetStopWords()
        for stopWord in stopWordsList:
            if dic.has_key(stopWord) == True:
                dic.pop(stopWord)
        for word in dic.keys():
            if len(word) <= 4 or word.isalnum() or word.isspace() or word[0].isalnum() or word[-1].isalnum(): 
                dic.pop(word)
        return dic
 
    def ComputeTf(self,text):
        wordList = text.split(' ')
        tf =self.FreqDist(wordList)
        return tf

    def GetNumOfLines(self,fileAddr):
        num = 0
        f = open(fileAddr)
        while True:
            if not f.readline(): break
            num+=1
        f.close()
        return num

    def GetSentList(self,fileAddr):
        f = open(fileAddr)
        sentList = []
        for line in f.readlines(): 
            sentList.append(line.split(' '))
        f.close() 
        return sentList


    def ComputeIdf(self,fileAddr):
        NumOfLines = self.GetNumOfLines(fileAddr)
        f = open(fileAddr)
        pasList  = []
        for sent in f.readlines():
            sentTf = self.ComputeTf(sent)
            pasList += sentTf.keys() 
        idf =self.FreqDist(pasList)
        return idf

    def GetWordRank(self,fileAddr):
        f = open(fileAddr)
        text = f.read()
        tf = self.ComputeTf(text)
        idf = self.ComputeIdf(fileAddr)
        wordRank = {}
        for word in idf:
            if tf.get(word) != None and word != None:
                tmp = math.log((tf[word]*idf[word]+1),2)
                if tmp != None:
                    wordRank[word] = tmp 
        wordRank = self.FilterStopWords(wordRank)
        return wordRank


    def GetSentRank(self):
        wordRank = self.GetWordRank(self.queryAddr) 
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
    fw  = open('wordRank','w')
    t = TfIdf()
    wordRank = t.GetWordRank(t.queryAddr)
    for word in wordRank.keys():
        fw.writelines(str(word)+' '+str(wordRank[word]))
        fw.write('\n')
    fw.close() 
"""
if __name__=="__main__":
    t = TfIdf()
    t.WriteToFile('sentRank')
