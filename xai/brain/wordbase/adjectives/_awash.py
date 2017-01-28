

#calss header
class _AWASH():
	def __init__(self,): 
		self.name = "AWASH"
		self.definitions = [u'covered with a liquid, especially water: ', u'having an amount of something that is very large or larger than necessary or wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
