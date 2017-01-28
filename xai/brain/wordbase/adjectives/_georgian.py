

#calss header
class _GEORGIAN():
	def __init__(self,): 
		self.name = "GEORGIAN"
		self.definitions = [u'relating to the period when Kings George I, II, III, and IV were kings of Britain, from 1714 to 1830: ', u'relating to the period when Kings George V and VI were kings of Britain, from 1910 to 1952', u'belonging to or relating to the country of Georgia, its people, or its language', u'belonging to or relating to the US state of Georgia or its people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
