# Generated by Django 3.2.16 on 2022-12-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('academy_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lesson_category', models.CharField(max_length=50)),
                ('academy_address', models.CharField(max_length=200)),
                ('lesson_fee', models.BigIntegerField()),
                ('lesson_hours', models.BigIntegerField()),
            ],
            options={
                'db_table': 'academy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('bus_station_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sido', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoreCity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'core_city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoreCountry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'core_country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoPlotlyDashDashapp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('instance_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=110, unique=True)),
                ('base_state', models.TextField()),
                ('creation', models.DateTimeField()),
                ('update', models.DateTimeField()),
                ('save_on_change', models.IntegerField()),
            ],
            options={
                'db_table': 'django_plotly_dash_dashapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoPlotlyDashStatelessapp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=110, unique=True)),
            ],
            options={
                'db_table': 'django_plotly_dash_statelessapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EducationBudgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_code', models.IntegerField(blank=True, null=True)),
                ('budget_amount', models.BigIntegerField(blank=True, null=True)),
                ('code_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'education_budgets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HomeNotice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('article', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('hit', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'home_notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('building_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('building_address', models.CharField(max_length=50)),
                ('contract_date', models.DateField()),
                ('price', models.IntegerField()),
                ('building_area', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'real_estate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalesCustomers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=64)),
                ('site', models.CharField(blank=True, max_length=64, null=True)),
                ('team', models.CharField(blank=True, max_length=64, null=True)),
                ('position', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=11)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'sales_customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=30)),
                ('school_level', models.CharField(max_length=5)),
                ('students_number', models.IntegerField()),
                ('teachers_number', models.IntegerField()),
                ('students_per_class', models.DecimalField(decimal_places=1, max_digits=3)),
                ('school_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeoulInfo',
            fields=[
                ('gugun', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('population', models.IntegerField()),
                ('population_dentisy', models.IntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'seoul_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('subway_station_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sido', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subway',
                'managed': False,
            },
        ),
    ]
