

#calss header
class _ATMOSPHERIC():
	def __init__(self,): 
		self.name = "ATMOSPHERIC"
		self.definitions = [u'relating to the air or to the atmosphere: ', u'creating a special feeling, especially a mysterious or romantic feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
