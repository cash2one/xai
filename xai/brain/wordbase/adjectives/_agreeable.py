

#calss header
class _AGREEABLE():
	def __init__(self,): 
		self.name = "AGREEABLE"
		self.definitions = [u'pleasant or pleasing: ', u'able to be accepted by everyone: ', u'willing to do or accept something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
