

#calss header
class _BICYCLING():
	def __init__(self,): 
		self.name = "BICYCLING"
		self.definitions = [u'riding a bicycle or relating to riding bicycles: ', u'used to refer to a royal family with an informal personal style, especially the royal family of the Netherlands or Sweden : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
