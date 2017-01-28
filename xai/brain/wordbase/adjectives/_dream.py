

#calss header
class _DREAM():
	def __init__(self,): 
		self.name = "DREAM"
		self.definitions = [u'the perfect house, job, etc., that you want more than any other']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
