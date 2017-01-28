

#calss header
class _EVENTUAL():
	def __init__(self,): 
		self.name = "EVENTUAL"
		self.definitions = [u'happening or existing at a later time or at the end, especially after a lot of effort, problems, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
