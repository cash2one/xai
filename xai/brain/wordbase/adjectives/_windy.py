

#calss header
class _WINDY():
	def __init__(self,): 
		self.name = "WINDY"
		self.definitions = [u'with a lot of wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
