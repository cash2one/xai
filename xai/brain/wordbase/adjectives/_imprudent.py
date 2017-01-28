

#calss header
class _IMPRUDENT():
	def __init__(self,): 
		self.name = "IMPRUDENT"
		self.definitions = [u'unwise, by failing to consider the likely results of your actions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
