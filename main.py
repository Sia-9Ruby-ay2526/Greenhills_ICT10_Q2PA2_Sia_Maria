# Working with Sets
from pyscript import display, document

def get_name(e):

    grade_seven = {'jane doe', 'john doe', 'johnny doe', 'james doe'}
    grade_eight = {'joanne doe', 'jeremy doe', 'joel doe', 'joshua doe'}
    grade_nine = {'jenna doe', 'joebelle doe', 'joseph doe', 'jolly doe'}
    grade_ten = {'jessie doe', 'jessica doe', 'joanna doe', 'jeremiah doe'}

    f_name = document.getElementById('f_name').value
    l_name = document.getElementById('l_name').value

    add_member = f"{f_name} {l_name}".lower()

    SS_club_members = {name for name in (grade_seven | grade_eight | grade_nine | grade_ten)}
    SS_club_members.add(add_member)  # Adding a new member
    display(SS_club_members, target='output')

    display(len(grade_seven | grade_eight | grade_nine | grade_ten | {add_member}),target='output')

    display_message = (f"Here are the total no. of members.")

    display(display_message, target="output")








