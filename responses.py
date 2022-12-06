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
    # print(embeds)
    # print(dir(embeds))
    for embed in embeds:        
        # print(embed)
        title = embed.title
      
        n = 1

        groups = title.split('] ')

        ' '.join(groups[:n])
        
        ' '.join(groups[n:])

        before = groups[0]

        title = groups[1]
        print(title)
        author = embed.author.name

        
        if len(student_list) == 0:

            student = Student(author)

            student_list.append(student)

        for s in student_list:

            if author != s.name:

                student = Student(author)

                student_list.append(student)
                
                # print(s.)
            
                return f'{s.name} was added to the list of students'
            

        if title.startswith('New comment on pull request '):

            if author:

                t = dt.datetime.now()

                for s in student_list:

                    if author == s.name:

                        s.parse_comments(before)
            
                        print(s.comment)
            return f'{s.name}: {t.day} {t.month} {t.year}'
            
            #     return f'{t}'

        if title.startswith('Pull request opened:'):

            pull = 'pull added' 

            return pull

        if title.startswith('1 new commit:'):
            
            if author:

                t = dt.datetime.now()

                

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



