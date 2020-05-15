import datajoint as dj
from .lab import *
import inspect
from djutils.pipeline import Pipeline


_lab_tables = (Lab, Location, User, UserRole, LabMembership,
               ProtocolType, Protocol, Project, ProjectUser,
               Source)

pipeline = Pipeline(_lab_tables)
