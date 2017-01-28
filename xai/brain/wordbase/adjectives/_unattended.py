

#calss header
class _UNATTENDED():
	def __init__(self,): 
		self.name = "UNATTENDED"
		self.definitions = [u'not being watched or taken care of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
