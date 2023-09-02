[jp](README.md)

# DjangoAutoModels
A collection of Abstract Models for Django with autofill fields.  
Use it by inheriting it to the model you want to adapt.

## Introduction
1. Install the library.
    ```sh
    pip install django-auto-models
     or
    pip install git+https://github.com/taogya/DjangoAutoModels.git
    ```
1. Add the following to `settings.py`.
    ```python
    INSTALLED_APPS = [
        :
        'django_auto_models'
    ]
    ```
1. Inherit the Model you want to inherit.
    ```python
    # e.g. If you want to automatically generate the creation date/time/update date/time
    from django_auto_models.models import AutoTimestampModel

    class YourModel(AutoTimestampModel):
        :
    ```

    Multiple inheritance is possible as follows.
    ```python
    # e.g. If you want to specify the ID as BigAutoField and automatically generate the creation date/time/update date/time
    from django_auto_models.models import AutoTimestampModel, AutoIDModel

    class YourModel(AutoIDModel, AutoTimestampModel):
        :
    ```
1. do migrate.
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

## Models
|Category|Model Name|Column|Field|Description|
|---|---|---|---|---|
|datetime|AutoCreatedAtModel|created_at|DateTimeField|Stores created date and time|
|^ |AutoUpdateAtModel |updated_at|DateTimeField|Stores created/updated date and time|
|^ |AutoTimestampModel|created_at|DateTimeField|Stores created date and time|
|^ |^ |updated_at|DateTimeField|Stores created/updated date and time|
|id|AutoIDModel |id|AutoField |Stores integer sequential numbers<br>1 to 2,147,483,647<br>Explicitly declares id to be an AutoField|
|^ |AutoBigIDModel|id|AutoBigField |Stores integer sequential numbers<br>1 to 9,223,372,036,854,775,807<br>Explicitly declares id to be AutoBigField|
|^ |AutoUUIDModel |id|UUIDField |Stores random 128bit UUID<br>Generated 3×10^17 times, 1% chance of duplicate |

## Note
none