

#calss header
class _WILD():
	def __init__(self,): 
		self.name = "WILD"
		self.definitions = [u'uncontrolled, violent, or extreme: ', u'very unusual, often in a way that is attractive or exciting: ', u'used to refer to plants or animals that live or grow independently of people, in natural conditions and with natural characteristics: ', u'Wild land is not used to grow crops and has few people living in it: ', u'something that you say that is not based on facts and is probably wrong']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
