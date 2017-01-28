

#calss header
class _INDEFATIGABLE():
	def __init__(self,): 
		self.name = "INDEFATIGABLE"
		self.definitions = [u'always determined and energetic in trying to achieve something and never willing to admit defeat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
