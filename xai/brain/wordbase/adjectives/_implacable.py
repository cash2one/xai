

#calss header
class _IMPLACABLE():
	def __init__(self,): 
		self.name = "IMPLACABLE"
		self.definitions = [u'used to describe (someone who has) strong opinions or feelings that are impossible to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
