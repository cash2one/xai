

#calss header
class _SEXY():
	def __init__(self,): 
		self.name = "SEXY"
		self.definitions = [u'sexually attractive: ', u'used to describe something that attracts a lot of interest and excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
