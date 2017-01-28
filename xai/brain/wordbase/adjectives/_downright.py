

#calss header
class _DOWNRIGHT():
	def __init__(self,): 
		self.name = "DOWNRIGHT"
		self.definitions = [u'(especially of something bad) extremely or very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
