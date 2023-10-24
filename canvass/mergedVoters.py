from dataSources import dataSources
from helper_functions import post_updates
import csv


class MergedVoterEntry:
    OriginalVoterId = ""
    OriginalNmLast = ""
    OriginalNmFirst = ""
    OriginalNmMid = ""
    OriginalStreetNumber = ""
    OriginalStreetName = ""
    OriginalUnit = ""
    OriginalAddressLine2 = ""
    OriginalCity = ""
    OriginalZip5 = ""
    OriginalZip4 = ""
    OriginalCdStatus = ""
    OriginalCdStatReason = ""
    OriginalCountyName = ""
    DuplicateVoterId = ""
    NmLast1 = ""
    NmFirst1 = ""
    NmMid1 = ""
    StreetNumber1 = ""
    StreetName1 = ""
    Unit1 = ""
    AddressLine21 = ""
    City1 = ""
    Zip51 = ""
    Zip41 = ""
    CdStatus1 = ""
    CdStatReason1 = ""
    DuplicateCountyName = ""

    def __str__(self):
        return f"{self.OriginalNmFirst} {self.OriginalNmLast}, {self.OriginalVoterId} became " \
               f"{self.NmFirst1} {self.NmLast1}, {self.DuplicateVoterId}"

    def __repr__(self):
        return f"Merged Voter Entry: {self.OriginalVoterId} merged with {self.DuplicateVoterId}"


class MergedVoterHandler:
    csvOfMergedVoters = dataSources.mergedVoters

    def generateMergedVoterEntry(self, row):
        voterPair = MergedVoterEntry()
        voterPair.OriginalVoterId = int(row["ORIGINAL_VOTER_ID"])
        voterPair.OriginalNmLast = row["ORIGINAL_NM_LAST"]
        voterPair.OriginalNmFirst = row["ORIGINAL_NM_FIRST"]
        voterPair.OriginalNmMid = row["ORIGINAL_NM_MID"]
        voterPair.OriginalStreetNumber = row["ORIGINAL_STREET#"]
        voterPair.OriginalStreetName = row["ORIGINAL_STREET_NAME"]
        voterPair.OriginalUnit = row["ORIGINAL_UNIT"]
        voterPair.OriginalAddressLine2 = row["ORIGINAL_ADDRESS_LINE_2"]
        voterPair.OriginalCity = row["ORIGINAL_CITY"]
        voterPair.OriginalZip5 = row["ORIGINAL_ZIP5"]
        voterPair.OriginalZip4 = row["ORIGINAL_ZIP4"]
        voterPair.OriginalCdStatus = row["ORIGINAL_CD_STATUS"]
        voterPair.OriginalCdStatReason = row["ORIGINAL_CD_STAT_REASON"]
        voterPair.OriginalCountyName = row["ORIGINAL_COUNTY_NAME"]
        voterPair.DuplicateVoterId = int(row["DUPLICATE_VOTER_ID"])
        voterPair.NmLast1 = row["NM_LAST_1"]
        voterPair.NmFirst1 = row["NM_FIRST_1"]
        voterPair.NmMid1 = row["NM_MID_1"]
        voterPair.StreetNumber1 = row["STREET#_1"]
        voterPair.StreetName1 = row["STREET_NAME_1"]
        voterPair.Unit1 = row["UNIT_1"]
        voterPair.AddressLine21 = row["ADDRESS_LINE_2_1"]
        voterPair.City1 = row["CITY_1"]
        voterPair.Zip51 = row["ZIP5_1"]
        voterPair.Zip41 = row["ZIP4_1"]
        voterPair.CdStatus1 = row["CD_STATUS_1"]
        voterPair.CdStatReason1 = row["CD_STAT_REASON_1"]
        voterPair.DuplicateCountyName = row["DUPLICATE_COUNTY_NAME"]

        return voterPair

    def readMergedVoterFile(self):
        with open(self.csvOfMergedVoters, errors="replace") as mergedVotersFile:

            mergedVotersReader = csv.DictReader(mergedVotersFile, delimiter=",", quoting=csv.QUOTE_NONE)
            row_count = 0
            for row in mergedVotersReader:
                yield self.generateMergedVoterEntry(row)
                row_count += 1
                post_updates(row_count, [1, 10, 100, 1000, 10000, 100000])
        mergedVotersFile.close()

    def getListOfRegistrationPairs(self):
        listOfMergedPairs = []
        dictOfRegNumbers = {}
        for mergedPair in self.readMergedVoterFile():
            listOfMergedPairs.append([mergedPair.OriginalVoterId, mergedPair.DuplicateVoterId])
            dictOfRegNumbers[mergedPair.OriginalVoterId] = None
            dictOfRegNumbers[mergedPair.DuplicateVoterId] = None

        return listOfMergedPairs, dictOfRegNumbers