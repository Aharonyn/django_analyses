from django.db import models
from django_analysis.models.input.definitions.input_definition import InputDefinition
from django_analysis.models.input.types.float_input import FloatInput
from django_analysis.models.input.definitions.input_definitions import InputDefinitions


class FloatInputDefinition(InputDefinition):
    min_value = models.FloatField(blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)
    default = models.FloatField(blank=True, null=True)

    INPUT_CLASS = FloatInput

    def get_input_type(self) -> InputDefinitions:
        return InputDefinitions.FLT
