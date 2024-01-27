from django.db import models
from seed.models import Seed
# Create your models here.
class Step(models.Model):
    img = models.ImageField(default='default_seed_pic.PNG', upload_to='step_pics')
    content = models.TextField()
    seed = models.ForeignKey("seed.Seed", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.seed.seedName} step'