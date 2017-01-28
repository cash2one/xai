

#calss header
class _JUSTIFIABLE():
	def __init__(self,): 
		self.name = "JUSTIFIABLE"
		self.definitions = [u'If something is justifiable, there is a good reason for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
