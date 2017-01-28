

#calss header
class _TERTIARY():
	def __init__(self,): 
		self.name = "TERTIARY"
		self.definitions = [u'relating to a third level or stage', u'relating to education in colleges and universities: ', u'A tertiary industry provides a service and is not involved with getting the materials with which products are made, or with making products.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
