

#calss header
class _WORRISOME():
	def __init__(self,): 
		self.name = "WORRISOME"
		self.definitions = [u'worrying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
