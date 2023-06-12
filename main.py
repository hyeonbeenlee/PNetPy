from recurdyn import *

# from recurdyn import Chart
# from recurdyn import MTT2D
# from recurdyn import FFlex
# from recurdyn import RFlex
from recurdyn import Tire
from datetime import datetime
import numpy as np
import re, os, glob, os
import pandas as pd

from utils.modeling import *
from analysis.doe_batch import *
from analysis.doe_gui import *
from analysis.export_data import *

app = None
application = None
model_document = None
plot_document = None
model = None

ref_frame_1 = None
ref_frame_2 = None


# initialize() should be called before ProcessNet function call.
def initialize():
    global app
    global application
    global model_document
    global plot_document
    global model

    app = dispatch_recurdyn()
    application = IApplication(app.RecurDynApplication)
    model_document = application.ActiveModelDocument
    if model_document is not None:
        model_document = IModelDocument(model_document)
    plot_document = application.ActivePlotDocument
    if plot_document is not None:
        plot_document = IPlotDocument(plot_document)

    if model_document is None and plot_document is None:
        application.PrintMessage("No model file")
        model_document = application.NewModelDocument("Examples")
    if model_document is not None:
        model_document = IModelDocument(model_document)
        model = ISubSystem(model_document.Model)

    return application, model_document, plot_document, model


# dispose() should be called after ProcessNet function call.
def dispose():
    global application
    global model_document

    model_document = application.ActiveModelDocument
    if model_document is not None:
        model_document = IModelDocument(model_document)
    else:
        return

    if not model_document.Validate():
        return
    # Redraw() and UpdateDatabaseWindow() can take more time in a heavy model.
    # model_document.Redraw()
    # model_document.PostProcess() # UpdateDatabaseWindow(), SetModified()
    # model_document.UpdateDatabaseWindow()
    # If you call SetModified(), Animation will be reset.
    # model_document.SetModified()
    model_document.SetUndoHistory("Python ProcessNet")


if __name__ == "__main__":
    application, model_document, plot_document, model = initialize()

    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################
    # GUI solver (not parallelized)
    RunDOE_GUI(
        ModelFileDir=f"{os.getcwd()}/SampleModel.rdyn",
        TopFolderName="TestDOE_GUI",
        NumCPUCores=8,
        EndTime=1,
        NumSteps=100,
    )
    rplt2csv(f"{os.getcwd()}/TestDOE_GUI")

    # Batch solver (parallelized)
    RunDOE_Batch(
        ModelFileDir="SampleModel.rdyn",
        TopFolderName="TestDOE_Batch",
        NumCPUCores=8,
        EndTime=1,
        NumSteps=100,
        NumParallelBatches=5,
    )
    rplt2csv(f"{os.getcwd()}/TestDOE_Batch")
    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################
    ######################################### EDIT HERE #########################################

    dispose()
