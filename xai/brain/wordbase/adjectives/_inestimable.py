

#calss header
class _INESTIMABLE():
	def __init__(self,): 
		self.name = "INESTIMABLE"
		self.definitions = [u'extremely great, or too great to be described or expressed exactly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
