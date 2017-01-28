

#calss header
class _STERN():
	def __init__(self,): 
		self.name = "STERN"
		self.definitions = [u'severe, or showing disapproval: ', u'If something, such as a job, is stern, it is difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
