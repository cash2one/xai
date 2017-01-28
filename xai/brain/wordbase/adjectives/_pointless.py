

#calss header
class _POINTLESS():
	def __init__(self,): 
		self.name = "POINTLESS"
		self.definitions = [u'Something that is pointless has no purpose, and it is a waste of time doing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
