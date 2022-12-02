import bot
student_dictionary = {

    'name': {
        'commit_count':0,
        'push_count':0
    }

}

# print(student_dictionary['name']['commit_count'])


def count():


    # grab all incoming messages from current day

    # split between push and commits

    # parse message text

    # save users into user list  or variable?

    # return list of variables
    # return counted_commit, counted_push
    pass


def get_response(message: object, user_message:str) -> object | str:

    embeds = message.embeds
    # print(f"'embeds': {dir(embeds)}")

    
    print(user_message)


    if type(user_message) == str:
        pass
    
    if user_message == 'git push count':

        push = 'push got'

        return push

    # if type(embeds) == object:
    for embed in embeds:

        author = embed.author.name

        title = embed.title

        print(f'{title}\n{author}')

        if title.startswith('[PdxCodeGuild/HB3] Pull request opened:'):

            pull = 'pull added' 

            return pull


        if title.startswith('[PdxCodeGuild/HB3] New comment on pull request'):

            return '`This is an editable message`'
    

    return f'invalid command'