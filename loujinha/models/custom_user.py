from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
import re


class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    address = models.TextField(verbose_name='Address')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    
    def clean(self):
        super().clean()
        if not self._cpf_validation(self.cpf):
            raise ValidationError({'cpf': 'Invalid CPF format'})
        
    def _cpf_validation(self, cpf:str) ->bool:
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11 or cpf == cpf[0]*11:
            return False
        
        sum1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digit1 = (sum1 * 10 % 11) % 10
        
        sum2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digit2 = (sum2 * 10 % 11) % 10
        
        return cpf[-2:] == f"{digit1}{digit2}"

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
