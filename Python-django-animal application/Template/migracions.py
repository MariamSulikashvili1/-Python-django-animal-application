import django.db

class Migration(django.db.migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        django.db.migrations.DeleteModel('Tribble'),
        django.db.migrations.AddField('Animal', 'rating', django.db.models.IntegerField(default=0)),
    ]