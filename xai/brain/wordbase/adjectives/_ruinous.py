

#calss header
class _RUINOUS():
	def __init__(self,): 
		self.name = "RUINOUS"
		self.definitions = [u'causing great harm and destruction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
