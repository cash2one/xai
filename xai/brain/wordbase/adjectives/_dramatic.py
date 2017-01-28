

#calss header
class _DRAMATIC():
	def __init__(self,): 
		self.name = "DRAMATIC"
		self.definitions = [u'very sudden or noticeable, or full of action and excitement: ', u'relating to plays and acting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
