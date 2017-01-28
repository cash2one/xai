

#calss header
class _UGLY():
	def __init__(self,): 
		self.name = "UGLY"
		self.definitions = [u'unpleasant to look at; not attractive: ', u'unpleasant and threatening or violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
