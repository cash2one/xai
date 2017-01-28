

#calss header
class _LTD():
	def __init__(self,): 
		self.name = "LTD"
		self.definitions = [u'written abbreviation for limited liability company: used in the name of a company whose owners have limited responsibility for the money that it owes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
