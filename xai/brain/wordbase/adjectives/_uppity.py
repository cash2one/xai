

#calss header
class _UPPITY():
	def __init__(self,): 
		self.name = "UPPITY"
		self.definitions = [u'An uppity person behaves in an unpleasant way because they think that they are more important than they really are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
