

#calss header
class _SOCIETAL():
	def __init__(self,): 
		self.name = "SOCIETAL"
		self.definitions = [u'relating to or involving society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
