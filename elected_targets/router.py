class ElectedTargetsRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'elected_targets':
            return 'congress'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'elected_targets':
            return 'congress'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
