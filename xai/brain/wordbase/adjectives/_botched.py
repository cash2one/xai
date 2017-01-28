

#calss header
class _BOTCHED():
	def __init__(self,): 
		self.name = "BOTCHED"
		self.definitions = [u'used to describe something, usually a job, that is done badly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
