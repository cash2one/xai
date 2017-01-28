

#calss header
class _UNCOUNTABLE():
	def __init__(self,): 
		self.name = "UNCOUNTABLE"
		self.definitions = [u'An uncountable noun is not used with "a" or "an" and cannot be made plural: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
