

#calss header
class _SHATTERING():
	def __init__(self,): 
		self.name = "SHATTERING"
		self.definitions = [u'making you feel extremely tired: ', u'making you feel extremely upset: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
