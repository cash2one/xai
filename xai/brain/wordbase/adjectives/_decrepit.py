

#calss header
class _DECREPIT():
	def __init__(self,): 
		self.name = "DECREPIT"
		self.definitions = [u'in very bad condition because of being old, or not having been cared for, or having been used a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
