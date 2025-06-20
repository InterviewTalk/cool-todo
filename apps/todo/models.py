from django.db import models


# define our table of todos
class Todo(models.Model):
    # primary key
    id = models.AutoField(primary_key=True)
    # short name
    item = models.CharField(max_length=50)
    # long details
    notes = models.CharField(max_length=200)
    # is it done yet?
    complete = models.BooleanField(default=False)

    # created at - auto populate
    created_at = models.DateTimeField(auto_now_add=True)
    # updated at - auto populate
    updated_at = models.DateTimeField(auto_now=True)
    # soft delete
    removed_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f"id:{self.id} item:{self.item} notes:{self.notes} complete:{self.complete} created_at:{self.created_at.isoformat()}, updated_at:{self.updated_at.isoformat()}, removed_at:{self.removed_at.isoformat() if self.removed_at else ''}"

    # option to mark the todo item complete
    def set_complete(self):
        # set the complete boolean True
        self.complete = True
        self.save()
