

#calss header
class _PACKED():
	def __init__(self,): 
		self.name = "PACKED"
		self.definitions = [u'completely full: ', u'very full of people: ', u'to have put your things into a suitcase, bag, box, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
