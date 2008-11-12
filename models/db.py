db=SQLDB("sqlite://db.db")

db.define_table('component', 
	SQLField('name',length=256),
	SQLField('cost','integer'))

db.define_table('skill',
    SQLField('name'))
    
db.define_table('craftable', 
    SQLField('name', length=256), 
    SQLField('description'),
    SQLField('skill', db.skill),
	SQLField('experience', 'integer'))
    
db.define_table('formula',
    SQLField('craftable', db.craftable),
    SQLField('component', db.component),
    SQLField('amount', 'integer'))
    
db.component.name.requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'component.name')]
db.craftable.name.requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'craftable.name')]
db.craftable.skill.requires=IS_IN_DB(db,'skill.id','skill.name')
db.skill.name.requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'skill.name')]
db.formula.craftable.requires=IS_IN_DB(db,'craftable.id','craftable.name')
db.formula.component.requires=IS_IN_DB(db,'component.id','component.name')