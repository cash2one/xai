

#calss header
class _BACKSTAGE():
	def __init__(self,): 
		self.name = "BACKSTAGE"
		self.definitions = [u'in the area behind the stage in a theatre, especially the rooms in which actors change their clothes or where equipment is kept: ', u'If something happens backstage, it is not generally known about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
