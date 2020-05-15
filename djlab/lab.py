import datajoint as dj


class Lab(dj.Lookup):
    definition = """
    lab             : varchar(32)  # name of lab
    ---
    institution     : varchar(255)
    address         : varchar(255)
    time_zone       : varchar(64)
    """


class Location(dj.Lookup):  # revisit the naming
    definition = """
    # location of animal housing or experimental rigs
    -> Lab
    location            : varchar(32)
    ---
    location_desc=''    : varchar(255)
    """


class UserRole(dj.Lookup):
    definition = """
    user_role       : varchar(16)
    """


class User(dj.Lookup):
    definition = """
    user                : varchar(32)
    ---
    user_email=''       : varchar(128)
    user_cellphone=''   : varchar(32)
    """


class LabMembership(dj.Lookup):
    definition = """
    -> Lab
    -> User
    ---
    -> [nullable] UserRole
    """


class ProtocolType(dj.Lookup):
    definition = """
    protocol_type           : varchar(32)
    """


class Protocol(dj.Lookup):
    definition = """
    # protocol approved by some institutions like IACUC, IRB
    protocol                : varchar(16)
    ---
    -> ProtocolType
    protocol_desc=''        : varchar(255)
    """


class Project(dj.Lookup):
    definition = """
    project                 : varchar(32)
    ---
    project_desc=''         : varchar(1024)
    """


class ProjectUser(dj.Manual):
    definition = """
    -> Project
    -> User
    """


class Source(dj.Lookup):
    definition = """
    # source of animal
    source             : varchar(32)    # nickname of the source
    ---
    source_name        : varchar(255)	# fullname of source
    contact_details='' : varchar(255)
    source_desc=''     : varchar(255)	# description
    """
