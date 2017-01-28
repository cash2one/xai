

#calss header
class _REPUGNANT():
	def __init__(self,): 
		self.name = "REPUGNANT"
		self.definitions = [u'If behaviour or beliefs, etc. are repugnant, they are very unpleasant, causing a feeling of disgust: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
