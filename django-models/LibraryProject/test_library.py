import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Library

library = Library.objects.create(name="Terminal Test Library")
print(Library.objects.all())