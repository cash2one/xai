

#calss header
class _CURSORY():
	def __init__(self,): 
		self.name = "CURSORY"
		self.definitions = [u'quick and probably not detailed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
