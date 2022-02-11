from django.db import models

# Create your models here.
# DBの設定


class Profile(models.Model):
    # 各項目
    name = models.CharField('名前', max_length=100)
    # image = models.ImageField('イメージ',upload_to='profile')
    imgURL = models.CharField('画像のURL', max_length=255, null=True, blank=True)
    career = models.CharField('職業', max_length=55, null=True, blank=True)
    age = models.CharField('年齢', max_length=55, null=True, blank=True)
    github = models.URLField('GithubのURL', null=True, blank=True)
    introduction = models.TextField('自己紹介文')

    class Meta:  # テーブル名
        verbose_name_plural = 'プロフィール'


class Description(models.Model):

    text = models.CharField('本文', max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'スキルの概要'


class Skill(models.Model):

    name = models.CharField('名前', max_length=100)
    years = models.FloatField('経験年数', default=0)
    # 別テーブルとのリレーション（on_delete=models.CASCADEを設定すると、親側のデータを削除すると、結び付いた子側のデータも連動して削除）
    description = models.ForeignKey(
        Description, on_delete=models.SET_NULL, null=True, verbose_name='概要')

    def years_rounded(self):
        years = self.years
        if years.is_integer():
            years = int(years)
        return years

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'スキル'


class Work(models.Model):

    title = models.CharField('タイトル', max_length=100)
    # image = models.ImageField('イメージ',upload_to='works',null=True,blank=True)
    imgURL = models.CharField('画像のURL', max_length=255, null=True, blank=True)
    url = models.URLField('URL')
    published = models.DateField('公開日', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '作品'
