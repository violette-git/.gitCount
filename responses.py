import bot
import sched
import datetime as dt

class Student:

    def __init__(self, name):

        self.name = name
        self.comment = 0
        self.commit = 0
        self.pull = 0
    
    def parse_comments(self, comment):

        self.comment = comment
    
    def parse_pulls(self, pull):

        self.pull = pull

    def parse_commits(self, commit):

        self.commit = commit

    def __str__(self):

        return f'{self.name}'



student_list = []
def get_response(message: str, user_message:str) -> str | str:

    embeds = message.embeds
    for embed in embeds:        
       
        title = embed.title
      
        n = 1

        groups = title.split('] ')

        ' '.join(groups[:n])
        
        ' '.join(groups[n:])

        before = groups[0]

        title = groups[1]

        author = embed.author.name

        if author not in student_list:

            author = Student(author)

            student_list.append(author)
            
            return f'{author.name} was added to the list of students'

        else: 
            pass

            author = author

        if title.startswith('New comment on pull request '):

            t = dt.datetime.now()
            
            if author in student_list:

                author.parse_comments(before)
            
                return f'{t}'

        if title.startswith('Pull request opened:'):

            pull = 'pull added' 

            return pull

        if title.startswith('1 new commit:'):

            pull = 'pull added' 

            return pull    
    
    if user_message.lower() == 'git push count':

        push = 'push got'

        return push

    if user_message.lower() == 'git commit count':
        
        return 'counted'

    if user_message.lower() == 'git students':        #complete

        list = [s.name for s in student_list if student_list]

        return list        

    else:

        return f'invalid command'



