

#calss header
class _FLORAL():
	def __init__(self,): 
		self.name = "FLORAL"
		self.definitions = [u'made of flowers, or decorated with pictures of flowers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
