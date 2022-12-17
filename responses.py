import bot
import sched
import datetime as dt

class Student:

    def __init__(self, name):

        self.name = name
        self.commit = 0
        self.timestamp = ''
        self.student_list = {}
        self.student_list = set()

    def parse_commits(self, commit, time):

        self.commit = self.commit + commit

        self.timestamp = time

        return f'{self.name} made {self.commit} commit(s) @ {self.timestamp}'

    def __str__(self):

        return f'{self.name}'

class StudentList:

    def __init__(self):

        self.student_list = {}
        self.student_list = set()

    def add_students(self, student):

        self.student_list.add(student)

        return f'{student} was added to list of students'

    def __str__(self):

        return f'{self.student_list}'



student_list = {}
student_list = set()
print(type(student_list))

def get_response(message: str, user_message:str) -> str | str:

    # student_list = StudentList()

    embeds = message.embeds
    # print(embeds)
    # print(dir(embeds))
    for embed in embeds:        
        # print(embed)
        title = embed.title

        user_message = user_message
      
        n = 1

        groups = title.split('] ')

        ' '.join(groups[:n])
        
        ' '.join(groups[n:])

        before = groups[0]

        title = groups[1]
        # print(title)
        author = embed.author.name

        print(author)
        print(student_list)

        
        if len(student_list) == 0:
            print('level 1')
            student = Student(str(author))



            student_list.add(student)

            numbers = title.split(' new ')

            commits = int(numbers[0])

            student.commit = student.commit + commits

            print(student.commit)

            t = dt.datetime.now()

            # student.parse_commits(commits, t)

            student_t = StudentList()

            student_t.add_students(student)

            print(student_t.student_list)

            return f'{author} was added to the list of students'

        if len(student_list) > 0:

            print('level 2')

            print(f'{author}')

            list = [s.name for s in student_list if len(student_list) > 0]

            if str(author) not in list:

                print(f'{author}')

                student = Student(str(author))
            
                student_list.add(student)

                numbers = title.split(' new ')

                commits = int(numbers[0])

                # student.commit = student.commit + commits

                print(student.commit)

                t = dt.datetime.now()

                # student.parse_commits(commits, t)

                # student_t = StudentList()

                # student_t.add_students(student)

                print(student_t.student_list)
        
                return f'{author} was added to the list of students'
                # print(student_list)
                # print(author)

            else:
                return 'calculating...'

    if user_message.lower() == 'git commits':

        list = [(s.commit, s.name) for s in student_list if len(student_list) > 0]
                
        return f'{list}'      

    else:

        return f'invalid command'



