

#calss header
class _CRYPTIC():
	def __init__(self,): 
		self.name = "CRYPTIC"
		self.definitions = [u'mysterious and difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
