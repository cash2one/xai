

#calss header
class _EXTENDED():
	def __init__(self,): 
		self.name = "EXTENDED"
		self.definitions = [u'long or longer than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
