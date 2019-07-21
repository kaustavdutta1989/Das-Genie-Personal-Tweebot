from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os


DasGenie = ChatBot('DasGenie')

DasGenie.set_trainer(ListTrainer)

TrainingDataLoc = 'GenieCuisine'

for conversationFile in os.listdir(TrainingDataLoc):
    convo = open(TrainingDataLoc + '/' + conversationFile, 'r').readlines()
    DasGenie.train(convo)
