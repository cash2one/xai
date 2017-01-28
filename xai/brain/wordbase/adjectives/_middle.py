

#calss header
class _MIDDLE():
	def __init__(self,): 
		self.name = "MIDDLE"
		self.definitions = [u'in a central position: ', u'neither high nor low in importance, amount, or size: ', u'A middle child has the same number of older brothers and sisters as younger brothers and sisters: ', u'used to refer to a form of a particular language that existed between its earliest known stage and its present form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
