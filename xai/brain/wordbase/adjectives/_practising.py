

#calss header
class _PRACTISING():
	def __init__(self,): 
		self.name = "PRACTISING"
		self.definitions = [u'actively involved in a religion: ', u'actively involved in a job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
