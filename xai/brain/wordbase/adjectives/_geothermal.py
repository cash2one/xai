

#calss header
class _GEOTHERMAL():
	def __init__(self,): 
		self.name = "GEOTHERMAL"
		self.definitions = [u'of or connected with the heat inside the earth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
