

#calss header
class _FLACCID():
	def __init__(self,): 
		self.name = "FLACCID"
		self.definitions = [u'soft or weak rather than firm: ', u'weak and not effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
