

#calss header
class _UNRELENTING():
	def __init__(self,): 
		self.name = "UNRELENTING"
		self.definitions = [u'extremely determined; never becoming weaker or admitting defeat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
