

#calss header
class _ORNAMENTAL():
	def __init__(self,): 
		self.name = "ORNAMENTAL"
		self.definitions = [u'beautiful rather than useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
