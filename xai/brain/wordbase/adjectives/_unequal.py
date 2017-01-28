

#calss header
class _UNEQUAL():
	def __init__(self,): 
		self.name = "UNEQUAL"
		self.definitions = [u'different in size, level, amount, etc.: ', u'not treating everyone the same; unfair: ', u'to not have the necessary ability, power, or qualities to achieve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
