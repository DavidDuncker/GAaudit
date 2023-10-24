import csv
import sys
from dataSources import dataSources
from helper_functions import post_updates
csv.field_size_limit(999999999)

county_dict = {'001': 'APPLING', '002': 'ATKINSON', '003': 'BACON', '004': 'BAKER', '005': 'BALDWIN', '006': 'BANKS',
               '007': 'BARROW', '008': 'BARTOW', '009': 'BEN HILL', '010': 'BERRIEN', '011': 'BIBB', '012': 'BLECKLEY',
               '013': 'BRANTLEY', '014': 'BROOKS', '015': 'BRYAN', '016': 'BULLOCH', '017': 'BURKE', '018': 'BUTTS',
               '019': 'CALHOUN', '020': 'CAMDEN', '021': 'CANDLER', '022': 'CARROLL', '023': 'CATOOSA',
               '024': 'CHARLTON', '025': 'CHATHAM', '026': 'CHATTAHOOCHEE', '027': 'CHATTOOGA', '028': 'CHEROKEE',
               '029': 'CLARKE', '030': 'CLAY', '031': 'CLAYTON', '032': 'CLINCH', '033': 'COBB', '034': 'COFFEE',
               '035': 'COLQUITT', '036': 'COLUMBIA', '037': 'COOK', '038': 'COWETA', '039': 'CRAWFORD', '040': 'CRISP',
               '041': 'DADE', '042': 'DAWSON', '043': 'DECATUR', '044': 'DEKALB', '045': 'DODGE', '046': 'DOOLY',
               '047': 'DOUGHERTY', '048': 'DOUGLAS', '049': 'EARLY', '050': 'ECHOLS', '051': 'EFFINGHAM',
               '052': 'ELBERT', '053': 'EMANUEL', '054': 'EVANS', '055': 'FANNIN', '056': 'FAYETTE', '057': 'FLOYD',
               '058': 'FORSYTH', '059': 'FRANKLIN', '060': 'FULTON', '061': 'GILMER', '062': 'GLASCOCK',
               '063': 'GLYNN', '064': 'GORDON', '065': 'GRADY', '066': 'GREENE', '067': 'GWINNETT', '068': 'HABERSHAM',
               '069': 'HALL', '070': 'HANCOCK', '071': 'HARALSON', '072': 'HARRIS', '073': 'HART', '074': 'HEARD',
               '075': 'HENRY', '076': 'HOUSTON', '077': 'IRWIN', '078': 'JACKSON', '079': 'JASPER',
               '080': 'JEFF DAVIS', '081': 'JEFFERSON', '082': 'JENKINS', '083': 'JOHNSON', '084': 'JONES',
               '085': 'LAMAR', '086': 'LANIER', '087': 'LAURENS', '088': 'LEE', '089': 'LIBERTY', '090': 'LINCOLN',
               '091': 'LONG', '092': 'LOWNDES', '093': 'LUMPKIN', '094': 'MACON', '095': 'MADISON', '096': 'MARION',
               '097': 'MCDUFFIE', '098': 'MCINTOSH', '099': 'MERIWETHER', '100': 'MILLER', '101': 'MITCHELL',
               '102': 'MONROE', '103': 'MONTGOMERY', '104': 'MORGAN', '105': 'MURRAY', '106': 'MUSCOGEE',
               '107': 'NEWTON', '108': 'OCONEE', '109': 'OGLETHORPE', '110': 'PAULDING', '111': 'PEACH',
               '112': 'PICKENS', '113': 'PIERCE', '114': 'PIKE', '115': 'POLK', '116': 'PULASKI', '117': 'PUTNAM',
               '118': 'QUITMAN', '119': 'RABUN', '120': 'RANDOLPH', '121': 'RICHMOND', '122': 'ROCKDALE',
               '123': 'SCHLEY', '124': 'SCREVEN', '125': 'SEMINOLE', '126': 'SPALDING', '127': 'STEPHENS',
               '128': 'STEWART', '129': 'SUMTER', '130': 'TALBOT', '131': 'TALIAFERRO', '132': 'TATTNALL',
               '133': 'TAYLOR', '134': 'TELFAIR', '135': 'TERRELL', '136': 'THOMAS', '137': 'TIFT', '138': 'TOOMBS',
               '139': 'TOWNS', '140': 'TREUTLEN', '141': 'TROUP', '142': 'TURNER', '143': 'TWIGGS', '144': 'UNION',
               '145': 'UPSON', '146': 'WALKER', '147': 'WALTON', '148': 'WARE', '149': 'WARREN', '150': 'WASHINGTON',
               '151': 'WAYNE', '152': 'WEBSTER', '153': 'WHEELER', '154': 'WHITE', '155': 'WHITFIELD', '156': 'WILCOX',
               '157': 'WILKES', '158': 'WILKINSON', '159': 'WORTH', "": ""}


