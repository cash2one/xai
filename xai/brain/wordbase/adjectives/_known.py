

#calss header
class _KNOWN():
	def __init__(self,): 
		self.name = "KNOWN"
		self.definitions = [u'used to refer to something or someone that is familiar to or understood by people: ', u'If someone or something is known as a particular name, that person or thing is called by that name: ', u'to tell people about something so that it becomes publicly known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
