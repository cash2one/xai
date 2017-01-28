

#calss header
class _DOMINICAN():
	def __init__(self,): 
		self.name = "DOMINICAN"
		self.definitions = [u'belonging to or relating to Dominica or its people', u'belonging to or relating to the Dominican Republic, or its people', u'belonging to or relating to the Christian religious group of Dominicans: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
