from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def menu_link(context, url, text, icon):
    return template.Template("""<li><a class="nav-link" href="%s">%s
                    <span class="sub_icon fa %s"></span>
            </a></li>""" % (url, text, icon)).render(context)
