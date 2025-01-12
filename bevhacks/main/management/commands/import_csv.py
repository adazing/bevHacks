import csv
from django.core.management.base import BaseCommand
from main.models import Institution

# INSTNM (name)
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
    #TUITIONFEEIN(in state)
    #TUITIONFEEOUT(out of state)
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


class Command(BaseCommand):
    help = 'Load initial data from CSV file into the database'

    '''
        name=models.CharField(max_length=256, null=True, blank=True)
        admission_rate = models.FloatField(null=True, blank=True)
        control = models.CharField(max_length=256, null=True, blank=True)
        address = models.CharField(max_length=256, null=True, blank=True)
        city = models.CharField(max_length=256, null=True, blank=True)
        stabbr = models.CharField(max_length=256, null=True, blank=True)
        zip_code = models.IntegerField(null=True, blank=True)
        latitude = models.FloatField(null=True, blank=True)
        longitude = models.FloatField(null=True, blank=True)
        home_page = models.CharField(max_length=256, null=True, blank=True)
        num_studs = models.IntegerField(null=True, blank=True)
        satvr25 = models.IntegerField(null=True, blank=True)
        satvr50 = models.IntegerField(null=True, blank=True)
        satvr75 = models.IntegerField(null=True, blank=True)
        satmt25 = models.IntegerField(null=True, blank=True)
        satmt50 = models.IntegerField(null=True, blank=True)
        satmt75 = models.IntegerField(null=True, blank=True)
        tuition_fee_in = models.FloatField(null=True, blank=True)
        tuition_fee_out = models.FloatField(null=True, blank=True)
        np_curl = models.FloatField(null=True, blank=True)
        men = models.IntegerField(null=True, blank=True)
        women = models.IntegerField(null=True, blank=True)
        white = models.IntegerField(null=True, blank=True)
        black = models.IntegerField(null=True, blank=True)
        hispanic = models.IntegerField(null=True, blank=True)
        asian = models.IntegerField(null=True, blank=True)
        ai_an = models.IntegerField(null=True, blank=True)
        na_pi = models.IntegerField(null=True, blank=True)
        two = models.IntegerField(null=True, blank=True)
        alien = models.IntegerField(null=True, blank=True)
        unknown = models.IntegerField(null=True, blank=True)
    '''

    def handle(self, *args, **kwargs):
        with open(r'C:\Users\jl\OneDrive\Documents\dev\bevHacks\bevhacks\main\management\commands\Most-Recent-Cohorts-Institution.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row.keys())
                # Create a new record in the UserProfile model for each row in the CSV
                Institution.objects.create(
                    name=row["INSTNM"] if row["INSTNM"]!="NA" else None,
                    admission_rate=float(row["ADM_RATE_ALL"]) if row["ADM_RATE_ALL"]!="NA" else None,
                    control = row["CONTROL"] if row["CONTROL"]!="NA" else None,
                    address = row["ADDR"] if row["ADDR"]!="NA" else None,
                    city = row["CITY"] if row["CITY"]!="NA" else None,
                    stabbr = row["STABBR"] if row["STABBR"]!="NA" else None,
                    # zip_code = int(row["ZIP"]) if row["ZIP"]!="NA" else None,
                    latitude = float(row["LATITUDE"]) if row["LATITUDE"]!="NA" else None,
                    longitude = float(row["LONGITUDE"]) if row["LONGITUDE"]!="NA" else None,
                    home_page = row["INSTURL"] if row["INSTURL"]!="NA" else None,
                    satvr25 = int(row["SATVR25"]) if row["SATVR25"]!="NA" else None,
                    satvr50 = int(row["SATVR50"]) if row["SATVR50"]!="NA" else None,
                    satvr75 = int(row["SATVR75"]) if row["SATVR75"]!="NA" else None,
                    satmt25 = int(row["SATMT25"]) if row["SATMT25"]!="NA" else None,
                    satmt50 = int(row["SATMT50"]) if row["SATMT50"]!="NA" else None,
                    satmt75 = int(row["SATMT75"]) if row["SATMT75"]!="NA" else None,
                    tuition_fee_in = float(row["TUITIONFEE_IN"]) if row["TUITIONFEE_IN"]!="NA" else None,
                    tuition_fee_out = float(row["TUITIONFEE_OUT"]) if row["TUITIONFEE_OUT"]!="NA" else None,
                    np_curl = row["NPCURL"] if row["NPCURL"]!="NA" else None,
                    men = float(row["UGDS_MEN"]) if row["UGDS_MEN"]!="NA" else None,
                    women = float(row["UGDS_WOMEN"]) if row["UGDS_WOMEN"]!="NA" else None,
                    white = float(row["UGDS_WHITE"]) if row["UGDS_WHITE"]!="NA" else None,
                    black = float(row["UGDS_BLACK"]) if row["UGDS_BLACK"]!="NA" else None,
                    hispanic = float(row["UGDS_HISP"]) if row["UGDS_HISP"]!="NA" else None,
                    asian = float(row["UGDS_ASIAN"]) if row["UGDS_ASIAN"]!="NA" else None,
                    ai_an = float(row["UGDS_AIAN"]) if row["UGDS_AIAN"]!="NA" else None,
                    na_pi = float(row["UGDS_NHPI"]) if row["UGDS_NHPI"]!="NA" else None,
                    two = float(row["UGDS_2MOR"]) if row["UGDS_2MOR"]!="NA" else None,
                    alien = float(row["UGDS_NRA"]) if row["UGDS_NRA"]!="NA" else None,
                    unknown = float(row["UGDS_UNKN"]) if row["UGDS_UNKN"]!="NA" else None,
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))
