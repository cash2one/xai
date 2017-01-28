

#calss header
class _INSULTING():
	def __init__(self,): 
		self.name = "INSULTING"
		self.definitions = [u'rude or offensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
