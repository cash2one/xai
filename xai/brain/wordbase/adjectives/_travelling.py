

#calss header
class _TRAVELLING():
	def __init__(self,): 
		self.name = "TRAVELLING"
		self.definitions = [u'moving from one place to another, especially to perform or while working, etc.: ', u'relating to or used for travel']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
