

#calss header
class _INTRAVENOUSLY():
	def __init__(self,): 
		self.name = "INTRAVENOUSLY"
		self.definitions = [u'by means of a vein: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
