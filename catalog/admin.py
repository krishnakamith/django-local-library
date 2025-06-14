from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = [('first_name', 'last_name'),('date_of_birth', 'date_of_death')]

    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
   model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]

    def display_genre(self, obj):
        return ','.join(genre.name for genre in obj.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_date', 'id')
    list_filter = ('status', 'due_date')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_date')
        }),
    )