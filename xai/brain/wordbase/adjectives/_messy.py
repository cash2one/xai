

#calss header
class _MESSY():
	def __init__(self,): 
		self.name = "MESSY"
		self.definitions = [u'untidy: ', u'producing or causing dirt and untidiness: ', u'used to describe a situation that is confused and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
