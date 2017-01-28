

#calss header
class _ANAL():
	def __init__(self,): 
		self.name = "ANAL"
		self.definitions = [u'relating to the anus (= the opening at end of the intestines through which solid waste leaves the body): ', u'\u2192\xa0 anally retentive : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
