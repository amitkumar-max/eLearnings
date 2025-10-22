from django import template

register = template.Library()

@register.filter
def file_contents(file_path):
    """Reads a text file and returns its content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return "Content not available."
