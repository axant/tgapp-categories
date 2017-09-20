# -*- coding: utf-8 -*-
"""The tgapp-categories package"""

from tg.configuration import milestones


def plugme(app_config, options):
    from tgappcategories import model
    milestones.config_ready.register(model.configure_models)

    return dict(appid='tgappcategories', global_helpers=False)