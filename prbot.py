
from classes.pr_command import PRCommand

pr_command = PRCommand(2)
while True:
    command = input('> ')
    try:
        which_command = command.split(' pr ')
        if which_command[0] == 'create':
            pr_command.create_pr(which_command[1])
        elif which_command[0] == 'merge':
            pr_command.merge_pr(which_command[1])
        elif which_command[0] == 'delete':
            pr_command.delete_pr(which_command[1])
        elif which_command[0] == 'reviewers':
            pr_command.reviewer_pr(which_command[1])
        elif which_command[0] == 'available reviewers':
            pr_command.available_reviewers()
        elif which_command[0] == 'busy reviewers':
            pr_command.busy_reviewers()
        else:
            print('Invalid command!')
    except:
        print('Invalid command!')
