[en](README_en.md)

# DjangoAutoModels
自動入力フィールドを備えたDjango用のAbstract Model群です。  
適応させたいモデルに継承させて使用します。

## 導入
1. ライブラリをインストールする。
    ```sh
    pip install django-auto-models
     or
    pip install git+https://github.com/taogya/DjangoAutoModels.git
    ```
1. `settings.py`に以下を追加する。
    ```python
    INSTALLED_APPS = [
        :
        'django_auto_models'
    ]
    ```
1. 継承したいModelを継承する。
    ```python
    # 例) 作成日時/更新日時を自動生成したい場合
    from django_auto_models.models import AutoTimestampModel

    class YourModel(AutoTimestampModel):
        :
    ```

    以下のように複数継承することもできます。
    ```python
    # 例) IDをBigAutoFieldと明示、作成日時/更新日時を自動生成したい場合
    from django_auto_models.models import AutoTimestampModel, AutoIDModel

    class YourModel(AutoIDModel, AutoTimestampModel):
        :
    ```
1. migrateを行う。
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

## Models
|カテゴリ|モデル名|カラム|フィールド|説明|
|---|---|---|---|---|
|datetime|AutoCreatedAtModel|created_at|DateTimeField|createした日時を格納|
|^       |AutoUpdateAtModel |updated_at|DateTimeField|create/updateした日時を格納|
|^       |AutoTimestampModel|created_at|DateTimeField|createした日時を格納|
|^       |^                 |updated_at|DateTimeField|create/updateした日時を格納|
|id|AutoIDModel   |id|AutoField    |integer の連番を格納<br>1 to 2,147,483,647<br>明示的にidがAutoFieldであると宣言|
|^ |AutoBigIDModel|id|AutoBigField |integer の連番を格納<br>1 to 9,223,372,036,854,775,807<br>明示的にidがAutoBigFieldであると宣言|
|^ |AutoUUIDModel |id|UUIDField    |ランダム128bit UUIDを格納<br>3×10^17回生成して1%の確率で重複の可能性|

## 補足
なし