import csv
from dataSources import dataSources
from helper_functions import post_updates
csv.field_size_limit(999999999)

class AbsenteeFileEntry:
    County = ""
    VoterRegistrationNumber = ""
    LastName = ""
    FirstName = ""
    MiddleName = ""
    Suffix = ""
    StreetNumber = ""
    StreetName = ""
    AptUnit = ""
    City = ""
    State = ""
    ZipCode = ""
    MailingStreetNumber = ""
    MailingStreetName = ""
    MailingAptUnit = ""
    MailingCity = ""
    MailingState = ""
    MailingZipCode = ""
    ApplicationStatus = ""
    BallotStatus = ""
    StatusReason = ""
    ApplicationDate = ""
    BallotIssuedDate = ""
    BallotReturnDate = ""
    BallotStyle = ""
    BallotAssisted = ""
    ChallengedProvisional = ""
    IdRequired = ""
    MunicipalPrecinct = ""
    CountyPrecinct = ""
    Cng = ""
    Sen = ""
    House = ""
    Jud = ""
    ComboNumber = ""
    VoteCenterId = ""
    BallotId = ""
    PostNumber = ""
    Party = ""

    def __str__(self):
        return f"{self.VoterRegistrationNumber}: {self.FirstName} {self.LastName}, " \
               f"from {self.ResidenceCity}"

    def __repr__(self):
        return f"Absentee File Entry: {self.VoterRegistrationNumber}, Ballot Status: {self.BallotStatus}"



def eba_voter_generator(eba_filepath=PATH):
    with open(eba_filepath, errors="replace") as eba_file:
        voterbase_reader = csv.DictReader(eba_file)
        for row in voterbase_reader:
            if row['Apt/Unit'] == " ":
                row['Apt/Unit'] = ""
            yield row
    eba_file.close()


def get_dict_of_voters(voterbase_filepath=PATH):
    dict_of_voters = {}
    dict_of_mail_voters = {}
    dict_of_inperson_voters = {}
    dict_of_fulton_voters = {}
    dict_of_fulton_mail_voters = {}
    dict_of_fulton_inperson_voters = {}

    voters = eba_voter_generator(voterbase_filepath)
    for voter in voters:
        registration_number = int(voter['Voter Registration #'])
        county = voter['County']
        ballot_status = voter["Ballot Status"]
        if ballot_status != "A":
            continue
        dict_of_voters.update({registration_number: ''})
        ballot_style = voter["Ballot Style"]
        if ballot_style == "MAILED":
            dict_of_mail_voters.update({registration_number: ''})
        elif ballot_style == "IN PERSON" or ballot_style == "ELECTRONIC":
            dict_of_inperson_voters.update({registration_number: ''})
        if county != "FULTON":
            continue
        dict_of_fulton_voters.update({registration_number: ''})
        if ballot_style == "MAILED":
            dict_of_fulton_mail_voters.update({registration_number: ''})
        elif ballot_style == "IN PERSON" or ballot_style == "ELECTRONIC":
            dict_of_fulton_inperson_voters.update({registration_number: ''})

    return dict_of_voters, dict_of_mail_voters, dict_of_inperson_voters, \
           dict_of_fulton_voters, dict_of_fulton_mail_voters, dict_of_fulton_inperson_voters

