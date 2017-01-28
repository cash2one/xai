

#calss header
class _ENABLED():
	def __init__(self,): 
		self.name = "ENABLED"
		self.definitions = [u'provided with a particular type of equipment or technology, or having the necessary or correct system, device, or arrangement to use it: ', u'operated or made possible by the use of a particular thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
