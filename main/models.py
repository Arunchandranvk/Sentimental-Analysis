from django.db import models

# Create your models here.

class Header(models.Model):

    general_title = models.CharField('General Title', max_length=50)
    working_days = models.CharField('Working Days', max_length=30)
    phone = models.CharField('Phone Number', max_length=25)
    social1 = models.URLField('Social 1')
    social2 = models.URLField('Social 2')
    social3 = models.URLField('Social 3')
    social4 = models.URLField('Social 4')
    title = models.CharField('Title', max_length=30)
    path1 = models.CharField('Path 1', max_length=30)
    path2 = models.CharField('Path 2', max_length=30)
    path3 = models.CharField('Path 3', max_length=30)
    path4 = models.CharField('Path 4', max_length=30)
    path5 = models.CharField('Path 5', max_length=30)
    path6 = models.CharField('Path 6', max_length=30 ,null=True)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    background = models.ImageField('Background')
    subtitle = models.CharField('Subtitle', max_length=50)
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)
    button_link = models.CharField('Button Link', max_length=20)

    
    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self) -> str:
        return self.title
    
class Callback(models.Model):

    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)
    button_link = models.CharField('Button Link', max_length=20)
    
    class Meta:

        verbose_name = 'Callback'
        verbose_name_plural = 'Callback'

class Title(models.Model):

    title1 = models.CharField('Services Title', max_length=40)
    colored_title1 = models.CharField('Services Colored Title', max_length=40)
    subtitle1 = models.CharField('Services Subtitle', max_length=100)
    title2 = models.CharField('About Title', max_length=40)
    colored_title2 = models.CharField('About Colored Title', max_length=40)
    subtitle2 = models.CharField('About Subtitle', max_length=100)
    title3 = models.CharField('Testomonials Title', max_length=40)
    colored_title3 = models.CharField('Testomonials Colored Title', max_length=40)
    subtitle3 = models.CharField('Testomonials Subtitle', max_length=100)
    title4 = models.CharField('Contact Title', max_length=40)
    colored_title4 = models.CharField('Contact Colored Title', max_length=40)
    subtitle4 = models.CharField('Contact Subtitle', max_length=100)

class Service(models.Model):

    img = models.ImageField('Image')
    title = models.CharField('Title', max_length=40)
    text = models.TextField('Text')
    button = models.CharField('Button', max_length=30)

    def __str__(self) -> str:
        return self.title
    
class Info(models.Model):

    background = models.ImageField('Background')
    title = models.CharField('Contact Title', max_length=40)
    colored_title = models.CharField('Contact Colored Title', max_length=40)
    subtitle = models.CharField('Contact Subtitle', max_length=50,null=True, blank = True)
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    button = models.CharField('Button', max_length=30)

class Count(models.Model):

    num = models.IntegerField('Number')
    title = models.CharField('Title', max_length=30)

    def __str__(self) -> str:
        return f'{self.title} - {self.num}'
    
class About(models.Model):

    img = models.ImageField('Image')
    text1 = models.TextField('Text 1')
    text2 = models.TextField('Text 2')
    button = models.CharField('Button', max_length=30)
    button_link = models.URLField('Website Link')
        
    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class Testimonial(models.Model):

    name = models.CharField('Name', max_length=60)
    position = models.CharField('Position', max_length=60)
    text = models.TextField('Text')
    # img = models.ImageField('Image')
    Company = models.CharField('Company Name',max_length = 50 ,null=True)

    def __str__(self) -> str:
        return f'{self.name} ------- {self.position}'
    
class Contact(models.Model):

    username = models.CharField('Username', max_length=60)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=50)
    message = models.TextField('Message')

    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self) -> str:
        return f'{self.username} ------------ {self.subject}'
    
class Sponsor(models.Model):

    img = models.ImageField('Sponsor Logo')

class FooterContact(models.Model):

    footer_email = models.EmailField('Email')

    class Meta:

        verbose_name = 'Footer Contact'
        verbose_name_plural = 'Footer Contact'

    def __str__(self) -> str:
        return self.footer_email