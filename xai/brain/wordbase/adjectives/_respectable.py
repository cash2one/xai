

#calss header
class _RESPECTABLE():
	def __init__(self,): 
		self.name = "RESPECTABLE"
		self.definitions = [u'considered to be socially acceptable because of your good character, appearance, or behaviour: ', u'A respectable amount or quality is large enough or of a good enough standard to be acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