class VoterBaseEntry:
    CountyName = ""
    CountyCode = ""
    RegistrationNumber = ""
    VoterStatus = ""
    LastName = ""
    FirstName = ""
    MiddleMaidenName = ""
    NameSuffix = ""
    NameTitle = ""
    ResidenceHouseNumber = ""
    ResidenceStreetName = ""
    ResidenceStreetSuffix = ""
    ResidenceAptUnitNbr = ""
    ResidenceCity = ""
    ResidenceZipcode = ""
    Birthdate = ""
    RegistrationDate = ""
    Race = ""
    Gender = ""
    LandDistrict = ""
    LandLot = ""
    StatusReason = ""
    CountyPrecinctId = ""
    CityPrecinctId = ""
    CongressionalDistrict = ""
    SenateDistrict = ""
    HouseDistrict = ""
    JudicialDistrict = ""
    CommissionDistrict = ""
    SchoolDistrict = ""
    CountyDistrictaName = ""
    CountyDistrictaValue = ""
    CountyDistrictbName = ""
    CountyDistrictbValue = ""
    MunicipalName = ""
    MunicipalCode = ""
    WardCityCouncilName = ""
    WardCityCouncilCode = ""
    CitySchoolDistrictName = ""
    CitySchoolDistrictValue = ""
    CityDistaName = ""
    CityDistaValue = ""
    CityDistbName = ""
    CityDistbValue = ""
    CityDistcName = ""
    CityDistcValue = ""
    CityDistdName = ""
    CityDistdValue = ""
    DateLastVoted = ""
    PartyLastVoted = ""
    DateAdded = ""
    DateChanged = ""
    DistrictCombo = ""
    RaceDesc = ""
    LastContactDate = ""
    MailHouseNbr = ""
    MailStreetName = ""
    MailAptUnitNbr = ""
    MailCity = ""
    MailState = ""
    MailZipcode = ""
    MailAddress2 = ""
    MailAddress3 = ""
    MailCountry = ""

    def __str__(self):
        return f"{self.RegistrationNumber}: {self.FirstName} {self.LastName}, born in {self.Birthdate}, " \
               f"from {self.ResidenceCity}"

    def __repr__(self):
        return f"VoterBase Entry: {self.RegistrationNumber}, {self.Birthdate}, Last Voted in {self.DateLastVoted}"


