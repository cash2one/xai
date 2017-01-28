

#calss header
class _SIGNAL():
	def __init__(self,): 
		self.name = "SIGNAL"
		self.definitions = [u'noticeable and unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
