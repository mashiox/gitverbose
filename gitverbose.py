import re

class Commit:
    def __init__(self, hashNum, author, dateStr, message):
        self.hashNum = hashNum
        self.author  = author
        self.date    = dateStr
        self.message = message

    def GetHash(self):
        return self.hashNum

    def GetDate(self):
        return self.date

    def GetMessage(self):
        return '\n'.join(self.message)

    def GetMessageLines(self):
        return len(self.message)

    def GetAuthor(self):
        return self.author

    def toString(self):
        return ("commit " + self.hashNum   + "\n" 
               "Author: "+ self.author     + "\n"  
               "Date:   "+ self.date       + "\n" 
               "\n" +
               self.GetMessage() +"\n" )

class Log:
    def __init__(self, filename):
        self.__commits = self.__GetCommits(self.__GetLines(filename))
        
    def __GetLines(self, filename):
        return [ lines.rstrip('\n') for lines in open(filename) ]

    def __GetCommits(self, lines):
        commits = []
        index = 0
        offset = 0
        while (index < len(lines) ):
            message = []
            hsh = lines[index].split()[1]
            offset = 1 if re.match("Merge: [a-z0-9]+ [a-z0-9]+", lines[index+1]) else 0
            auth = lines[index+offset+1].split("Author: ", 1)[1]
            date = lines[index+offset+2].split("Date: ", 1)[1].strip()
            index += 4 #this offset includes spacer whitespace in log
            while ( index < len(lines) and re.match("commit [a-z0-9]+", lines[index] ) == None ):
                message.append( lines[index] )
                index += 1
            #end while
            message.pop() if len(message) > 1 else 0
            commits.append( Commit(hsh, auth, date, message ) )
        #end while
        return commits
    
    '''
    Singular
    Gets a single commit with the longest commit message
    '''
    def GetLongestCommit(self):
        return sorted(self.__commits, key = lambda commit: commit.GetMessageLines() ).pop()

    '''
    Plural
    Gets all the commits with the longest commit messages
    '''
    def GetLongestCommits(self):
        return [ commit for commit in self.__commits if commit.GetMessageLines() >= self.GetLongestCommit().GetMessageLines() ]

    '''
    Gets Commits with messages over n lines long
    '''
    def GetCommitsOverNLines(self, n):
        if ( n < 0 ):
            raise ValueError("n must be 0 or larger")
        return [ commit for commit in self.__commits if commit.GetMessageLines() >= n ]
        
    '''
    Returns the string of the logfile
    '''
    def toString(self): return '\n'.join([ commit.toString() for commit in self.__commits ])


