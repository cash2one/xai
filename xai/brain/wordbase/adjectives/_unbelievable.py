

#calss header
class _UNBELIEVABLE():
	def __init__(self,): 
		self.name = "UNBELIEVABLE"
		self.definitions = [u'extremely surprising: ', u'unable to be believed because unlikely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
