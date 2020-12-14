
from classes.reviewer import Reviewer
import random

class PRCommand:

    def __init__(self, number_reviewers_per_pr):
        self.number_reviewers_per_pr = number_reviewers_per_pr
        self.list_reviewer = [Reviewer('Ivan'), Reviewer('Jozimar'), Reviewer('Kaio'), 
                                Reviewer('Lucas'), Reviewer('Rubens'), Reviewer('Wandson')]

    def is_pr_without_reviewers(self, pr_id):
        for reviewer in self.list_reviewer:
            if reviewer.pr_id == pr_id:
                return False
        return True

    def set_reviewer_pr_id(self, reviewer_name, pr_id):
        for reviewer in self.list_reviewer:
            if reviewer.name == reviewer_name:
                reviewer.pr_id = pr_id
                return

    def message_list_reviewers(self, list_reviewers):
        message = ''
        len_list_reviewers = len(list_reviewers)
        if len_list_reviewers == 0:
            return message
        for index in range(len_list_reviewers):
            if index == len_list_reviewers - 1:
                message += 'and %s' %list_reviewers[index]
            else:
                message += '%s, ' %list_reviewers[index]
        return message
    
    def create_pr(self, pr_id):
        if not self.is_pr_without_reviewers(pr_id):
            print('PR %s already has reviewers!' %pr_id)
            return
        list_reviewer_not_reviewing = [reviewer for reviewer in self.list_reviewer if not reviewer.pr_id]
        if len(list_reviewer_not_reviewing) < self.number_reviewers_per_pr:
            print('There are not enough reviewers!')
            return
        reviewers_for_that_pr = random.sample(list_reviewer_not_reviewing, k = self.number_reviewers_per_pr)
        for reviewer in reviewers_for_that_pr:
            self.set_reviewer_pr_id(reviewer.name, pr_id)
        print('Allocated %s to PR %s.' %(self.message_list_reviewers([reviewer for reviewer in self.list_reviewer if reviewer.pr_id == pr_id]), pr_id))

    def free_reviewers(self, method, pr_id):
        list_free_reviewers = []
        for reviewer in self.list_reviewer:
            if reviewer.pr_id == pr_id:
                reviewer.pr_id = ''
                list_free_reviewers.append(reviewer)
        if len(list_free_reviewers) > 0:
            print('%s PR %s free reviewers %s.' %(method, pr_id, self.message_list_reviewers(list_free_reviewers)))
        else:
            print('PR %s does not exist!' % pr_id)

    def merge_pr(self, pr_id):
        self.free_reviewers('Merge', pr_id)

    def delete_pr(self, pr_id):
        self.free_reviewers('Delete', pr_id)

    def reviewer_pr(self, pr_id):
        list_reviewer_per_pr = [reviewer for reviewer in self.list_reviewer if reviewer.pr_id == pr_id]
        message = self.message_list_reviewers(list_reviewer_per_pr)
        if message == '':
            print('PR %s does not have reviewers!' % pr_id)
        else:
            print('%s.' % message)

    def available_reviewers(self):
        list_available_reviewer = [reviewer for reviewer in self.list_reviewer if not reviewer.pr_id]
        message = self.message_list_reviewers(list_available_reviewer)
        if message == '':
            print('There are no reviewers available!')
        else:
            print('%s.' % message)
    
    def busy_reviewers(self):
        list_pr_with_reviewers = set([reviewer.pr_id for reviewer in self.list_reviewer if reviewer.pr_id])
        group_reviewers_by_pr = {}
        for pr in list_pr_with_reviewers:
            group_reviewers_by_pr[pr] = [reviewer for reviewer in self.list_reviewer if reviewer.pr_id == pr]
        if len(group_reviewers_by_pr) == 0:
            print('There are no busy reviewers!')
        else:
            message = ''
            for pr in sorted(list_pr_with_reviewers):
                message += 'PR %s: %s;\n' %(pr, self.message_list_reviewers(group_reviewers_by_pr[pr]))
            print(message)