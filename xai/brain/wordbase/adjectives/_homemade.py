

#calss header
class _HOMEMADE():
	def __init__(self,): 
		self.name = "HOMEMADE"
		self.definitions = [u'made at home and not bought from a shop: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
