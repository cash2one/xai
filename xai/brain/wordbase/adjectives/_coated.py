

#calss header
class _COATED():
	def __init__(self,): 
		self.name = "COATED"
		self.definitions = [u'thickly covered: ', u'If your tongue is coated, it is covered with a layer of a greyish-white substance, often because you are ill.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
