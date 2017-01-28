

#calss header
class _JAGGED():
	def __init__(self,): 
		self.name = "JAGGED"
		self.definitions = [u'rough and with sharp points: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
