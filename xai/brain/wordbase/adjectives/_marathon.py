

#calss header
class _MARATHON():
	def __init__(self,): 
		self.name = "MARATHON"
		self.definitions = [u'related to marathons (= running races): ', u'used to describe something that takes a very long time and makes you very tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
