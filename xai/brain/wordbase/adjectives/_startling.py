

#calss header
class _STARTLING():
	def __init__(self,): 
		self.name = "STARTLING"
		self.definitions = [u'surprising and sometimes worrying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
