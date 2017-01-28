

#calss header
class _INCOMPETENT():
	def __init__(self,): 
		self.name = "INCOMPETENT"
		self.definitions = [u'not having the ability to do something as it should be done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
