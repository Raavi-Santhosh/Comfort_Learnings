from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


class CourseCatalogue(models.Model):
    """
        This model is to store the course's category
    """
    category_name = models.CharField(max_length=100, unique=True, blank=False, null=False,
                                     verbose_name='Course Category', db_column='course_category')
    category_name_slug = models.SlugField(max_length=100, blank=True, null=True, editable=False)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
    modified_at = models.DateTimeField(auto_now=timezone.now)

    class Meta:
        verbose_name = 'Course Catalogue'
        verbose_name_plural = 'Course Catalogues'
        ordering = ['created_at', ]

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.category_name_slug = slugify(self.category_name)
        super(CourseCatalogue, self).save(*args, **kwargs)


class Courses(models.Model):
    """
        This model  is to store the courses with respective category using
        foreign key pointing to CourseCatalogue model
    """
    course_category = models.ForeignKey(CourseCatalogue, on_delete=models.CASCADE,
                                        related_name='courses')  # related_name is used to get reverse relationship
    course_name = models.CharField(max_length=100, unique=True, blank=False, null=False,
                                   verbose_name='Course Name', db_column='course_name')
    course_name_slug = models.SlugField(max_length=100, blank=True, null=True, editable=False)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.course_name_slug = slugify(self.course_name)
        super(Courses, self).save(*args, **kwargs)

    def get_course_url(self):
        """Creating to get dynamic urls for specific courses using reverse"""
        return reverse('courses:course', args=[self.course_category.category_name_slug,
                                               self.course_name_slug])

    def __str__(self):
        return '{} - {}'.format(self.course_name, self.course_category.category_name)

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ['created_at']


class CourseContentHeadings(models.Model):
    """
        This model is to store the course curriculum
    """
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,
                               related_name="course_content_heading")
    topic_name = models.CharField(max_length=700, blank=False,
                                  null=False, verbose_name='Topic Name')
    topic_name_slug = models.SlugField(max_length=700, editable=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'topic_name'], name='topic_unique_to_course')
        ]
        verbose_name = 'Course Content Heading'
        verbose_name_plural = 'Course Content Headings'

    def __str__(self):
        return '{} - {}'.format(self.topic_name, self.course.course_name)

    def save(self, *args, **kwargs):
        self.topic_name_slug = slugify(self.topic_name)
        super(CourseContentHeadings, self).save(*args, **kwargs)


class CourseContentVideos(models.Model):
    """
        This model is to store the course videos
    """
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_content_videos")
    course_heading = models.ForeignKey(CourseContentHeadings, on_delete=models.CASCADE,
                                       related_name="course_heading_videos")

    video_name = models.CharField(max_length=700, blank=False, null=False, )
    video_slug = models.SlugField(max_length=700, editable=False)
    video_link = models.CharField(max_length=250, null=True, blank=True, default='no-link')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    video_uid = models.UUIDField(editable=False, null=True, blank=True, default=uuid.uuid4, unique=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.video_name, self.course_heading.topic_name,
                                     self.course.course_name)

    def save(self, *args, **kwargs):
        self.video_slug = slugify(self.video_name)
        super(CourseContentVideos, self).save(*args, **kwargs)

    def get_video_url(self):
        cat = self.course.course_category.category_name_slug
        crs = self.course.course_name_slug
        link = self.video_uid
        return reverse('courses:course_videos', args=[cat, crs, link])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'course_heading', 'video_name'],
                                    name='course_video_unique_to_heading')
        ]
        verbose_name = 'Course Content Video'
        verbose_name_plural = 'Course Content Videos'
