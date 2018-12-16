from os import listdir # This library has some functions to read the list of files names in a folder
from Scripts.Functions import *
import os, shutil #To remove files from a folder



# ***************  Remove Files *************************************** #


def removeFilesFolder(folderPath):

    # folder = '/path/to/folder'
    for the_file in os.listdir(folderPath):
        file_path = os.path.join(folderPath, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

# ***************  Files Export *************************************** #

def exportParticipantsFiles(path, folder, transposeParticipantUniqueFile  = True, mode = None, participantsIdsList = None):


    #Mode: Chile or UK

    #Path with participants responses
    fullPath = path+"/"+folder

    #List of folders with participants' responses

    foldersList = listdir(fullPath)
    foldersList.sort() #Sort list in an increasing order


    #Files where the participants responses will be exported
    # fileSimulatedLearningResponses = "SimulatedLearningResponses"
    # fileDescriptiveLearningResponses = "DescriptiveLearningResponses"
    # fileSimulatedChoiceResponses = "SimulatedChoiceResponses"
    # fileDescriptiveChoiceResponses = "DescriptiveChoiceResponses"
    fileParticipants = "Participants" #I need to transpose the information before

    #Read list of files in folder with participants' files

    participantFiles = ["ExperimentsSimulatedLearningResponses"
        , "ExperimentsDescriptiveLearningResponses"
        , "ExperimentsSimulatedChoiceResponses"
        , "ExperimentsDescriptiveChoiceResponses"
        , "TravelBehaviourInformation"
        , "ExperimentDebriefInformation"
        , "ExperimentsReactionTimeResponses"]

    #Remove existing files from the folders

    for filesFolder in participantFiles:
        folderPath = path+"/"+filesFolder
        removeFilesFolder(folderPath=folderPath)

    folderPath = path + "/Participants"
    removeFilesFolder(folderPath=folderPath)

    #**Information about descriptive learning response is not shown for participants allocated in the treatment descriptive condition

    # participantFiles = ["ExperimentsSimulatedLearningResponses.csv"
    #     , "ExperimentsSimulatedChoiceResponses.csv"
    #     , "ExperimentsSimulatedLearningResponses.csv"]


    #Create list with participants ids

    participantsIds = []

    # ParticipantsIdList: The user may specify a range of ids to read from the folder (a subset of participants responses)

    if participantsIdsList is not None:
        for nParticipantId in participantsIdsList:
            if nParticipantId < 10:
                participantsIds.append("0"+str(nParticipantId))
            else:
                participantsIds.append(str(nParticipantId))

    else:
        for participantFolderName in foldersList:

            participantFolderNameInteger = ""
            try:
                participantFolderNameInteger = int(participantFolderName)
            except ValueError:
                participantFolderNameInteger = None

            if participantFolderNameInteger is not None:
                participantsIds.append(participantFolderName)

    firstFile = None #boolean
    counterLine = None #Counter for the line read by the algorithm

    for participantFile in participantFiles:

        firstFile = True

        for nParticipant in foldersList:

            if nParticipant in participantsIds: #only read from fodler with valid ids.

                counterLine = 0

                participantFileTransposed = False

                #Check if there are files in the participant's folder

                participantFoldersFilesListPath = fullPath + "/" + str(nParticipant)
                participantFoldersFilesList = listdir(participantFoldersFilesListPath)
                participantFileCsv = participantFile + ".csv"

                if participantFileCsv in participantFoldersFilesList:

                    #Read informatin from participant file (1 out of 4 files)
                    readingPath = fullPath+"/"+str(nParticipant)+"/"+participantFile+".csv"
                    readingFileParticipant = open(readingPath,'r')
                    infoFileParticipant = readingFileParticipant.readlines()
                    readingFileParticipant.close()

                    if len(infoFileParticipant) is not 0: #If the file is empty

                        # Write one file per participant
                        writingUniquePath = path + "/" + participantFile + "/" + str(nParticipant) + ".csv"
                        writingUniqueFileParticipant = open(writingUniquePath, 'w')  # Remove the existing file

                        # Write information in unique file
                        writingPath = path + "/" + participantFile + ".csv"

                        if firstFile is True:
                            writingFileParticipant = open(writingPath, 'w')  # Remove the existing file

                        else:
                            writingFileParticipant = open(writingPath, 'a')

                        for infoFileParticipantLine in infoFileParticipant:

                            writingUniqueFileParticipant.write(infoFileParticipantLine)

                            if firstFile is True:
                                writingFileParticipant.write(infoFileParticipantLine)
                                firstFile = False

                            else:
                                if counterLine>0:
                                    writingFileParticipant.write(infoFileParticipantLine)

                            counterLine += 1


                    writingFileParticipant.close()

    #Transpose unique file for each participant

    if transposeParticipantUniqueFile is True:

        firstFile = True
        firstParticipant = True

        for nParticipant in foldersList:

            if nParticipant in participantsIds:  # only read from fodler with valid ids.


                participantFoldersFilesListPath = fullPath + "/" + str(nParticipant)
                participantFoldersFilesList = listdir(participantFoldersFilesListPath)
                participantFileCsv = participantFile + ".csv"

                if participantFileCsv in participantFoldersFilesList:

                    #Transpose unique participant file

                        readingPath = fullPath + "/" + str(nParticipant) + "/" + "Participant" +str(int(nParticipant)) +".csv" #Apply int function because the ids of the files do not include the 0 digit on the left
                        readingFileParticipant = open(readingPath, 'r')
                        infoFileParticipant = readingFileParticipant.readlines()
                        readingFileParticipant.close()

                        colLabels = []
                        rowLabels = []

                        for infoFileParticipantLine in infoFileParticipant:
                            colLabels.append(infoFileParticipantLine.split(",")[0].replace("\n","").replace(" ",""))
                            rowLabels.append(infoFileParticipantLine.split(",")[1].replace("\n","").replace(" ",""))

                        writingPath = path + "/" + "participants.csv"

                        writingUniquePath = path + "/"+ "Participants" + "/" + str(nParticipant) + ".csv"
                        writingUniqueFileParticipant = open(writingUniquePath, 'w')  # Remove the existing file
                        writingUniqueFileParticipant.write(printCsvLine(colLabels))
                        writingUniqueFileParticipant.write(printCsvLine(rowLabels))

                        if firstFile is True:
                            writingFileParticipant = open(writingPath, 'w')  # Remove the existing file
                            firstFile = False

                        else:
                            writingFileParticipant = open(writingPath, 'a')


                        if firstParticipant is True:
                            writingFileParticipant.write(printCsvLine(colLabels))
                            writingFileParticipant.write(printCsvLine(rowLabels))

                            firstParticipant = False

                        else:
                            writingFileParticipant.write(printCsvLine(rowLabels))

                        writingFileParticipant.close()
                        writingUniqueFileParticipant.close()

# def exportParticipantExperiencedOpenQuestion()


# ***************  Data Depuration *************************************** #

def separateExperiencedExperimentQuestion(path, experimentDebriefInformationFolder,outputFolderOpenQuestion, outputFolderNonOpenQuestions):
    pathFilesFolder = path + "/" + experimentDebriefInformationFolder
    participantsResponsesFiles = listdir(pathFilesFolder)

    for participantsResponsesFile in participantsResponsesFiles:

        readingPath = pathFilesFolder + "/" + participantsResponsesFile # Apply int function because the ids of the files do not include the 0 digit on the left
        readingFileParticipant = open(readingPath, 'r')
        infoFileParticipant = readingFileParticipant.readlines()
        readingFileParticipant.close()

        colLabels = []
        rowLabels = []

        colLabels  = infoFileParticipant[0].split(",")
        rowLabels = infoFileParticipant[1].split(",")

        # for infoFileParticipantLine in infoFileParticipant:
        #     colLabels.append(infoFileParticipantLine.split(",").replace("\n", "").replace(" ", ""))
        #     rowLabels.append(infoFileParticipantLine[1].split(",").replace("\n", "").replace(" ", ""))

        writingPath = path + "/" + "participants.csv"

        writingPathNonOpenQuestions = path + "/" + outputFolderNonOpenQuestions + "/" + participantsResponsesFile
        writingPathOpenQuestion = path + "/" + outputFolderOpenQuestion + "/" + participantsResponsesFile

        colLabelsNonOpenQuestions = colLabels[0:(len(colLabels)-1)]
        colLabelsOpenQuestion = colLabels[len(colLabels)-1]

        rowLabelsNonOpenQuestions = rowLabels[0:(len(colLabels)-1)]
        rowLabelsOpenQuestion = rowLabels[len(colLabels)-1]

        #Write one file per participant containing the non-open questions.
        writingUniqueFileParticipant = open(writingPathNonOpenQuestions, 'w')  # Remove the existing file
        writingUniqueFileParticipant.write(printCsvLine(colLabelsNonOpenQuestions))
        writingUniqueFileParticipant.write(printCsvLine(rowLabelsNonOpenQuestions))










# ***************  Execution *************************************** #
# Function to process data collected in Chile
# exportParticipantsFiles(path = "/Users/pablo/GoogleDrive/UCL/Academic/MasterThesis/DataAnalysis/Data/ExperimentChile"
#                         ,folder = "ParticipantsFolders", firstParticipantId = 1, lastParticipantId = 36
#               , transposeParticipantUniqueFile = True)

# Function to process data collected in the UK
exportParticipantsFiles(path = "/Users/pablo/GoogleDrive/University/UCL/Academic/MasterThesis/DataAnalysis/Data/ExperimentUK"
                        ,folder = "ParticipantsFolders", transposeParticipantUniqueFile = True)

# exportParticipantsFiles(path = "/Users/pablo/GoogleDrive/UCL/Academic/MasterThesis/DataAnalysis/Data/ExperimentUK"
#                         ,folder = "ParticipantsFolders",participantsIdsList  = list(range(37,50))
#                         , transposeParticipantUniqueFile = True)


separateExperiencedExperimentQuestion(path = "/Users/pablo/GoogleDrive/University/UCL/Academic/MasterThesis/DataAnalysis/Data/ExperimentUK"
                                      , experimentDebriefInformationFolder = "ExperimentDebriefInformation"
                                      , outputFolderOpenQuestion = "ExperimentOpenResponse"
                                      , outputFolderNonOpenQuestions = "ExperimentDebriefResponses")