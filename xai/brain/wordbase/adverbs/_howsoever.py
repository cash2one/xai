

#calss header
class _HOWSOEVER():
	def __init__(self,): 
		self.name = "HOWSOEVER"
		self.definitions = [u'formal for  however ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
