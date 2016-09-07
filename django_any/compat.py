import django

if django.VERSION >= (1, 8):
    from django.utils.lorem_ipsum import paragraphs
else:
    from django.contrib.webdesign.lorem_ipsum import paragraphs


ipaddress_field_defined = django.VERSION < (1, 9)


def get_model_onetoone_fields(model):
    if django.VERSION >= (1, 8):
        return [
            (relation.name, relation)
            for relation in model._meta.get_fields()
            if relation.one_to_one and relation.auto_created
        ]
    else:
        # procceed reversed relations
        return [
            (relation.var_name, relation.field)
            for relation in model._meta.get_all_related_objects()
            if relation.field.unique # TODO and not relation.field.rel.parent_link ??
        ]


def get_model_private_fields(model):
    if django.VERSION >= (1, 10):
        return model._meta.private_fields
    else:
        return model._meta.virtual_fields


def get_remote_field(field):
    if django.VERSION >= (1, 9):
        return field.remote_field
    else:
        return field.rel


def get_remote_field_model(field):
    if django.VERSION >= (1, 9):
        return field.remote_field.model
    else:
        return field.rel.to
