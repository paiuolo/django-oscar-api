# Solr
THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'

# Oscar
OSCAR_SHOP_NAME = 'vanilla'
OSCAR_SHOP_TAGLINE = ''
OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = False
DISPLAY_VERSION = False

OSCAR_DEFAULT_CURRENCY = 'EUR'
PAYMENT_CURRENCY = OSCAR_DEFAULT_CURRENCY
PAYMENT_INCLUDE_TAXES = True

OSCAR_ALLOW_ANON_REVIEWS = False

OSCAR_FROM_EMAIL ='admin@example.com'
OSCAR_HIDDEN_FEATURES = ['reviews']
#OSCAR_HOMEPAGE

# Order processing
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'

OSCAR_ORDER_STATUS_PIPELINE = OSCAR_LINE_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Payed', 'Shipped', 'Cancelled'),
    'Being processed': ('Payed', 'Shipped', 'Cancelled'),
    'Payed': ('Shipped', 'Refunded'),
    'Shipped': ('Refunded', ),
    'Refunded': (),
    'Cancelled': (),
}

OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Cancelled': 'Cancelled',
}
