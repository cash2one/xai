

#calss header
class _SOMETIME():
	def __init__(self,): 
		self.name = "SOMETIME"
		self.definitions = [u'(especially of a job or position) in the past but not any longer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
