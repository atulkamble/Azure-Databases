DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analyticsdb',
        'USER': 'pgadmin',
        'PASSWORD': 'ChangeMe123!',
        'HOST': 'pgsql-demo.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}
