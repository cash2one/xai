

#calss header
class _RELIEVED():
	def __init__(self,): 
		self.name = "RELIEVED"
		self.definitions = [u'happy that something unpleasant has not happened or has ended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
