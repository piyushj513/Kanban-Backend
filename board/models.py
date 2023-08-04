# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Board(models.Model):
    board_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    board_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    col = models.ForeignKey('Col', models.DO_NOTHING, blank=True, null=True)
    project_name = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    story_points = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    summary = models.TextField(blank=True, null=True)
    reporter = models.ForeignKey('User', models.DO_NOTHING, db_column='reporter', related_name='reporter_cards')
    assignee = models.ForeignKey('User', models.DO_NOTHING, db_column='assignee', related_name='assignee_cards')
    acceptance_criteria = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


    class Meta:
        managed = False
        db_table = 'card'


class Col(models.Model):
    col_id = models.IntegerField(primary_key=True)
    board = models.ForeignKey(Board, models.DO_NOTHING, blank=True, null=True)
    col_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'col'


class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    card = models.ForeignKey(Card, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    comment_desc = models.TextField(blank=True, null=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comments'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'user'
