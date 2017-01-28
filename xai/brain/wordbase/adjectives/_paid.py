

#calss header
class _PAID():
	def __init__(self,): 
		self.name = "PAID"
		self.definitions = [u'being given money for something: ', u'used in combination to refer to the amount of money that someone is given for their work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
