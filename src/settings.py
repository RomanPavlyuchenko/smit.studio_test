import os


TORTOISE_ORM = {
    'connections': {
        'default': os.environ.get("DATABASE_URL"),
    },
    'apps': {
        'models': {
            'models': ['aerich.models', 'rates.models'],
            'deault_connection': 'default',
        },
    },
}
