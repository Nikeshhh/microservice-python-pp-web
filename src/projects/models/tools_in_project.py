from django.db import models


class Tool(models.Model):
    tool_name = models.CharField(max_length=100)


class ToolsInProject(models.Model):
    tool = models.ForeignKey(to="Tool", on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    participants_needed = models.PositiveIntegerField(null=True, blank=True)
