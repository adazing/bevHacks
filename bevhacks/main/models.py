from django.db import models

# Create your models here.

# INSTNM

#general
    #ADM_RATE_ALL (admission rates)
    #CONTROL(type of school: public, private, etc)(we have to convert 1,2,3 to their corresponding values)
    #ADDR,  CITY, STABBR,  ZIP
    #LATITUDE, LONGITUDE
    #INSTURL(homepage for school)


#Student-to-Faculty Ratio
#numstuds

#test scores/stats
    #SATVR{25,50,75} (reading)
    #SATMT{25,50,75} (math)


#Paying for stuff
    #TUITIONFEE_IN(in state)
    #TUITIONFEE_OUT(out of state)
    #NPCURL(price claculator for that school!!)

#diversity
    # men (UGDS_MEN)
    # women (UGDS_WOMEN)
    # white (UGDS_WHITE)
    # black (UGDS_BLACK)
    # Hispanic (UGDS_HISP)
    # Asian (UGDS_ASIAN)
    # American Indian/Alaska Native (UGDS_AIAN)
    # Native Hawaiian/Pacific Islander (UGDS_NHPI)
    # two or more races (UGDS_2MOR)
    # non-resident aliens (UGDS_NRA)
    # race unknown (UGDS_UNKN)


class Institution(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    admission_rate = models.FloatField(null=True, blank=True)
    control = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    stabbr = models.CharField(max_length=256, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    home_page = models.CharField(max_length=256, null=True, blank=True)
    satvr25 = models.IntegerField(null=True, blank=True)
    satvr50 = models.IntegerField(null=True, blank=True)
    satvr75 = models.IntegerField(null=True, blank=True)
    satmt25 = models.IntegerField(null=True, blank=True)
    satmt50 = models.IntegerField(null=True, blank=True)
    satmt75 = models.IntegerField(null=True, blank=True)
    tuition_fee_in = models.FloatField(null=True, blank=True)
    tuition_fee_out = models.FloatField(null=True, blank=True)
    np_curl = models.CharField(max_length=256, null=True, blank=True)
    men = models.FloatField(null=True, blank=True)
    women = models.FloatField(null=True, blank=True)
    white = models.FloatField(null=True, blank=True)
    black = models.FloatField(null=True, blank=True)
    hispanic = models.FloatField(null=True, blank=True)
    asian = models.FloatField(null=True, blank=True)
    ai_an = models.FloatField(null=True, blank=True)
    na_pi = models.FloatField(null=True, blank=True)
    two = models.FloatField(null=True, blank=True)
    alien = models.FloatField(null=True, blank=True)
    unknown = models.FloatField(null=True, blank=True)
# {{i.unknown}}