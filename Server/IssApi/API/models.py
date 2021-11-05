from django.db import models

# Create your models here.


class Node(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    lastPing = models.DateTimeField(auto_now=True)
    IpAddress = models.TextField(primary_key=True)
    nickName = models.CharField(max_length=100)

    def __str__(self):
        return self.nickName


class File(models.Model):
    Node = models.ForeignKey(Node, on_delete=models.CASCADE)
    key = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastPing = models.DateTimeField(auto_now=True)
    fileName = models.CharField(max_length=100)
    filePath = models.CharField(max_length=200)

    def __str__(self):
        return self.fileName
