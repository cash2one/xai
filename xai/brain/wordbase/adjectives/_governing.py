

#calss header
class _GOVERNING():
	def __init__(self,): 
		self.name = "GOVERNING"
		self.definitions = [u'having the power to govern a country or an organization: ', u'having a controlling influence on something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
