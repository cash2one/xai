

#calss header
class _MOTLEY():
	def __init__(self,): 
		self.name = "MOTLEY"
		self.definitions = [u'consisting of many different types that do not appear to go together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
