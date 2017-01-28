

#calss header
class _UNMANAGEABLE():
	def __init__(self,): 
		self.name = "UNMANAGEABLE"
		self.definitions = [u'impossible to deal with or manage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
