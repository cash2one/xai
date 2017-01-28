

#calss header
class _LUXURIOUS():
	def __init__(self,): 
		self.name = "LUXURIOUS"
		self.definitions = [u'very comfortable and expensive: ', u'giving great pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
