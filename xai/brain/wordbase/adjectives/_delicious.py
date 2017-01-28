

#calss header
class _DELICIOUS():
	def __init__(self,): 
		self.name = "DELICIOUS"
		self.definitions = [u'having a very pleasant taste or smell: ', u'used to describe a situation or activity that gives you great pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
