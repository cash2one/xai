

#calss header
class _BILIOUS():
	def __init__(self,): 
		self.name = "BILIOUS"
		self.definitions = [u'relating to an illness, caused by too much bile, that can cause vomiting: ', u'If someone is bilious, they are always in a bad mood: ', u'extremely unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
