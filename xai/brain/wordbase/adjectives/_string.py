

#calss header
class _STRING():
	def __init__(self,): 
		self.name = "STRING"
		self.definitions = [u'consisting of or relating to string instruments: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
