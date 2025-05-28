# steps/template_step.py

from jinja2 import Template  # pip install jinja2
from steps.base import BaseStep
from dsl.models import MappingItem

class TemplateStep(BaseStep):
    def apply(self, item: MappingItem, context: dict):
        tmpl = Template(item.template)
        return tmpl.render(**context)