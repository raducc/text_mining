from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "author"


class Book(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author)
    slug = models.CharField(max_length=255)

    class Meta:
        db_table = "book"
        unique_together = ('author', 'name')


class BaseFeatures(models.Model):
    TYPE_COMA = 1
    TYPE_SEMICOLON = 2
    TYPE_QUOTATIO = 3
    TYPE_EXCLAMATIO = 4
    TYPE_HYPHEN = 5
    TYPE_AND = 6
    TYPE_BUT = 7
    TYPE_HOWEVER = 8
    TYPE_IF = 9
    TYPE_THAT = 10
    TYPE_MORE = 11
    TYPE_MUST = 12
    TYPE_MIGHT = 13
    TYPE_THIS = 14
    TYPE_VERY = 15
    TYPE_WORD_LENGTH = 16
    TYPE_SENTENCE_LENGTH = 17
    TYPE_STANDARD_DEVIATION_SENTENCE = 18

    TYPES = (
        (TYPE_COMA, 'Coma'),
        (TYPE_SEMICOLON, 'Semicolon'),
        (TYPE_QUOTATIO, 'Quotatio'),
        (TYPE_EXCLAMATIO, 'Exclamatio'),
        (TYPE_HYPHEN, 'Hyphen'),
        (TYPE_AND, 'And'),
        (TYPE_BUT, 'But'),
        (TYPE_HOWEVER, 'However'),
        (TYPE_IF, 'If'),
        (TYPE_THAT, 'That'),
        (TYPE_MORE, 'More'),
        (TYPE_MUST, 'Must'),
        (TYPE_MIGHT, 'Might'),
        (TYPE_THIS, 'This'),
        (TYPE_VERY, 'Very'),
        (TYPE_WORD_LENGTH, 'Mean Word Length'),
        (TYPE_SENTENCE_LENGTH, 'Mean Sentence Length'),
        (TYPE_STANDARD_DEVIATION_SENTENCE, 'Standard deviation of Sentence Length'),
    )
    feature_type = models.IntegerField(choices=TYPES)

    class Meta:
        abstract = True


class FeaturesCounts(BaseFeatures):

    book = models.ForeignKey(Book)
    values = models.CharField(max_length=255)

    class Meta:
        db_table = "feature_counts"


class AuthorFeatures(BaseFeatures):
    value = models.FloatField(default=0.0)

    class Meta:
        db_table = "author_features"
