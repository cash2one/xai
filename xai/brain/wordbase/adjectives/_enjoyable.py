

#calss header
class _ENJOYABLE():
	def __init__(self,): 
		self.name = "ENJOYABLE"
		self.definitions = [u'An enjoyable event or experience gives you pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
