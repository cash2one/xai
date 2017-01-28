

#calss header
class _SERAPHIC():
	def __init__(self,): 
		self.name = "SERAPHIC"
		self.definitions = [u'beautiful in a way that suggests that someone is morally good and pure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
