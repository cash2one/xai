

#calss header
class _DOCUMENTARY():
	def __init__(self,): 
		self.name = "DOCUMENTARY"
		self.definitions = [u'in the form of documents: ', u'giving facts and information about a subject in the form of a film or television or radio programme: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
