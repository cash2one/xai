

#calss header
class _COSMIC():
	def __init__(self,): 
		self.name = "COSMIC"
		self.definitions = [u'relating to the universe and the natural processes that happen in it: ', u'very great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
