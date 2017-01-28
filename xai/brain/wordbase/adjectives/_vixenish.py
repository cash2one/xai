

#calss header
class _VIXENISH():
	def __init__(self,): 
		self.name = "VIXENISH"
		self.definitions = [u'(of a woman) determined and difficult to control, sometimes in an unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
