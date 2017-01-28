

#calss header
class _IBERIAN():
	def __init__(self,): 
		self.name = "IBERIAN"
		self.definitions = [u'the area of land that consists of Spain, Portugal, Andorra, Gibraltar, and part of France: ', u'relating to the Iberian Peninsula: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
