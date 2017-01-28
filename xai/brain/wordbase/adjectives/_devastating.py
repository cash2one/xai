

#calss header
class _DEVASTATING():
	def __init__(self,): 
		self.name = "DEVASTATING"
		self.definitions = [u'causing a lot of damage or destruction: ', u'making someone very shocked and upset: ', u'used to describe a personal quality that has a powerful effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
