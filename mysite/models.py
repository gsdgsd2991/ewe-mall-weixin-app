# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BasMallPermission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_code = models.CharField(db_column='ROLE_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resource_code = models.CharField(db_column='RESOURCE_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bas_mall_permission'


class BasMallResource(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    permission = models.CharField(db_column='PERMISSION', max_length=60, blank=True, null=True)  # Field name made lowercase.
    parent_code = models.CharField(db_column='PARENT_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    parent_name = models.CharField(db_column='PARENT_NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    is_menu = models.CharField(db_column='IS_MENU', max_length=20)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    sort_no = models.IntegerField(db_column='SORT_NO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bas_mall_resource'


class BasMallRole(models.Model):
    role_name = models.CharField(db_column='ROLE_NAME', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_code = models.CharField(db_column='ROLE_CODE', max_length=50)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bas_mall_role'


class BasMallUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login_name = models.CharField(db_column='LOGIN_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=200, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    id_card = models.CharField(db_column='ID_CARD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_place = models.CharField(db_column='BIRTH_PLACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    graduate_school = models.CharField(db_column='GRADUATE_SCHOOL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='MAJOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(db_column='EDUCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    join_years = models.CharField(db_column='JOIN_YEARS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    home_address = models.CharField(db_column='HOME_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    current_address = models.CharField(db_column='CURRENT_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    join_way = models.CharField(db_column='JOIN_WAY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contract_no = models.CharField(db_column='CONTRACT_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contract_limits = models.DateField(db_column='CONTRACT_LIMITS', blank=True, null=True)  # Field name made lowercase.
    is_insurance = models.IntegerField(db_column='IS_INSURANCE', blank=True, null=True)  # Field name made lowercase.
    insurance_date = models.DateField(db_column='INSURANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    renewal_date = models.DateField(db_column='RENEWAL_DATE', blank=True, null=True)  # Field name made lowercase.
    certificate = models.CharField(db_column='CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    quit_date = models.DateField(db_column='QUIT_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    org_id = models.IntegerField(db_column='ORG_ID', blank=True, null=True)  # Field name made lowercase.
    org_code = models.CharField(db_column='ORG_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='ORG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bas_mall_user'


class BasMallUserRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    role_code = models.CharField(db_column='ROLE_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bas_mall_user_role'


class EmallAddress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    is_default = models.IntegerField(db_column='IS_DEFAULT', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_address'


class EmallBilling(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bill_no = models.CharField(db_column='BILL_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    open_id = models.CharField(db_column='OPEN_ID', max_length=45)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT')  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_billing'


class EmallComment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    product_no = models.CharField(db_column='PRODUCT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_sku_id = models.IntegerField(db_column='PRODUCT_SKU_ID', blank=True, null=True)  # Field name made lowercase.
    author_id = models.IntegerField(db_column='AUTHOR_ID', blank=True, null=True)  # Field name made lowercase.
    author_name = models.CharField(db_column='AUTHOR_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author_profile = models.CharField(db_column='AUTHOR_PROFILE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='RATE', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    reply_customer_id = models.IntegerField(db_column='REPLY_CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    reply_customer_name = models.CharField(db_column='REPLY_CUSTOMER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_comment'


class EmallCustomerTag(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    tag_group_id = models.IntegerField(db_column='TAG_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name_cn = models.CharField(db_column='NAME_CN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(db_column='NAME_EN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_customer_tag'


class EmallCustomerTagGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_customer_tag_group'


class EmallDecoration(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_name = models.CharField(db_column='IMAGE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_decoration'


class EmallExcelDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    excel_list_id = models.IntegerField(db_column='EXCEL_LIST_ID', blank=True, null=True)  # Field name made lowercase.
    excel_cell = models.CharField(db_column='EXCEL_CELL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    table_column = models.CharField(db_column='TABLE_COLUMN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    excel_cell_num = models.IntegerField(db_column='EXCEL_CELL_NUM', blank=True, null=True)  # Field name made lowercase.
    data_type = models.CharField(db_column='DATA_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    not_null = models.IntegerField(db_column='NOT_NULL', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_excel_detail'


class EmallExcelList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    business_code = models.CharField(db_column='BUSINESS_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    business_desc = models.CharField(db_column='BUSINESS_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    business_type = models.CharField(db_column='BUSINESS_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sheet_name = models.CharField(db_column='SHEET_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    limits = models.IntegerField(db_column='LIMITS', blank=True, null=True)  # Field name made lowercase.
    from_field = models.CharField(db_column='FROM_', max_length=2000, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    where_field = models.CharField(db_column='WHERE_', max_length=2000, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    orderby_field = models.CharField(db_column='ORDERBY_', max_length=2000, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_excel_list'


class EmallFavorite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_favorite'


class EmallFollow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    follower_id = models.IntegerField(db_column='FOLLOWER_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_follow'


class EmallImageStore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sub_type = models.CharField(db_column='SUB_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ref_id = models.IntegerField(db_column='REF_ID', blank=True, null=True)  # Field name made lowercase.
    bucket = models.CharField(db_column='BUCKET', max_length=45, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_image_store'


class EmallInvoice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    invoice_type = models.CharField(db_column='INVOICE_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_invoice'


class EmallMatching(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_amount = models.FloatField(db_column='TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    actual_amount = models.FloatField(db_column='ACTUAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    preferences = models.CharField(db_column='PREFERENCES', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    praises = models.IntegerField(db_column='PRAISES', blank=True, null=True)  # Field name made lowercase.
    steps = models.IntegerField(db_column='STEPS', blank=True, null=True)  # Field name made lowercase.
    comments = models.IntegerField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    favorites = models.IntegerField(db_column='FAVORITES', blank=True, null=True)  # Field name made lowercase.
    likes = models.IntegerField(db_column='LIKES', blank=True, null=True)  # Field name made lowercase.
    gender_code = models.CharField(db_column='GENDER_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tone_code = models.CharField(db_column='TONE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    occasion_code = models.CharField(db_column='OCCASION_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    style_code = models.CharField(db_column='STYLE_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.
    sys_random_praises_num = models.IntegerField(db_column='SYS_RANDOM_PRAISES_NUM', blank=True, null=True)  # Field name made lowercase.
    sys_random_favorites_num = models.IntegerField(db_column='SYS_RANDOM_FAVORITES_NUM', blank=True, null=True)  # Field name made lowercase.
    sys_random_comments_num = models.IntegerField(db_column='SYS_RANDOM_COMMENTS_NUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_matching'


class EmallMatchingItem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    product_no = models.CharField(db_column='PRODUCT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    product_image_url = models.CharField(db_column='PRODUCT_IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='UNIT_PRICE', blank=True, null=True)  # Field name made lowercase.
    actual_price = models.FloatField(db_column='ACTUAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_matching_item'


class EmallOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_account = models.CharField(db_column='CUSTOMER_ACCOUNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address_id = models.IntegerField(db_column='ADDRESS_ID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    receiver = models.CharField(db_column='RECEIVER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_method = models.CharField(db_column='DELIVERY_METHOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    freight = models.CharField(db_column='FREIGHT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_time = models.DateTimeField(db_column='DELIVERY_TIME', blank=True, null=True)  # Field name made lowercase.
    express_code = models.CharField(db_column='EXPRESS_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    transaction_id = models.CharField(db_column='TRANSACTION_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    payment_channel = models.CharField(db_column='PAYMENT_CHANNEL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    total_amount = models.FloatField(db_column='TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment = models.FloatField(db_column='PAYMENT', blank=True, null=True)  # Field name made lowercase.
    actual_amount = models.FloatField(db_column='ACTUAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    invoice_type = models.CharField(db_column='INVOICE_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    invoice_id = models.IntegerField(db_column='INVOICE_ID', blank=True, null=True)  # Field name made lowercase.
    invoice_title = models.CharField(db_column='INVOICE_TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    invoice_content = models.CharField(db_column='INVOICE_CONTENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_status = models.CharField(db_column='DELIVERY_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    invoice_status = models.CharField(db_column='INVOICE_STATUS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    payment_time = models.DateTimeField(db_column='PAYMENT_TIME', blank=True, null=True)  # Field name made lowercase.
    close_reason = models.CharField(db_column='CLOSE_REASON', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_order'


class EmallOrderDeliver(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID')  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_account = models.CharField(db_column='CUSTOMER_ACCOUNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address_id = models.IntegerField(db_column='ADDRESS_ID', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_method = models.CharField(db_column='DELIVERY_METHOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_time = models.DateTimeField(db_column='DELIVERY_TIME', blank=True, null=True)  # Field name made lowercase.
    express_code = models.CharField(db_column='EXPRESS_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    delivery_reason = models.CharField(db_column='DELIVERY_REASON', max_length=45, blank=True, null=True)  # Field name made lowercase.
    freight = models.FloatField(db_column='FREIGHT', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    express_no = models.CharField(db_column='EXPRESS_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_order_deliver'


class EmallOrderItem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID')  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    product_no = models.CharField(db_column='PRODUCT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_sku_id = models.CharField(db_column='PRODUCT_SKU_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    size_code = models.CharField(db_column='SIZE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    color_code = models.CharField(db_column='COLOR_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(db_column='COUNT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unit_price = models.FloatField(db_column='UNIT_PRICE', blank=True, null=True)  # Field name made lowercase.
    total_price = models.FloatField(db_column='TOTAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    actual_price = models.FloatField(db_column='ACTUAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    total_actual_price = models.FloatField(db_column='TOTAL_ACTUAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    product_image_url = models.CharField(db_column='PRODUCT_IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_order_item'


class EmallPointBalance(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(db_column='POINT', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_point_balance'


class EmallPointSettlement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(db_column='POINT', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_point_settlement'


class EmallPointSpec(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    points_type = models.CharField(db_column='POINTS_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unit = models.IntegerField(db_column='UNIT')  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    conversion_rate = models.FloatField(db_column='CONVERSION_RATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_point_spec'


class EmallPraise(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    praise_type = models.IntegerField(db_column='PRAISE_TYPE')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_praise'


class EmallProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_no = models.CharField(db_column='PRODUCT_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sub_title = models.CharField(db_column='SUB_TITLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pants_code = models.CharField(db_column='PANTS_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gender_code = models.CharField(db_column='GENDER_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    product_type_code = models.CharField(db_column='PRODUCT_TYPE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    classification_code = models.CharField(db_column='CLASSIFICATION_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    model_code = models.CharField(db_column='MODEL_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tonal_code = models.CharField(db_column='TONAL_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fabric_code = models.CharField(db_column='FABRIC_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    limbs_code = models.CharField(db_column='LIMBS_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    size_offset_code = models.CharField(db_column='SIZE_OFFSET_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    collar_code = models.CharField(db_column='COLLAR_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    saturability_code = models.CharField(db_column='SATURABILITY_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    figure_code = models.CharField(db_column='FIGURE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    sale_price = models.FloatField(db_column='SALE_PRICE', blank=True, null=True)  # Field name made lowercase.
    purchase_price = models.FloatField(db_column='PURCHASE_PRICE', blank=True, null=True)  # Field name made lowercase.
    suitable_month = models.CharField(db_column='SUITABLE_MONTH', max_length=45, blank=True, null=True)  # Field name made lowercase.
    supply_link = models.CharField(db_column='SUPPLY_LINK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    putaway = models.IntegerField(db_column='PUTAWAY', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.
    provider_name = models.CharField(db_column='PROVIDER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    provider_id = models.IntegerField(db_column='PROVIDER_ID', blank=True, null=True)  # Field name made lowercase.
    provider_no = models.CharField(db_column='PROVIDER_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    buyer = models.IntegerField(db_column='BUYER', blank=True, null=True)  # Field name made lowercase.
    buyer_name = models.CharField(db_column='BUYER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product'


class EmallProductDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_detail'


class EmallProductFashion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_fashion'


class EmallProductFigure(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_figure'


class EmallProductImage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_image'


class EmallProductLength(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_length'


class EmallProductOccasion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_occasion'


class EmallProductSku(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    size_code = models.CharField(db_column='SIZE_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    color_code = models.CharField(db_column='COLOR_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    stock = models.CharField(db_column='STOCK', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_sku'


class EmallProductStyle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=45)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_product_style'


class EmallProvider(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    provider_no = models.CharField(db_column='PROVIDER_NO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WEBSITE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(db_column='NUMBER', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contact_name = models.CharField(db_column='CONTACT_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_provider'


class EmallWalletBalance(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    match_id = models.IntegerField(db_column='MATCH_ID', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emall_wallet_balance'


class HpActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=126, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=512, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='ISDELETED', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_activity'


class HpActivityAttend(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    real_name = models.CharField(db_column='REAL_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    activity_id = models.IntegerField(db_column='ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=126, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=512, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=126, blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_activity_attend'


class HpArticle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hp_article_title = models.CharField(db_column='HP_ARTICLE_TITLE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    hp_article_info = models.TextField(db_column='HP_ARTICLE_INFO', blank=True, null=True)  # Field name made lowercase.
    hp_article_img = models.CharField(db_column='HP_ARTICLE_IMG', max_length=256, blank=True, null=True)  # Field name made lowercase.
    hp_article_type = models.IntegerField(db_column='HP_ARTICLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    hp_article_browser = models.IntegerField(db_column='HP_ARTICLE_BROWSER', blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='IS_DELETED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_article'


class HpArticleComment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    article_id = models.IntegerField(db_column='ARTICLE_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_article_comment'


class HpCollect(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    article_id = models.IntegerField(db_column='ARTICLE_ID', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_collect'


class HpColumn(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hp_column_name = models.CharField(db_column='HP_COLUMN_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_column'


class HpGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_group'


class HpLesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    super_class_id = models.IntegerField(db_column='SUPER_CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    class_id = models.IntegerField(db_column='CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=126, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(db_column='TEACHER', max_length=126, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    count_price = models.FloatField(db_column='COUNT_PRICE', blank=True, null=True)  # Field name made lowercase.
    brief_info = models.CharField(db_column='BRIEF_INFO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    fit_for_person = models.CharField(db_column='FIT_FOR_PERSON', max_length=128, blank=True, null=True)  # Field name made lowercase.
    application = models.CharField(db_column='APPLICATION', max_length=512, blank=True, null=True)  # Field name made lowercase.
    teacher_info = models.CharField(db_column='TEACHER_INFO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    willnum = models.IntegerField(db_column='WILLNUM', blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.IntegerField(db_column='IS_DELETED', blank=True, null=True)  # Field name made lowercase.
    lesson_code = models.CharField(db_column='LESSON_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_lesson'


class HpLessonClass(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    superclass_id = models.IntegerField(db_column='SUPERCLASS_ID', blank=True, null=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='CLASS_NAME', max_length=126, blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    superclassname = models.CharField(db_column='superClassName', max_length=126, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_lesson_class'


class HpLessonPurchase(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    real_name = models.CharField(db_column='REAL_NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    hp_lesson_id = models.IntegerField(db_column='HP_LESSON_ID', blank=True, null=True)  # Field name made lowercase.
    super_class_id = models.IntegerField(db_column='SUPER_CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    class_id = models.IntegerField(db_column='CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=126, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(db_column='TEACHER', max_length=126, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    count_price = models.FloatField(db_column='COUNT_PRICE', blank=True, null=True)  # Field name made lowercase.
    brief_info = models.CharField(db_column='BRIEF_INFO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    fit_for_person = models.CharField(db_column='FIT_FOR_PERSON', max_length=128, blank=True, null=True)  # Field name made lowercase.
    application = models.CharField(db_column='APPLICATION', max_length=512, blank=True, null=True)  # Field name made lowercase.
    teacher_info = models.CharField(db_column='TEACHER_INFO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    willnum = models.IntegerField(db_column='WILLNUM', blank=True, null=True)  # Field name made lowercase.
    lesson_code = models.CharField(db_column='LESSON_CODE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_lesson_purchase'


class HpLessonSuperClass(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    super_class_name = models.CharField(db_column='SUPER_CLASS_NAME', max_length=126, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_lesson_super_class'


class HpMessage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=126, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=512, blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_message'


class HpRecruit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=128, blank=True, null=True)  # Field name made lowercase.
    company_logo = models.CharField(db_column='COMPANY_LOGO', max_length=256, blank=True, null=True)  # Field name made lowercase.
    company_tag = models.CharField(db_column='COMPANY_TAG', max_length=256, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=128, blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(db_column='SALARY', max_length=128, blank=True, null=True)  # Field name made lowercase.
    demand = models.CharField(db_column='DEMAND', max_length=512, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=512, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='ISDELETED', blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', max_length=125, blank=True, null=True)  # Field name made lowercase.
    company_info = models.CharField(db_column='COMPANY_INFO', max_length=125, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_recruit'


class HpResume(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recruit_id = models.IntegerField(db_column='RECRUIT_ID', blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='REALNAME', max_length=126, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    degree = models.CharField(db_column='DEGREE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(db_column='SCHOOL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    evaluation = models.TextField(db_column='EVALUATION', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_resume'


class HpUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    openid = models.CharField(db_column='OPENID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    subscribe = models.IntegerField(db_column='SUBSCRIBE', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='SEX', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=128, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=128, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='PROVINCE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='LANGUAGE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.CharField(db_column='HEADIMGURL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    subscribe_time = models.DateTimeField(db_column='SUBSCRIBE_TIME', blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=56, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='REALNAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GROUPID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID', blank=True, null=True)  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hp_user'


class TblAccount(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    recharge_total_amount = models.IntegerField(db_column='RECHARGE_TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    account_balance = models.IntegerField(db_column='ACCOUNT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    gift_total_amount = models.IntegerField(db_column='GIFT_TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    gift_balance = models.IntegerField(db_column='GIFT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    gift_expire_date = models.DateField(db_column='GIFT_EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_account'


class TblAccountConsumptionTransaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='ACCOUNT_ID', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    consume_date = models.DateTimeField(db_column='CONSUME_DATE', blank=True, null=True)  # Field name made lowercase.
    pre_account_balance = models.IntegerField(db_column='PRE_ACCOUNT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    consume_amount = models.IntegerField(db_column='CONSUME_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    account_balance = models.IntegerField(db_column='ACCOUNT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    consume_status = models.CharField(db_column='CONSUME_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pre_gift_balance = models.IntegerField(db_column='PRE_GIFT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    consume_gift = models.IntegerField(db_column='CONSUME_GIFT', blank=True, null=True)  # Field name made lowercase.
    gift_balance = models.IntegerField(db_column='GIFT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    trans_date = models.DateTimeField(db_column='TRANS_DATE', blank=True, null=True)  # Field name made lowercase.
    trans_status = models.CharField(db_column='TRANS_STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    total_consume_amount = models.IntegerField(db_column='TOTAL_CONSUME_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_account_consumption_transaction'


class TblAddress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='DISTRICT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    location_lat = models.FloatField(db_column='LOCATION_LAT', blank=True, null=True)  # Field name made lowercase.
    location_lng = models.FloatField(db_column='LOCATION_LNG', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_address'


class TblApplicationDesc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    desc = models.CharField(db_column='DESC', max_length=400, blank=True, null=True)  # Field name made lowercase.
    host_url = models.CharField(db_column='HOST_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_application_desc'


class TblApplyServiceEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    apply_date = models.DateTimeField(db_column='APPLY_DATE', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_apply_service_event'


class TblAttendanceStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    month = models.CharField(db_column='MONTH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    attendance_days = models.CharField(db_column='ATTENDANCE_DAYS', max_length=11, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_attendance_statistics'


class TblBonusPointEvent(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    bonus_point_type = models.CharField(db_column='BONUS_POINT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bonus_point = models.IntegerField(db_column='BONUS_POINT', blank=True, null=True)  # Field name made lowercase.
    bonus_date = models.DateField(db_column='BONUS_DATE', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    check_event_id = models.IntegerField(db_column='CHECK_EVENT_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_bonus_point_event'


class TblCancelServiceEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    cancel_date = models.DateTimeField(db_column='CANCEL_DATE', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cancel_service_event'


class TblCancelServiceStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    order_contact_name = models.CharField(db_column='ORDER_CONTACT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_contact_phone = models.CharField(db_column='ORDER_CONTACT_PHONE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    order_contact_address = models.CharField(db_column='ORDER_CONTACT_ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    order_service_item_name = models.CharField(db_column='ORDER_SERVICE_ITEM_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    order_service_item_number = models.CharField(db_column='ORDER_SERVICE_ITEM_NUMBER', max_length=5, blank=True, null=True)  # Field name made lowercase.
    order_amount = models.CharField(db_column='ORDER_AMOUNT', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cancel_date = models.DateField(db_column='CANCEL_DATE', blank=True, null=True)  # Field name made lowercase.
    order_payment_type = models.CharField(db_column='ORDER_PAYMENT_TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    technician_employee_no = models.CharField(db_column='TECHNICIAN_EMPLOYEE_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    technician_name = models.CharField(db_column='TECHNICIAN_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cancel_service_statistics'


class TblCaptcha(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(db_column='GENRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    captcha = models.CharField(db_column='CAPTCHA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    failure_date = models.DateTimeField(db_column='FAILURE_DATE', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    day_date = models.CharField(db_column='DAY_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_captcha'


class TblCertification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cert_type = models.CharField(db_column='CERT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cert_no = models.CharField(db_column='CERT_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE', blank=True, null=True)  # Field name made lowercase.
    effect_date = models.DateField(db_column='EFFECT_DATE', blank=True, null=True)  # Field name made lowercase.
    expire_date = models.DateField(db_column='EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_certification'


class TblCheckEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    check_date = models.DateField(db_column='CHECK_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_check_event'


class TblComment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    comment_level = models.IntegerField(db_column='COMMENT_LEVEL', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=400, blank=True, null=True)  # Field name made lowercase.
    comment_date = models.DateTimeField(db_column='COMMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    time_level = models.IntegerField(db_column='TIME_LEVEL', blank=True, null=True)  # Field name made lowercase.
    service_level = models.IntegerField(db_column='SERVICE_LEVEL', blank=True, null=True)  # Field name made lowercase.
    massage_level = models.IntegerField(db_column='MASSAGE_LEVEL', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_comment'


class TblCommission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    month = models.DateField(db_column='MONTH', blank=True, null=True)  # Field name made lowercase.
    commission_status = models.CharField(db_column='COMMISSION_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    last_stettle_date = models.DateField(db_column='LAST_STETTLE_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_commission'


class TblCommissionChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    change_type = models.CharField(db_column='CHANGE_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pre_specification = models.CharField(db_column='PRE_SPECIFICATION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    specification = models.CharField(db_column='SPECIFICATION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    specification_id = models.IntegerField(db_column='SPECIFICATION_ID', blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_commission_change_event'


class TblCommissionSpecification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    commission_rate = models.FloatField(db_column='COMMISSION_RATE', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_commission_specification'


class TblContact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    address_id = models.IntegerField(db_column='ADDRESS_ID', blank=True, null=True)  # Field name made lowercase.
    location_lat = models.FloatField(db_column='LOCATION_LAT', blank=True, null=True)  # Field name made lowercase.
    location_lng = models.FloatField(db_column='LOCATION_LNG', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_contact'


class TblCoupon(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_name = models.CharField(db_column='COUPON_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    effect_date = models.DateField(db_column='EFFECT_DATE', blank=True, null=True)  # Field name made lowercase.
    quit_date = models.DateField(db_column='QUIT_DATE', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    template_id = models.IntegerField(db_column='TEMPLATE_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    discount_type = models.CharField(db_column='DISCOUNT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_type = models.CharField(db_column='SERVICE_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    service_subtype = models.CharField(db_column='SERVICE_SUBTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_specification_id = models.IntegerField(db_column='SERVICE_SPECIFICATION_ID', blank=True, null=True)  # Field name made lowercase.
    discount_rate = models.FloatField(db_column='DISCOUNT_RATE', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=10)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_coupon'


class TblCouponTemplate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    template_type = models.CharField(db_column='TEMPLATE_TYPE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    coupon_name = models.CharField(db_column='COUPON_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    limit_value = models.IntegerField(db_column='LIMIT_VALUE', blank=True, null=True)  # Field name made lowercase.
    discount_type = models.CharField(db_column='DISCOUNT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    discount_rate = models.FloatField(db_column='DISCOUNT_RATE', blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    desc_txt = models.CharField(db_column='DESC_TXT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    limit_date = models.IntegerField(db_column='LIMIT_DATE', blank=True, null=True)  # Field name made lowercase.
    service_type = models.CharField(db_column='SERVICE_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    service_subtype = models.CharField(db_column='SERVICE_SUBTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    auto_send = models.IntegerField(db_column='AUTO_SEND', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_specification_id = models.IntegerField(db_column='SERVICE_SPECIFICATION_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_coupon_template'


class TblCustomer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_no = models.CharField(db_column='CUSTOMER_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    money = models.FloatField(db_column='MONEY', blank=True, null=True)  # Field name made lowercase.
    bonus_point = models.IntegerField(db_column='BONUS_POINT', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    channel_source = models.CharField(db_column='CHANNEL_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    market_activity_source = models.CharField(db_column='MARKET_ACTIVITY_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    weixin_open_id = models.CharField(db_column='WEIXIN_OPEN_ID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subscribe = models.IntegerField(db_column='SUBSCRIBE', blank=True, null=True)  # Field name made lowercase.
    subscribe_time = models.DateTimeField(db_column='SUBSCRIBE_TIME', blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateTimeField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customer_type = models.CharField(db_column='CUSTOMER_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_customer'


class TblCustomerContactPointStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    latest_consume_date = models.DateTimeField(db_column='LATEST_CONSUME_DATE', blank=True, null=True)  # Field name made lowercase.
    latest_telephone_follow_up_date = models.DateTimeField(db_column='LATEST_TELEPHONE_FOLLOW_UP_DATE', blank=True, null=True)  # Field name made lowercase.
    latest_telephone_follow_up_content = models.TextField(db_column='LATEST_TELEPHONE_FOLLOW_UP_CONTENT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_customer_contact_point_statistics'


class TblCustomerShape(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    customization_person_name = models.CharField(max_length=40, blank=True, null=True)
    weixin_open_id = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    body_shape = models.CharField(max_length=40, blank=True, null=True)
    face_shape = models.CharField(max_length=40, blank=True, null=True)
    face_color = models.CharField(max_length=40, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    isoneself = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    last_modified_id = models.IntegerField(blank=True, null=True)
    mark_for_delete = models.IntegerField(blank=True, null=True)
    opt_counter = models.IntegerField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_customer_shape'

class TblCustomerMatchHistory(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)
    customer_id = models.IntegerField(db_column='CUSTOMER_ID',blank=TRUE,null=TRUE)
    customization_person_name = models.CharField(max_length=40,blank=True,null=True)
    weixin_open_id=models.IntegerField(blank=True,null=True)
    match_id = models.IntegerField(blank=True,null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    last_modified_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed=True
        db_table='tbl_customer_match_history'


class TblCustomerStatistics(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    contact_point_id = models.IntegerField(db_column='CONTACT_POINT_ID', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_amount = models.BigIntegerField(db_column='PAYMENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    use_coupon_no = models.IntegerField(db_column='USE_COUPON_NO', blank=True, null=True)  # Field name made lowercase.
    unused_coupon_no = models.IntegerField(db_column='UNUSED_COUPON_NO', blank=True, null=True)  # Field name made lowercase.
    consume_discount_amount = models.BigIntegerField(db_column='CONSUME_DISCOUNT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    unconsumed_discount_amount = models.BigIntegerField(db_column='UNCONSUMED_DISCOUNT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_customer_statistics'


class TblDispatchCouponEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    target_customers = models.TextField(db_column='TARGET_CUSTOMERS', blank=True, null=True)  # Field name made lowercase.
    dispatch_type = models.CharField(db_column='DISPATCH_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    coupon_id = models.IntegerField(db_column='COUPON_ID', blank=True, null=True)  # Field name made lowercase.
    dispatch_date = models.DateField(db_column='DISPATCH_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_dispatch_coupon_event'


class TblEmployee(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(db_column='PID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='ABBREVIATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quit_date = models.DateField(db_column='QUIT_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_employee'


class TblImCodeList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    parent_code = models.CharField(db_column='PARENT_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name_cn = models.CharField(db_column='NAME_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(db_column='NAME_EN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sort_no = models.IntegerField(db_column='SORT_NO', blank=True, null=True)  # Field name made lowercase.
    selected = models.IntegerField(db_column='SELECTED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_im_code_list'


class TblImCodeType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name_cn = models.CharField(db_column='NAME_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name_en = models.CharField(db_column='NAME_EN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_im_code_type'


class TblMarketActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    weixin_qr_code_url = models.CharField(db_column='WEIXIN_QR_CODE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    weixin_qr_code_image_url = models.CharField(db_column='WEIXIN_QR_CODE_IMAGE_URL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_market_activity'


class TblMessage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    message = models.CharField(db_column='MESSAGE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    send_date = models.DateTimeField(db_column='SEND_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    plan_send_time = models.DateTimeField(db_column='PLAN_SEND_TIME', blank=True, null=True)  # Field name made lowercase.
    message_type = models.CharField(db_column='MESSAGE_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    target_no = models.IntegerField(db_column='TARGET_NO', blank=True, null=True)  # Field name made lowercase.
    send_type = models.CharField(db_column='SEND_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    message_target_id = models.IntegerField(db_column='MESSAGE_TARGET_ID', blank=True, null=True)  # Field name made lowercase.
    target_type = models.CharField(db_column='TARGET_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(db_column='EMPLOYEE_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_message'


class TblMessageRecord(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    message_id = models.CharField(db_column='MESSAGE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    message_type = models.CharField(db_column='MESSAGE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    business_name = models.CharField(db_column='BUSINESS_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    request = models.CharField(db_column='REQUEST', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='RESPONSE', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    receive = models.CharField(db_column='RECEIVE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_message_record'


class TblMessageTarget(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    target = models.TextField(db_column='TARGET', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_message_target'


class TblMobileAccessKey(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    access_key = models.CharField(db_column='ACCESS_KEY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_mobile_access_key'


class TblMobileValidatorCode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    validator_code = models.CharField(db_column='VALIDATOR_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    effect_date = models.DateTimeField(db_column='EFFECT_DATE', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_mobile_validator_code'


class TblOperationMonthlyStatement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='MONTH', max_length=2, blank=True, null=True)  # Field name made lowercase.
    operation_month = models.DateField(db_column='OPERATION_MONTH', blank=True, null=True)  # Field name made lowercase.
    sales_amount = models.BigIntegerField(db_column='SALES_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    new_customer_no = models.IntegerField(db_column='NEW_CUSTOMER_NO', blank=True, null=True)  # Field name made lowercase.
    bonus_point = models.BigIntegerField(db_column='BONUS_POINT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_operation_monthly_statement'


class TblOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    order_type = models.CharField(db_column='ORDER_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_status = models.CharField(db_column='SERVICE_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    coupon_id = models.IntegerField(db_column='COUPON_ID', blank=True, null=True)  # Field name made lowercase.
    coupon_discount = models.IntegerField(db_column='COUPON_DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    actual_amount = models.IntegerField(db_column='ACTUAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    service_time = models.IntegerField(db_column='SERVICE_TIME', blank=True, null=True)  # Field name made lowercase.
    contact_id = models.IntegerField(db_column='CONTACT_ID', blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    end_time = models.DateTimeField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    success_payment_transaction_id = models.IntegerField(db_column='SUCCESS_PAYMENT_TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    refund_transaction_id = models.IntegerField(db_column='REFUND_TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    take_flag = models.CharField(db_column='TAKE_FLAG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    comment_id = models.IntegerField(db_column='COMMENT_ID', blank=True, null=True)  # Field name made lowercase.
    consumption_transaction_id = models.IntegerField(db_column='CONSUMPTION_TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    use_account_amount = models.IntegerField(db_column='USE_ACCOUNT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    consume_account_amount = models.IntegerField(db_column='CONSUME_ACCOUNT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='ORDER_DATE', blank=True, null=True)  # Field name made lowercase.
    leave_message = models.CharField(db_column='LEAVE_MESSAGE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    payment_channel = models.CharField(db_column='PAYMENT_CHANNEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_item_code = models.CharField(db_column='SERVICE_ITEM_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_item_name = models.CharField(db_column='SERVICE_ITEM_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_item_number = models.IntegerField(db_column='SERVICE_ITEM_NUMBER', blank=True, null=True)  # Field name made lowercase.
    canceled_date = models.DateTimeField(db_column='CANCELED_DATE', blank=True, null=True)  # Field name made lowercase.
    finished_date = models.DateTimeField(db_column='FINISHED_DATE', blank=True, null=True)  # Field name made lowercase.
    technician_finished_service_time = models.DateTimeField(db_column='TECHNICIAN_FINISHED_SERVICE_TIME', blank=True, null=True)  # Field name made lowercase.
    technician_finished_service_status = models.CharField(db_column='TECHNICIAN_FINISHED_SERVICE_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    order_source = models.CharField(db_column='ORDER_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_order'


class TblOrderHelpEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    contact_id = models.IntegerField(db_column='CONTACT_ID', blank=True, null=True)  # Field name made lowercase.
    help_time = models.DateTimeField(db_column='HELP_TIME', blank=True, null=True)  # Field name made lowercase.
    contact_phone = models.CharField(db_column='CONTACT_PHONE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contact_address = models.CharField(db_column='CONTACT_ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    valid = models.IntegerField(db_column='VALID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_order_help_event'


class TblOrderStatusChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    pre_order_status = models.CharField(db_column='PRE_ORDER_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    change_source = models.CharField(db_column='CHANGE_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_order_status_change_event'


class TblOrderTechnicianChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    pre_technician_id = models.IntegerField(db_column='PRE_TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_order_technician_change_event'


class TblPaymentDesc(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payment_desc'


class TblPaymentSpecification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    channel = models.CharField(db_column='CHANNEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_desc_id = models.IntegerField(db_column='PAYMENT_DESC_ID', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=500)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payment_specification'


class TblPaymentTransaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    trans_status = models.CharField(db_column='TRANS_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    trans_date = models.DateTimeField(db_column='TRANS_DATE', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    order_amount = models.IntegerField(db_column='ORDER_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment_channel = models.CharField(db_column='PAYMENT_CHANNEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment_no = models.CharField(db_column='PAYMENT_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='PAYMENT_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_date = models.DateTimeField(db_column='PAYMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    success_date = models.DateTimeField(db_column='SUCCESS_DATE', blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(db_column='TRANS_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payment_transaction'


class TblPermission(models.Model):
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    resource_id = models.IntegerField(db_column='RESOURCE_ID')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_permission'


class TblPointsSpec(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    points_type = models.CharField(db_column='POINTS_TYPE', max_length=20)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE')  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_points_spec'


class TblRechargeActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    recharge_amount = models.IntegerField(db_column='RECHARGE_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    gift_amount = models.IntegerField(db_column='GIFT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    valid_day = models.IntegerField(db_column='VALID_DAY', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    enabled = models.CharField(db_column='ENABLED', max_length=11, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_recharge_activity'


class TblRechargeOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='ACCOUNT_ID', blank=True, null=True)  # Field name made lowercase.
    recharge_date = models.DateTimeField(db_column='RECHARGE_DATE', blank=True, null=True)  # Field name made lowercase.
    pre_account_balance = models.IntegerField(db_column='PRE_ACCOUNT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    recharge_amount = models.IntegerField(db_column='RECHARGE_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    account_balance = models.IntegerField(db_column='ACCOUNT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    payment_transaction_id = models.IntegerField(db_column='PAYMENT_TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    payment_channel = models.CharField(db_column='PAYMENT_CHANNEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    payment_type = models.CharField(db_column='PAYMENT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recharge_status = models.CharField(db_column='RECHARGE_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    trans_status = models.CharField(db_column='TRANS_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    trans_date = models.DateTimeField(db_column='TRANS_DATE', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    gift_amount = models.IntegerField(db_column='GIFT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    pre_gift_balance = models.IntegerField(db_column='PRE_GIFT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    gift_balance = models.IntegerField(db_column='GIFT_BALANCE', blank=True, null=True)  # Field name made lowercase.
    valid_day = models.IntegerField(db_column='VALID_DAY', blank=True, null=True)  # Field name made lowercase.
    pre_gift_expire_date = models.DateField(db_column='PRE_GIFT_EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    gift_expire_date = models.DateField(db_column='GIFT_EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    recharge_activity_id = models.IntegerField(db_column='RECHARGE_ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_recharge_order'


class TblRefundTransaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    payment_transaction_id = models.IntegerField(db_column='PAYMENT_TRANSACTION_ID', blank=True, null=True)  # Field name made lowercase.
    payment_amount = models.IntegerField(db_column='PAYMENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    refund_amount = models.IntegerField(db_column='REFUND_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    refund_date = models.DateTimeField(db_column='REFUND_DATE', blank=True, null=True)  # Field name made lowercase.
    refund_status = models.CharField(db_column='REFUND_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    trans_status = models.CharField(db_column='TRANS_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    trans_date = models.DateTimeField(db_column='TRANS_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_refund_transaction'


class TblResource(models.Model):
    resource_code = models.CharField(db_column='RESOURCE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resource_name = models.CharField(db_column='RESOURCE_NAME', max_length=50)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    permission = models.CharField(db_column='PERMISSION', max_length=60, blank=True, null=True)  # Field name made lowercase.
    parent_resource_code = models.CharField(db_column='PARENT_RESOURCE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_resource'


class TblRole(models.Model):
    role_name = models.CharField(db_column='ROLE_NAME', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_role'


class TblSalesStatement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    statement_type = models.CharField(db_column='STATEMENT_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sales_year = models.CharField(db_column='SALES_YEAR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sales_month = models.CharField(db_column='SALES_MONTH', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sales_date = models.DateField(db_column='SALES_DATE', blank=True, null=True)  # Field name made lowercase.
    sales_amount = models.BigIntegerField(db_column='SALES_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment_amount = models.BigIntegerField(db_column='PAYMENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sales_statement'


class TblServiceCalendar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_calendar'


class TblServiceDate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service_calendar_id = models.IntegerField(db_column='SERVICE_CALENDAR_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    service_time = models.CharField(db_column='SERVICE_TIME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    work_time = models.CharField(db_column='WORK_TIME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_date'


class TblServiceDesc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    service_comment = models.TextField(db_column='SERVICE_COMMENT', blank=True, null=True)  # Field name made lowercase.
    service_desc = models.TextField(db_column='SERVICE_DESC', blank=True, null=True)  # Field name made lowercase.
    service_content = models.TextField(db_column='SERVICE_CONTENT', blank=True, null=True)  # Field name made lowercase.
    appointment = models.TextField(db_column='APPOINTMENT', blank=True, null=True)  # Field name made lowercase.
    taboo = models.TextField(db_column='TABOO', blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='POSITION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(db_column='DISEASE', max_length=400, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_desc'


class TblServiceItem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    specification_id = models.IntegerField(db_column='SPECIFICATION_ID', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='NUMBER', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    total_price = models.IntegerField(db_column='TOTAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    service_time = models.IntegerField(db_column='SERVICE_TIME', blank=True, null=True)  # Field name made lowercase.
    total_service_time = models.IntegerField(db_column='TOTAL_SERVICE_TIME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_item'


class TblServiceItemSalesStatement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    spec_id = models.IntegerField(db_column='SPEC_ID', blank=True, null=True)  # Field name made lowercase.
    service_type = models.CharField(db_column='SERVICE_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_type_name = models.CharField(db_column='SERVICE_TYPE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_subtype = models.CharField(db_column='SERVICE_SUBTYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_subtype_name = models.CharField(db_column='SERVICE_SUBTYPE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_code = models.CharField(db_column='SERVICE_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    sales_amount = models.BigIntegerField(db_column='SALES_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    payment_amount = models.BigIntegerField(db_column='PAYMENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    sales_statement_id = models.IntegerField(db_column='SALES_STATEMENT_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_item_sales_statement'


class TblServiceSaleStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    finish_date = models.DateTimeField(db_column='FINISH_DATE', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payment_no = models.CharField(db_column='PAYMENT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type_code = models.CharField(db_column='TYPE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type_code_name = models.CharField(db_column='TYPE_CODE_NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    code_list = models.CharField(db_column='CODE_LIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    code_list_name = models.CharField(db_column='CODE_LIST_NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    service_item = models.CharField(db_column='SERVICE_ITEM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    service_item_name = models.CharField(db_column='SERVICE_ITEM_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    total_count = models.IntegerField(db_column='TOTAL_COUNT', blank=True, null=True)  # Field name made lowercase.
    total_amount = models.IntegerField(db_column='TOTAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    coupon_count = models.IntegerField(db_column='COUPON_COUNT', blank=True, null=True)  # Field name made lowercase.
    sales_actual_amount = models.IntegerField(db_column='SALES_ACTUAL_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_sale_statistics'


class TblServiceSpecification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_code = models.CharField(db_column='SERVICE_CODE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_time = models.IntegerField(db_column='SERVICE_TIME', blank=True, null=True)  # Field name made lowercase.
    service_type = models.CharField(db_column='SERVICE_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_type_name = models.CharField(db_column='SERVICE_TYPE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service_subtype = models.CharField(db_column='SERVICE_SUBTYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    service_subtype_name = models.CharField(db_column='SERVICE_SUBTYPE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    service_desc_id = models.IntegerField(db_column='SERVICE_DESC_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    stop_date = models.DateTimeField(db_column='STOP_DATE', blank=True, null=True)  # Field name made lowercase.
    enable = models.IntegerField(db_column='ENABLE', blank=True, null=True)  # Field name made lowercase.
    service_region = models.CharField(db_column='SERVICE_REGION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lower_limit = models.IntegerField(db_column='LOWER_LIMIT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_specification'


class TblServiceStatusChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    pre_status = models.CharField(db_column='PRE_STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    change_source = models.CharField(db_column='CHANGE_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_status_change_event'


class TblServiceTimeChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    change_source = models.CharField(db_column='CHANGE_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    pre_service_time = models.CharField(db_column='PRE_SERVICE_TIME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    service_time = models.CharField(db_column='SERVICE_TIME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_service_time_change_event'


class TblSettlement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    commission_id = models.IntegerField(db_column='COMMISSION_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    commission_type = models.CharField(db_column='COMMISSION_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    commission_rate = models.FloatField(db_column='COMMISSION_RATE', blank=True, null=True)  # Field name made lowercase.
    commission_amount = models.IntegerField(db_column='COMMISSION_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    finished_date = models.DateTimeField(db_column='FINISHED_DATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_settlement'


class TblSmsConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sms_type = models.CharField(db_column='SMS_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sms_url = models.CharField(db_column='SMS_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    api_key = models.CharField(db_column='API_KEY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='COUNT', blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='TIME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sms_config'


class TblTechnician(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(db_column='PID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='ABBREVIATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    stars = models.IntegerField(db_column='STARS', blank=True, null=True)  # Field name made lowercase.
    service_region = models.CharField(db_column='SERVICE_REGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=400, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quit_date = models.DateField(db_column='QUIT_DATE', blank=True, null=True)  # Field name made lowercase.
    technician_desc_id = models.IntegerField(db_column='TECHNICIAN_DESC_ID', blank=True, null=True)  # Field name made lowercase.
    enabled = models.IntegerField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=400, blank=True, null=True)  # Field name made lowercase.
    weixin_open_id = models.CharField(db_column='WEIXIN_OPEN_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comment_no = models.IntegerField(db_column='COMMENT_NO', blank=True, null=True)  # Field name made lowercase.
    positive_comment_no = models.IntegerField(db_column='POSITIVE_COMMENT_NO', blank=True, null=True)  # Field name made lowercase.
    neutral_comment_no = models.IntegerField(db_column='NEUTRAL_COMMENT_NO', blank=True, null=True)  # Field name made lowercase.
    negative_comment_no = models.IntegerField(db_column='NEGATIVE_COMMENT_NO', blank=True, null=True)  # Field name made lowercase.
    sort = models.IntegerField(db_column='SORT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician'


class TblTechnicianDesc(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=400, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician_desc'


class TblTechnicianLevelChangeEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    pre_level = models.CharField(db_column='PRE_LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    change_source = models.CharField(db_column='CHANGE_SOURCE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician_level_change_event'


class TblTechnicianSalesDetailStatement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sales_statement_id = models.IntegerField(db_column='SALES_STATEMENT_ID', blank=True, null=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='LEVEL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    auto_dispatch_no = models.IntegerField(db_column='AUTO_DISPATCH_NO', blank=True, null=True)  # Field name made lowercase.
    cust_select_no = models.IntegerField(db_column='CUST_SELECT_NO', blank=True, null=True)  # Field name made lowercase.
    service_order_no = models.IntegerField(db_column='SERVICE_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    payment_amount = models.BigIntegerField(db_column='PAYMENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    sales_amount = models.BigIntegerField(db_column='SALES_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    commission_rate = models.FloatField(db_column='COMMISSION_RATE', blank=True, null=True)  # Field name made lowercase.
    commission = models.BigIntegerField(db_column='COMMISSION', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician_sales_detail_statement'


class TblTechnicianSalesStatement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    technician_employee_no = models.CharField(db_column='TECHNICIAN_EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    technician_name = models.CharField(db_column='TECHNICIAN_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    technician_level = models.CharField(db_column='TECHNICIAN_LEVEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    finish_order_count = models.IntegerField(db_column='FINISH_ORDER_COUNT', blank=True, null=True)  # Field name made lowercase.
    finish_order_amount = models.IntegerField(db_column='FINISH_ORDER_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician_sales_statement'


class TblTechnicianService(models.Model):
    technician_id = models.IntegerField(db_column='TECHNICIAN_ID', blank=True, null=True)  # Field name made lowercase.
    service_spec_id = models.IntegerField(db_column='SERVICE_SPEC_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_technician_service'


class TblTelephoneFollowUp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    operator_id = models.IntegerField(db_column='OPERATOR_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_telephone_follow_up'


class TblUseCouponEvent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_id = models.IntegerField(db_column='COUPON_ID', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    优惠券使用的日期 = models.DateField(blank=True, null=True)
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_use_coupon_event'


class TblUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login_name = models.CharField(db_column='LOGIN_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=40, blank=True, null=True)  # Field name made lowercase.
    employee_no = models.CharField(db_column='EMPLOYEE_NO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    job_type = models.CharField(db_column='JOB_TYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=200, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    id_card = models.CharField(db_column='ID_CARD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nation = models.CharField(db_column='NATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birth_place = models.CharField(db_column='BIRTH_PLACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    graduate_school = models.CharField(db_column='GRADUATE_SCHOOL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    major = models.CharField(db_column='MAJOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(db_column='EDUCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    join_years = models.CharField(db_column='JOIN_YEARS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    home_address = models.CharField(db_column='HOME_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    current_address = models.CharField(db_column='CURRENT_ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    join_way = models.CharField(db_column='JOIN_WAY', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contract_no = models.CharField(db_column='CONTRACT_NO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contract_limits = models.DateField(db_column='CONTRACT_LIMITS', blank=True, null=True)  # Field name made lowercase.
    is_insurance = models.IntegerField(db_column='IS_INSURANCE', blank=True, null=True)  # Field name made lowercase.
    insurance_date = models.DateField(db_column='INSURANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    renewal_date = models.DateField(db_column='RENEWAL_DATE', blank=True, null=True)  # Field name made lowercase.
    certificate = models.CharField(db_column='CERTIFICATE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateField(db_column='JOIN_DATE', blank=True, null=True)  # Field name made lowercase.
    quit_date = models.DateField(db_column='QUIT_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    opt_counter_copy1 = models.IntegerField(db_column='OPT_COUNTER_copy1', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblUserRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_user_role'


class TblWeixinConfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    config_type = models.CharField(db_column='CONFIG_TYPE', max_length=20)  # Field name made lowercase.
    app_id = models.CharField(db_column='APP_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    app_secret = models.CharField(db_column='APP_SECRET', max_length=100, blank=True, null=True)  # Field name made lowercase.
    app_key = models.CharField(db_column='APP_KEY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_url = models.CharField(db_column='RETURN_URL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='TOKEN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_weixin_config'


class TblWeixinScanStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    market_activity_id = models.IntegerField(db_column='MARKET_ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    total_scan_no = models.IntegerField(db_column='TOTAL_SCAN_NO', blank=True, null=True)  # Field name made lowercase.
    total_customer_no = models.IntegerField(db_column='TOTAL_CUSTOMER_NO', blank=True, null=True)  # Field name made lowercase.
    conversion_rate = models.FloatField(db_column='CONVERSION_RATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_weixin_scan_statistics'


class TblWeixinScanTimeStatistics(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    market_activity_id = models.IntegerField(db_column='MARKET_ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    scan_no = models.IntegerField(db_column='SCAN_NO', blank=True, null=True)  # Field name made lowercase.
    customer_no = models.IntegerField(db_column='CUSTOMER_NO', blank=True, null=True)  # Field name made lowercase.
    conversion_rate = models.FloatField(db_column='CONVERSION_RATE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_weixin_scan_time_statistics'


class WxAutoReply(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=256, blank=True, null=True)  # Field name made lowercase.
    msg_type = models.CharField(db_column='MSG_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    event = models.CharField(db_column='EVENT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    key_word = models.CharField(db_column='KEY_WORD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    app_id = models.CharField(db_column='APP_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wx_auto_reply'


class WxAutoReplyArticleItem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    auto_reply_id = models.IntegerField(db_column='AUTO_REPLY_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pic_url = models.CharField(db_column='PIC_URL', max_length=256, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wx_auto_reply_article_item'


class WxMenu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    event_key = models.CharField(db_column='EVENT_KEY', max_length=128, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    media_id = models.CharField(db_column='MEDIA_ID', max_length=256, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.IntegerField(db_column='CREATED_BY')  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    last_modified_id = models.IntegerField(db_column='LAST_MODIFIED_ID')  # Field name made lowercase.
    mark_for_delete = models.IntegerField(db_column='MARK_FOR_DELETE', blank=True, null=True)  # Field name made lowercase.
    opt_counter = models.IntegerField(db_column='OPT_COUNTER', blank=True, null=True)  # Field name made lowercase.
    deleted_date = models.DateTimeField(db_column='DELETED_DATE', blank=True, null=True)  # Field name made lowercase.
    last_modified = models.DateTimeField(db_column='LAST_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    menu_type = models.CharField(db_column='MENU_TYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    show_order = models.IntegerField(db_column='SHOW_ORDER', blank=True, null=True)  # Field name made lowercase.
    app_id = models.CharField(db_column='APP_ID', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wx_menu'
