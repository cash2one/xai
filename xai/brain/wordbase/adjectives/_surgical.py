

#calss header
class _SURGICAL():
	def __init__(self,): 
		self.name = "SURGICAL"
		self.definitions = [u'used for medical operations: ', u'involved in performing medical operations: ', u'(of clothing) worn in order to treat a particular medical condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
