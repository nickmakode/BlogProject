from .models import Product
class productDBRouter:
       def db_for_read (self, model, **kwargs):
          if (model == Product):
             return 'product'
          return None
       
       def db_for_write (self, model, **kwargs):
          if (model == Product):
             return 'product'
          return None

       def allow_migrate(self, db, app_label, model_name=None,model=None, **hints):
            # print(model_name,model)
            print(hints)
            if (model == Product):
               print(model_name,model)
               return True
            return None