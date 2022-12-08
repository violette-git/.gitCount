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



student_list = {}
student_list = set()
print(type(student_list))

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
        # print(title)
        author = embed.author.name

        print(author)

        
        if len(student_list) == 0:

            student = Student(str(author))

            student_list.add(student)

            return f'{author} was added to the list of students'

        if len(student_list) > 0:

            print(f'{author}')

            for s in student_list:

                list = [s.name for s in student_list if len(student_list) > 0]

                if str(author) not in list:

                    print(f'{author}')

                    student = Student(str(author))
                
                    student_list.add(student)
            
                    return f'{author} was added to the list of students'
                    # print(student_list)
                    # print(author)

                else:
                    return 'calculating...'            


        if title.startswith('New comment on pull request '):

            if author:

                t = dt.datetime.now()

                for s in student_list:

                    if author == s.name:

                        s.parse_comments(before)
            
                        # print(s.comment for s in student_list if student_list)
                        return f'{s.name}: {t.day} {t.month} {t.year}'

        if title.startswith('Pull request opened:'):

            pull = 'pull added' 

            return pull

        elif title.startswith('1 new commit:'):
            
            if author:

                t = dt.datetime.now()



            pull = 'pull added' 

            return pull    
    
    if user_message.lower() == 'git push count':

        push = 'push got'

        return push

    elif user_message.lower() == 'git commit count':
        
        return 'counted'

    elif user_message.lower() == 'git students':        #complete

        list = [s.name for s in student_list if len(student_list) > 0]

        print(list)

        return list        

    else:

        return f'invalid command'



