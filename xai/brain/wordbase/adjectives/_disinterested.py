

#calss header
class _DISINTERESTED():
	def __init__(self,): 
		self.name = "DISINTERESTED"
		self.definitions = [u'having no personal involvement or receiving no personal advantage, and therefore free to act fairly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
