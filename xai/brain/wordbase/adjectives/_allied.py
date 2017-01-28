

#calss header
class _ALLIED():
	def __init__(self,): 
		self.name = "ALLIED"
		self.definitions = [u'connected by a political or military agreement: ', u'similar or related in some way: ', u'combined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
