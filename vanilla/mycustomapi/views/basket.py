from oscarapi.views import basic


class BasketList(basic.BasketList):
    """
    Overwrites default view in order to fix djangorestframework pagination
    """
    def get_queryset(self):
        qs = super(BasketList, self).get_queryset()
        return list(qs)
