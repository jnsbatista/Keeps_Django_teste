from asyncio.windows_events import NULL
from tokenize import Number
from elearning.models import *

def reprova_valid(score, status):
    if score == None and status == 'A':
        return False
    if score != None and score < 6 and status == 'A':
        return False
    else:
        return True

def aprova_valid(score, status):
    if score != None and score >= 6 and status != 'A':
        return False
    else:
        return True

def term_valid(date_close, status):
    if status == 'A' and not date_close:
        return False
    else:
        return True

def quitter_valid(status, justification):
    if status == 'D' and not justification:
        return False
    else:
        return True

def user_valid_enrollment(student):
    try:
        obj = Enrollment.objects.filter(student=student, score=0, status='C')
        if obj:
            return False
        else:
            return True
    except:
        pass

    