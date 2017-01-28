

#calss header
class _LIFELESS():
	def __init__(self,): 
		self.name = "LIFELESS"
		self.definitions = [u'dead: ', u'showing little energy or interest: ', u'not filled with or used by people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
