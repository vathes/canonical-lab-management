import datajoint as dj
from djlab import pipeline

schema = dj.schema('u24_lab_')

lab_tables = pipeline.init_pipeline(schema, add_here=True)
