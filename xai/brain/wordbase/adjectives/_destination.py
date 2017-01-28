

#calss header
class _DESTINATION():
	def __init__(self,): 
		self.name = "DESTINATION"
		self.definitions = [u'worth making a special journey for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
