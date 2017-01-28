

#calss header
class _UNSOPHISTICATED():
	def __init__(self,): 
		self.name = "UNSOPHISTICATED"
		self.definitions = [u'not complicated, or not showing a good understanding of culture and fashion; not sophisticated']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
