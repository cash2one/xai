

#calss header
class _IRREDEEMABLE():
	def __init__(self,): 
		self.name = "IRREDEEMABLE"
		self.definitions = [u'impossible to correct, improve, or change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
