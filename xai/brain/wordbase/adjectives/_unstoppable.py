

#calss header
class _UNSTOPPABLE():
	def __init__(self,): 
		self.name = "UNSTOPPABLE"
		self.definitions = [u'unable to be stopped or prevented from developing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
