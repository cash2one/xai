

#calss header
class _DASTARDLY():
	def __init__(self,): 
		self.name = "DASTARDLY"
		self.definitions = [u'evil and cruel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
