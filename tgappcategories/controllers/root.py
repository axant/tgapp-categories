# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, predicates
from tg.i18n import ugettext as _

from tgappcategories import model
from tgext.pluggable import app_model, plug_url, plug_redirect

from tgappcategories.lib import forms

from bson.objectid import ObjectId

class RootController(TGController):
    allow_only = predicates.has_permission('tgappcategories')

    @expose('tgappcategories.templates.index')
    def index(self):
        categories = model.provider.query(model.Category)
        return dict(categories_count=categories[0],
                    categories=categories[1],
                    mount_point=self.mount_point,
                    )

    @expose('tgappcategories.templates.new_category')
    def new_category(self):
        return dict(form=forms.NewCategory,
                    mount_point=self.mount_point,
                    action=plug_url('tgappcategories', '/create_category'),
                    values=None,
                    )

    @expose()
    @validate(forms.NewCategory, error_handler=new_category)
    def create_category(self, **kwargs):
        dictionary = {
            'name': kwargs.get('name'),
            'description': kwargs.get('description'),
        }
        model.provider.create(model.Category, dictionary)

        flash(_('Category created.'))
        return redirect(url(self.mount_point))

    @expose('tgappcategories.templates.edit_category')
    def edit_category(self, category_id):
        category = model.Category.query.get(_id=ObjectId(category_id))
        return dict(form=forms.EditCategory,
                    mount_point=self.mount_point,
                    action=plug_url('tgappcategories', '/update_category/' + category_id),
                    values=category,
                    )

    @expose()
    def update_category(self, category_id, **kwargs):
        category = model.Category.query.get(_id=ObjectId(category_id))
        category.name = kwargs.get('name')
        category.description = kwargs.get('description')
        flash(_('Category updated.'))
        return redirect(url(self.mount_point))