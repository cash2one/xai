

#calss header
class _UNRULY():
	def __init__(self,): 
		self.name = "UNRULY"
		self.definitions = [u'Unruly people are difficult to control and often do not obey rules: ', u'Unruly hair is difficult to keep tidyneat, often sticking up or out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
