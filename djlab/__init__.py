import datajoint as dj
from .lab import *
import inspect
from djutils.pipeline import Pipeline


# ========================== HELPER METHODS =======================

_lab_tbls = (Lab, Location, User, UserRole, LabMembership,
             ProtocolType, Protocol, Project, ProjectUser,
             Source)

pipeline = Pipeline(_lab_tbls)

# def _init_lab_tbls(schema, context):

#     init_tbls = {}
#     for tbl in _lab_tbls:
#         print(f'Initializing {tbl.__name__}')
#         init_tbl = schema(tbl, context=context)
#         init_tbls[tbl.__name__] = init_tbl

#     return init_tbls


# def init_lab_pipeline(schema, context={}, add_here=False):

#     if add_here and not context:
#         context = inspect.currentframe().f_back.f_locals

#     lab_pipeline = _init_lab_tbls(schema, context)

#     if add_here:
#         context.update(**lab_pipeline)

#     return lab_pipeline
