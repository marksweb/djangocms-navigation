# Generated by Django 3.2.10 on 2021-12-08 14:30

import django.db.models.deletion
from django.db import migrations, models

import cms.models.fields
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0023_auto_20211208_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationContainerModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='navigation_navigationcontainermodel', serialize=False, to='cms.cmsplugin')),
                ('name', models.CharField(blank=True, help_text='Optional name to help identify this plugin', max_length=255)),
                ('list_attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
            ],
            options={
                'verbose_name': 'Navigation container',
                'verbose_name_plural': 'Navigation containers',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='NavigationItemModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='navigation_navigationitemmodel', serialize=False, to='cms.cmsplugin')),
                ('link_external', models.URLField(blank=True)),
                ('link_label', models.CharField(blank=True, max_length=1024)),
                ('list_item_attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('link_attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('link_internal', cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cms.page')),
            ],
            options={
                'verbose_name': 'Navigation item',
                'verbose_name_plural': 'Navigation items',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
