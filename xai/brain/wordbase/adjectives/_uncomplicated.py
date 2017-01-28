

#calss header
class _UNCOMPLICATED():
	def __init__(self,): 
		self.name = "UNCOMPLICATED"
		self.definitions = [u'simple, and not difficult to understand or deal with; not complicated: ', u'not having any complications (= extra medical problems that make it more difficult to treat an existing illness or condition): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
