

#calss header
class _TREATABLE():
	def __init__(self,): 
		self.name = "TREATABLE"
		self.definitions = [u'A treatable illness or condition can be cured with drugs, exercises, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
