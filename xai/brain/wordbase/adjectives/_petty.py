

#calss header
class _PETTY():
	def __init__(self,): 
		self.name = "PETTY"
		self.definitions = [u'not important and not worth giving attention to: ', u'complaining too much about things that are not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
