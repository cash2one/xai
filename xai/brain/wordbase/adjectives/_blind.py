

#calss header
class _BLIND():
	def __init__(self,): 
		self.name = "BLIND"
		self.definitions = [u'unable to see: ', u'used to describe an extreme feeling that happens without thought or reason: ', u'to not be conscious of something or to refuse to notice something that is obvious to others: ', u'that a driver cannot see or cannot see around: ', u'used to refer to a scientific test in which either the people being tested or the person testing them, or both, do not know what is being tested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
