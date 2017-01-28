

#calss header
class _SHIMMERING():
	def __init__(self,): 
		self.name = "SHIMMERING"
		self.definitions = [u'reflecting a gentle light that seems to move slightly: ', u'attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
