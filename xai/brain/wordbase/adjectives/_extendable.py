

#calss header
class _EXTENDABLE():
	def __init__(self,): 
		self.name = "EXTENDABLE"
		self.definitions = [u'Something that is extendable can be made longer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
