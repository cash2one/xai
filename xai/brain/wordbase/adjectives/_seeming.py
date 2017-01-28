

#calss header
class _SEEMING():
	def __init__(self,): 
		self.name = "SEEMING"
		self.definitions = [u'appearing to be something, especially when this is not true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
