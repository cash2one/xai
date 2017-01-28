

#calss header
class _GONE():
	def __init__(self,): 
		self.name = "GONE"
		self.definitions = [u'If something is gone, there is none of it left: ', u'dead: ', u'pregnant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
