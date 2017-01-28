

#calss header
class _GRITTY():
	def __init__(self,): 
		self.name = "GRITTY"
		self.definitions = [u'containing grit or like grit', u'brave and determined: ', u'showing all the unpleasant but true details of a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
