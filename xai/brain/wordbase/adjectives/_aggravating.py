

#calss header
class _AGGRAVATING():
	def __init__(self,): 
		self.name = "AGGRAVATING"
		self.definitions = [u'annoying: ', u'making something worse, such as a crime: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
