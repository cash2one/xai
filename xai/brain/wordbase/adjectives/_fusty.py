

#calss header
class _FUSTY():
	def __init__(self,): 
		self.name = "FUSTY"
		self.definitions = [u'not fresh and smelling unpleasant especially because of being left slightly wet: ', u'old-fashioned in ideas and beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
