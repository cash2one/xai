

#calss header
class _PITILESS():
	def __init__(self,): 
		self.name = "PITILESS"
		self.definitions = [u'cruel and having no pity: ', u'severe and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
