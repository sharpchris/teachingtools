from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    option = models.CharField(max_length=20, unique=True, help_text="A short, unique tag for internal use by the webpage. Not visible, and must not have spaces.")
    verbose_name = models.CharField(max_length=50, help_text="The public-facing name of this category.")
    tooltip = models.CharField(max_length=255, help_text="The text that is visible when hovering over the category button.")

    def __str__(self):
        return self.option

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Tool(models.Model):
    def get_upload_path(self, filename):
        path = f'./{self.slug}/{filename}'
        return path

    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=get_upload_path)
    learning_link = models.URLField()
    description = models.TextField(help_text="A description of the tool that is only visible once the \"Read More\" button is clicked.")
    use_case = models.TextField(help_text="Should answer the prompt, \"You might use this tool if...\" and be written in the 2nd person.")
    categories = models.ManyToManyField(Category)
    EASE_OF_USE_CHOICES = [
        ('Simple', 'Simple'),
        ('Moderate', 'Moderate'),
        ('Advanced', 'Advanced'),
    ]
    ease_of_use = models.CharField(max_length=20, choices=EASE_OF_USE_CHOICES)
    PRICE_CHOICES = [
        ('free', 'Free or Free Tier Available'),
        ('facultyPays', 'Paid for by Faculty or Department'),
        ('stuentPays', 'Paid for by Student'),
        ('bothPay', 'Paid for by Both/Either'),
    ]
    price = models.CharField(max_length=20, choices=PRICE_CHOICES)
    website = models.URLField()
    slug = models.SlugField(max_length=50, unique=True, help_text="A short version of the title of the tool with no spaces used if a page is built for the tool, for example mainpage.com/[slug].")
    publish = models.BooleanField(default=False, help_text="Not yet functional.")

    def __str___(self):
        "Returns the name of the tool."
        return self.title

    class Meta:
        verbose_name = "Tool"
    
# TODO: Consider adding a file cleanup function for when screenshots are deleted from the admin interface
# https://timonweb.com/posts/cleanup-files-and-images-on-model-delete-in-django/
class Screenshot(models.Model):
    def get_upload_path(self, filename):
        path = f'./{self.tool.slug}/{filename}'
        return path

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)

