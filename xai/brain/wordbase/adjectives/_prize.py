

#calss header
class _PRIZE():
	def __init__(self,): 
		self.name = "PRIZE"
		self.definitions = [u'A prize animal, flower, or vegetable is one that has won or deserves to win a prize in a competition because it is of very good quality: ', u'used to describe something that is a very good or important example of its type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
