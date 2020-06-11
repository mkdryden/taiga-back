# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-25 12:29
from __future__ import unicode_literals

from django.db import migrations


UPDATE_ROLES_PERMISSIONS_SQL = """
    UPDATE users_role
    SET
        PERMISSIONS = array_append(PERMISSIONS, '{comment_permission}')
    WHERE
        '{base_permission}' = ANY(PERMISSIONS)
        AND
        NOT '{comment_permission}' = ANY(PERMISSIONS)
"""

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20160519_1058'),
    ]

    operations = [
        # user stories
        migrations.RunSQL(UPDATE_ROLES_PERMISSIONS_SQL.format(
            base_permission="modify_us",
            comment_permission="comment_us")
        ),

        # tasks
        migrations.RunSQL(UPDATE_ROLES_PERMISSIONS_SQL.format(
            base_permission="modify_task",
            comment_permission="comment_task")
        ),

        # issues
        migrations.RunSQL(UPDATE_ROLES_PERMISSIONS_SQL.format(
            base_permission="modify_issue",
            comment_permission="comment_issue")
        ),

        # wiki pages
        migrations.RunSQL(UPDATE_ROLES_PERMISSIONS_SQL.format(
            base_permission="modify_wiki_page",
            comment_permission="comment_wiki_page")
        )
    ]
