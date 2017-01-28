

#calss header
class _SHALLOW():
	def __init__(self,): 
		self.name = "SHALLOW"
		self.definitions = [u'having only a short distance from the top to the bottom: ', u'breathing in which you only take a small amount of air into your lungs with each breath', u'not showing serious or careful thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
