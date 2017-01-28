

#calss header
class _UNDEREMPLOYED():
	def __init__(self,): 
		self.name = "UNDEREMPLOYED"
		self.definitions = [u'not having enough work to do, or having a job that does not use all your skills']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
