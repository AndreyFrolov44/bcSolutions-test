from django.db import models


class Block(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.IntegerField()
    hash = models.CharField(max_length=100)
    date = models.DateTimeField()
    miner = models.CharField(max_length=100)
    transaction = models.IntegerField()

    class Meta:
        db_table = 'block'
        ordering = ['-height']

    def __str__(self):
        return self.hash
