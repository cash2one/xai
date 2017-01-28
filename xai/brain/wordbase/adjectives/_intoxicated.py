

#calss header
class _INTOXICATED():
	def __init__(self,): 
		self.name = "INTOXICATED"
		self.definitions = [u'drunk: ', u'excited, happy, and slightly out of control because of love, success, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
