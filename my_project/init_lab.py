import datajoint as dj
from djlab import schema_template as lab

schema = dj.schema('u24_lab_')

lab.declare_tables(schema, add_here=True)
