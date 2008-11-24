# try something likedef index(): return dict(message="hello from test.py")
def test():
	c = db((db.formula.craftable==1)&(db.formula.component==db.component.id)).select(db.component.ALL,db.formula.ALL)
	return dict(records=c)

def formulas():
	craftables = db().select(db.craftable.ALL)
	components = dict()
	for craftable in craftables:
		c = db((db.formula.craftable==craftable.id)&(db.formula.component==db.component.id))\
			.select(db.component.ALL,db.formula.ALL)
		components[craftable.id] = c
	
	return dict(craftables=craftables, components=components)
	
def craft():
	id=request.vars.id	
	craftable = db(db.craftable.id==id).select()
	components = db((db.formula.craftable==id)&(db.formula.component==db.component.id))\
			.select(db.component.ALL,db.formula.ALL)
	return dict(craftable=craftable[0],components=components)