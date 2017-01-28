

#calss header
class _TABULAR():
	def __init__(self,): 
		self.name = "TABULAR"
		self.definitions = [u'(of information, especially in printed material) in the form of a table (= an arrangement of facts and numbers in rows or blocks)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
