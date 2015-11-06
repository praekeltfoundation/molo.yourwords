from wagtail.wagtailcore.models import Page


class competition(Page):
    name = Page.CharField(max_length=128)
    startDate = Page.DateTimeField(null=True, blank=True)
    endDate = Page.DateTimeField(null=True, blank=True)


class competition_entry(Page):
    story_name = Page.CharField(max_length=128)
    story_text = Page.TextField()
    TERMS_OR_CONDITIONS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    terms_or_conditions_approved = Page.CharField(
        choices=TERMS_OR_CONDITIONS_CHOICES)
    HIDE_REAL_NAME_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    hide_real_name = Page.charfield(choices=HIDE_REAL_NAME_CHOICES)
