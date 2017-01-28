

#calss header
class _NASAL():
	def __init__(self,): 
		self.name = "NASAL"
		self.definitions = [u'related to the nose: ', u"If a person's voice is nasal, it has a particular sound because air is going through their nose when they speak: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
