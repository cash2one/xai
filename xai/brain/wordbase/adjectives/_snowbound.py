

#calss header
class _SNOWBOUND():
	def __init__(self,): 
		self.name = "SNOWBOUND"
		self.definitions = [u'(of vehicles or people) unable to travel because of heavy snow, or (of roads) not able to be travelled on or reached because of heavy snow: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
