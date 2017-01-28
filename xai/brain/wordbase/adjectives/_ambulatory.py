

#calss header
class _AMBULATORY():
	def __init__(self,): 
		self.name = "AMBULATORY"
		self.definitions = [u'relating to or describing people being treated for an injury or illness who are able to walk, and who, when treated in a hospital, are usually not staying for the night: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
