# Generated by Django 2.2.12 on 2020-05-11 07:22

from django.db import migrations


# Can't use fixtures because load_fixtures method is janky with django-tenant-schemas
def install_map_styles(apps, schema_editor):
    pass
    # create some decent styles for the quest maps (Cytoscapes) if they don't already exist
    # CytoStyleClass = apps.get_model('djcytoscape', 'CytoStyleClass')

    # link_hover_style, _ = CytoStyleClass.objects.get_or_create(
    #     name='link_hover',
    #     defaults={'styles': "'background-opacity': 1,\n'background-color': '#e5e5e5',"}
    # )

    # link_style, _ = CytoStyleClass.objects.get_or_create(
    #     name='link',
    #     defaults={'styles': "'color': '#2f70a8',\n'border-color': '#2f70a8',"}
    # )

    # Badge_style, _ = CytoStyleClass.objects.get_or_create(
    #     name='Badge',
    #     defaults={'styles': "'border-width': 3,"}
    # )

    # hidden_style, _ = CytoStyleClass.objects.get_or_create(
    #     name='hidden',
    #     defaults={'styles': "'opacity': 0,"}
    # )

    # CytoStyleSet = apps.get_model('djcytoscape', 'CytoStyleSet')

    # default_styleset, created = CytoStyleSet.objects.get_or_create(name="Default")

    # # style_classes = models.ManyToManyField(CytoStyleClass, blank=True)
    # if created:
    #     default_styleset.style_classes.add(link_hover_style)
    #     default_styleset.style_classes.add(link_style)
    #     default_styleset.style_classes.add(Badge_style)
    #     default_styleset.style_classes.add(hidden_style)


class Migration(migrations.Migration):

    dependencies = [
        ('djcytoscape', '0006_auto_20200511_1330'),
    ]

    operations = [
        migrations.RunPython(install_map_styles),
    ]
