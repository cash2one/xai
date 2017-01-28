

#calss header
class _SOUTH():
	def __init__(self,): 
		self.name = "SOUTH"
		self.definitions = [u'towards the south: ', u'to or in the south of a country or region: ', u'(in or to) England, when considered in relation to Scotland', u'(in or to) Mexico and the other countries south of the US border with Mexico, when considered in relation to the US']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
