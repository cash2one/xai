

#calss header
class _BLASTED():
	def __init__(self,): 
		self.name = "BLASTED"
		self.definitions = [u'used in phrases to express anger: ', u'used to refer to a plant or piece of land that has been damaged or destroyed by extreme cold, heat, or wind: ', u'drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
