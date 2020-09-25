# Generated by Django 3.1.1 on 2020-09-25 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_column='course_category', max_length=100, unique=True, verbose_name='Course Category')),
                ('category_name_slug', models.SlugField(blank=True, editable=False, max_length=100, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Course Catalogue',
                'verbose_name_plural': 'Course Catalogues',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseContentHeadings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=700, unique=True, verbose_name='Topic Name')),
                ('topic_name_slug', models.SlugField(blank=True, editable=False, max_length=700, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Course Content Heading',
                'verbose_name_plural': 'Course Content Headings',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(db_column='course_name', max_length=100, unique=True, verbose_name='Course Name')),
                ('course_name_slug', models.SlugField(blank=True, editable=False, max_length=100, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('course_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.coursecatalogue')),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseContentVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=700)),
                ('video_slug', models.SlugField(editable=False, max_length=700)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_content_video', to='courses.courses')),
                ('course_heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_heading', to='courses.coursecontentheadings')),
            ],
            options={
                'verbose_name': 'Course Content Video',
                'verbose_name_plural': 'Course Content Videos',
            },
        ),
        migrations.AddField(
            model_name='coursecontentheadings',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_content_heading', to='courses.courses'),
        ),
        migrations.AddConstraint(
            model_name='coursecontentvideos',
            constraint=models.UniqueConstraint(fields=('course_heading', 'video_name'), name='course_video_unique_to_heading'),
        ),
        migrations.AddConstraint(
            model_name='coursecontentheadings',
            constraint=models.UniqueConstraint(fields=('course', 'topic_name'), name='topic_unique_to_course'),
        ),
    ]