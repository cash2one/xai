

#calss header
class _GHOSTLY():
	def __init__(self,): 
		self.name = "GHOSTLY"
		self.definitions = [u'pale and transparent: ', u'not loud or clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
