

#calss header
class _ASTOUNDED():
	def __init__(self,): 
		self.name = "ASTOUNDED"
		self.definitions = [u'very surprised or shocked: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