class VoterBaseHandler:
    voterBaseNov2020 = dataSources.voterBaseNov
    voterBaseOct2020 = dataSources.voterBaseOct

    def generateVoterEntry(self, row):
        voter = VoterBaseEntry()
        voter.CountyName = county_dict[row["COUNTY_CODE"]]
        voter.CountyCode = row["COUNTY_CODE"]
        voter.RegistrationNumber = int(row["REGISTRATION_NUMBER"])
        voter.VoterStatus = row["VOTER_STATUS"]
        voter.LastName = row["LAST_NAME"]
        voter.FirstName = row["FIRST_NAME"]
        voter.MiddleMaidenName = row["MIDDLE_MAIDEN_NAME"]
        voter.NameSuffix = row["NAME_SUFFIX"]
        voter.NameTitle = row["NAME_TITLE"]
        voter.ResidenceHouseNumber = row["RESIDENCE_HOUSE_NUMBER"]
        voter.ResidenceStreetName = row["RESIDENCE_STREET_NAME"]
        voter.ResidenceStreetSuffix = row["RESIDENCE_STREET_SUFFIX"]
        voter.ResidenceAptUnitNbr = row["RESIDENCE_APT_UNIT_NBR"]
        voter.ResidenceCity = row["RESIDENCE_CITY"]
        voter.ResidenceZipcode = row["RESIDENCE_ZIPCODE"]
        voter.Birthdate = int(row["BIRTHDATE"])
        voter.RegistrationDate = int(row["REGISTRATION_DATE"])
        voter.Race = row["RACE"]
        voter.Gender = row["GENDER"]
        voter.LandDistrict = row["LAND_DISTRICT"]
        voter.LandLot = row["LAND_LOT"]
        voter.StatusReason = row["STATUS_REASON"]
        voter.CountyPrecinctId = row["COUNTY_PRECINCT_ID"]
        voter.CityPrecinctId = row["CITY_PRECINCT_ID"]
        voter.CongressionalDistrict = row["CONGRESSIONAL_DISTRICT"]
        voter.SenateDistrict = row["SENATE_DISTRICT"]
        voter.HouseDistrict = row["HOUSE_DISTRICT"]
        voter.JudicialDistrict = row["JUDICIAL_DISTRICT"]
        voter.CommissionDistrict = row["COMMISSION_DISTRICT"]
        voter.SchoolDistrict = row["SCHOOL_DISTRICT"]
        voter.CountyDistrictaName = row["COUNTY_DISTRICTA_NAME"]
        voter.CountyDistrictaValue = row["COUNTY_DISTRICTA_VALUE"]
        voter.CountyDistrictbName = row["COUNTY_DISTRICTB_NAME"]
        voter.CountyDistrictbValue = row["COUNTY_DISTRICTB_VALUE"]
        voter.MunicipalName = row["MUNICIPAL_NAME"]
        voter.MunicipalCode = row["MUNICIPAL_CODE"]
        voter.WardCityCouncilName = row["WARD_CITY_COUNCIL_NAME"]
        voter.WardCityCouncilCode = row["WARD_CITY_COUNCIL_CODE"]
        voter.CitySchoolDistrictName = row["CITY_SCHOOL_DISTRICT_NAME"]
        voter.CitySchoolDistrictValue = row["CITY_SCHOOL_DISTRICT_VALUE"]
        voter.CityDistaName = row["CITY_DISTA_NAME"]
        voter.CityDistaValue = row["CITY_DISTA_VALUE"]
        voter.CityDistbName = row["CITY_DISTB_NAME"]
        voter.CityDistbValue = row["CITY_DISTB_VALUE"]
        voter.CityDistcName = row["CITY_DISTC_NAME"]
        voter.CityDistcValue = row["CITY_DISTC_VALUE"]
        voter.CityDistdName = row["CITY_DISTD_NAME"]
        voter.CityDistdValue = row["CITY_DISTD_VALUE"]
        voter.DateLastVoted = row["DATE_LAST_VOTED"]
        voter.PartyLastVoted = row["PARTY_LAST_VOTED"]
        voter.DateAdded = row["DATE_ADDED"]
        voter.DateChanged = row["DATE_CHANGED"]
        voter.DistrictCombo = row["DISTRICT_COMBO"]
        voter.RaceDesc = row["RACE_DESC"]
        voter.LastContactDate = row["LAST_CONTACT_DATE"]
        voter.MailHouseNbr = row["MAIL_HOUSE_NBR"]
        voter.MailStreetName = row["MAIL_STREET_NAME"]
        voter.MailAptUnitNbr = row["MAIL_APT_UNIT_NBR"]
        voter.MailCity = row["MAIL_CITY"]
        voter.MailState = row["MAIL_STATE"]
        voter.MailZipcode = row["MAIL_ZIPCODE"]
        voter.MailAddress2 = row["MAIL_ADDRESS_2"]
        voter.MailAddress3 = row["MAIL_ADDRESS_3"]
        voter.MailCountry = row["MAIL_COUNTRY"]

        return voter

    def readVoterFile(self, voterFile=voterBaseNov2020):
        with open(voterFile, errors="replace") as voterbase_file:

            voterbase_reader = csv.DictReader(voterbase_file, delimiter="|", quoting=csv.QUOTE_NONE)
            row_count = 0
            for row in voterbase_reader:
                yield self.generateVoterEntry(row)
                row_count += 1
                post_updates(row_count, [1, 10, 100, 1000, 10000, 100000])
        voterbase_file.close()

    def getAll2020Voters(self):
        # Warning! This function will return a list of people that either
        #Voted in November 3rd, 2020, or voted early for the 12/01/2020 or 1/5/2021 election
        #by November 24th, 2020
        list_of_voters = []
        for voter in self.readVoterFile(voterFile=self.voterBaseNov2020):
            if voter.DateLastVoted > "20201103":
                list_of_voters.append(voter.RegistrationNumber)

        return list_of_voters



