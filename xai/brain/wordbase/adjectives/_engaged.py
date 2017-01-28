

#calss header
class _ENGAGED():
	def __init__(self,): 
		self.name = "ENGAGED"
		self.definitions = [u'having formally agreed to marry: ', u'involved in something: ', u'busy doing something: ', u'If a phone or public toilet is engaged, someone is already using it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
