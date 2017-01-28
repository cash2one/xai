

#calss header
class _SILVER():
	def __init__(self,): 
		self.name = "SILVER"
		self.definitions = [u'made of silver, or of the colour of silver: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
