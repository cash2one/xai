

#calss header
class _BACKUP():
	def __init__(self,): 
		self.name = "BACKUP"
		self.definitions = [u'supporting the main singer, performer, etc. : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
