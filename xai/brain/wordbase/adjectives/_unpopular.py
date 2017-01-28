

#calss header
class _UNPOPULAR():
	def __init__(self,): 
		self.name = "UNPOPULAR"
		self.definitions = [u'not liked by many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
