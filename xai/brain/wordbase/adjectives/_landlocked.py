

#calss header
class _LANDLOCKED():
	def __init__(self,): 
		self.name = "LANDLOCKED"
		self.definitions = [u'surrounded by the land of other countries and having no coast']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
