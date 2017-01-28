

#calss header
class _DISOBEDIENT():
	def __init__(self,): 
		self.name = "DISOBEDIENT"
		self.definitions = [u'refusing to do what someone in authority tells you to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
