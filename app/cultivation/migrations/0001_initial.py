# Generated by Django 3.2 on 2022-05-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('clean', models.IntegerField(verbose_name='清洁度')),
            ],
            options={
                'verbose_name_plural': '清洁度表',
                'db_table': 'pro_clean',
            },
        ),
        migrations.CreateModel(
            name='CultivationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '养殖信息表',
                'db_table': 'pro_cultivation_info',
            },
        ),
        migrations.CreateModel(
            name='EnvronmentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('temp', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='温度')),
                ('humi', models.CharField(max_length=20, verbose_name='湿度')),
                ('bug', models.CharField(max_length=20, verbose_name='蚊虫量')),
                ('excr', models.CharField(max_length=20, verbose_name='粪便量')),
            ],
            options={
                'verbose_name_plural': '环境信息表',
                'db_table': 'pro_envronment_info',
            },
        ),
        migrations.CreateModel(
            name='Fodder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=40, verbose_name='饲料名称')),
                ('factory', models.CharField(max_length=40, verbose_name='生产厂商')),
                ('license', models.CharField(max_length=40, verbose_name='批号')),
            ],
            options={
                'verbose_name_plural': '饲料表',
                'db_table': 'pro_fodder',
            },
        ),
        migrations.CreateModel(
            name='FodderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('use_num', models.FloatField(verbose_name='使用量')),
            ],
            options={
                'verbose_name_plural': '饲料信息表',
                'db_table': 'pro_fodder_info',
            },
        ),
        migrations.CreateModel(
            name='QuarantineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('qua_end', models.BooleanField(max_length=20, verbose_name='检疫结果')),
                ('qua_team', models.CharField(max_length=20, verbose_name='检疫部门')),
            ],
            options={
                'verbose_name_plural': '检疫信息表',
                'db_table': 'pro_quarantine_info',
            },
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('temp', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='温度')),
            ],
            options={
                'verbose_name_plural': '体温表',
                'db_table': 'pro_temp',
            },
        ),
        migrations.CreateModel(
            name='TurnInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('sla_name', models.CharField(max_length=20, verbose_name='屠宰场名称')),
                ('car_name', models.CharField(max_length=20, verbose_name='物流编号')),
            ],
            options={
                'verbose_name_plural': '转出信息表',
                'db_table': 'pro_turn_info',
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=40, verbose_name='疫苗名称')),
                ('factory', models.CharField(max_length=40, verbose_name='生产厂商')),
                ('license', models.CharField(max_length=40, verbose_name='批号')),
            ],
            options={
                'verbose_name_plural': '疫苗表',
                'db_table': 'pro_vaccine',
            },
        ),
        migrations.CreateModel(
            name='VaccineInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('use_num', models.IntegerField(verbose_name='注射')),
            ],
            options={
                'verbose_name_plural': '疫苗信息表',
                'db_table': 'pro_vaccine_info',
            },
        ),
    ]
