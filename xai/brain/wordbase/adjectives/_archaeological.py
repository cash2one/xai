

#calss header
class _ARCHAEOLOGICAL():
	def __init__(self,): 
		self.name = "ARCHAEOLOGICAL"
		self.definitions = [u'involving or relating to archaeology: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
