

#calss header
class _UNDIVIDED():
	def __init__(self,): 
		self.name = "UNDIVIDED"
		self.definitions = [u'existing as a whole, not in separate parts', u'complete attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
