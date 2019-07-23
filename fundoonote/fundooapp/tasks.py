from __future__ import absolute_import, unicode_literals
from self import self
from .mailer import Mailer
from .models import Notes, Label
from celery import shared_task

""" The @shared_task decorator returns a proxy that always uses the task instance 
in the current_app: """
@shared_task
def count_notes():  # count the number of notes
    return Notes.objects.count()

@shared_task
def update_notes(notes_id, title,trash, deleted): # rename the title
    note = Notes.objects.get(id=notes_id)
    note.title=title # take title field
    note.trash=trash
    note.deleted=deleted
    note.save()
    return note

@shared_task
def update_label(label_id, text):  # update label
    label = Label.objects.get(id=label_id) # verifying the label id
    label.text=text # update the text
    label.save() # save label

mail = Mailer()   # call class Mailer
mail.send_messages(subject=' Email account verification',
                   template='fundooapp/hello.html', # rendering hello.html
                   context={'user': self},
                   to_emails=['bhaktibj402@gmail.com','admin105@gmail.com', 'admin106@gmail.com'])


