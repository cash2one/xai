

#calss header
class _GLUEY():
	def __init__(self,): 
		self.name = "GLUEY"
		self.definitions = [u'covered with glue: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
