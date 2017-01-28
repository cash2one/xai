

#calss header
class _EMOLLIENT():
	def __init__(self,): 
		self.name = "EMOLLIENT"
		self.definitions = [u'helping to treat dry, sore skin: ', u'making people calm and avoiding argument: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
