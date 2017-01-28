

#calss header
class _COMPLETE():
	def __init__(self,): 
		self.name = "COMPLETE"
		self.definitions = [u'very great or to the largest degree possible: ', u'with all the parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
