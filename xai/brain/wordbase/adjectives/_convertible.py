

#calss header
class _CONVERTIBLE():
	def __init__(self,): 
		self.name = "CONVERTIBLE"
		self.definitions = [u'able to be arranged in a different way and used for a different purpose: ', u'used to refer to a type of money that can be easily exchanged into other types of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
