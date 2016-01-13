# gitverbose
Selects Git log messages in a fancy-free way.


Usage:

```bash
$ git log > log.txt
$ python
```

```python
import gitverbose as gb 
myLog = gb.Log("path/to/log.txt")

longest = myLog.GetLongestCommit()
print longest.toString() # Prints the entire log section

print longest.GetMessage() # Prints the comment comment

print longest.GetMesssageLength() # Prints the number of lines.

chatty = myLog.GetCommitsOverNLines(20) # Gets the commits that have 20 lines or more.
print '\n'.join([chat.toString() for chat in chatty]) # Prints all commits that are 20 lines or more
```

