

#calss header
class _RECURRENT():
	def __init__(self,): 
		self.name = "RECURRENT"
		self.definitions = [u'happening again many times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
