

#calss header
class _MONOLITHIC():
	def __init__(self,): 
		self.name = "MONOLITHIC"
		self.definitions = [u'too large, too regular, or without interesting differences, and unwilling or unable to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
