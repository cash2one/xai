

#calss header
class _RIOTOUS():
	def __init__(self,): 
		self.name = "RIOTOUS"
		self.definitions = [u'very loud and uncontrolled, and full of energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
