# Generated by Django 4.0.5 on 2022-08-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restDFR", "0002_game_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="photo",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
    ]
