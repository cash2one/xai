

#calss header
class _IRRETRIEVABLE():
	def __init__(self,): 
		self.name = "IRRETRIEVABLE"
		self.definitions = [u'impossible to correct or return to a previously existing situation or condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
